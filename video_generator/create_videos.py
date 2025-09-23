#!/usr/bin/env python3
"""
Combine frames and audio into video files
"""

import os
import glob
from pathlib import Path
from moviepy.editor import *
import numpy as np
from PIL import Image

def create_video_from_frames_and_audio(frames_pattern, audio_file, output_file, fps=24):
    """Create video from image frames and audio"""
    
    # Get all frame files
    frame_files = sorted(glob.glob(frames_pattern))
    
    if not frame_files:
        print(f"No frames found for pattern: {frames_pattern}")
        return False
    
    print(f"Found {len(frame_files)} frames")
    
    # Create video from frames
    clip = ImageSequenceClip(frame_files, fps=fps)
    
    # Add audio if available
    if Path(audio_file).exists():
        print(f"Adding audio: {audio_file}")
        audio = AudioFileClip(audio_file)
        
        # Match video duration to audio duration
        if audio.duration > clip.duration:
            # Audio is longer, extend video by repeating last frame
            last_frame_duration = audio.duration - clip.duration
            last_frame = ImageClip(frame_files[-1], duration=last_frame_duration)
            clip = concatenate_videoclips([clip, last_frame])
        
        # Set audio
        clip = clip.set_audio(audio)
    
    # Write video
    print(f"Creating video: {output_file}")
    clip.write_videofile(output_file, fps=fps, verbose=False, logger=None)
    print(f"✅ Video created: {output_file}")
    
    return True

def main():
    output_dir = Path("output")
    
    # Create individual section videos
    sections = [
        ("section_00_Welcome_to_C-Cube_Cold_Wallet", "Welcome to C-Cube"),
        ("section_01_Getting_Started_-_Security_First", "Security First"),
        ("section_02_Creating_Your_First_Wallet", "Creating Your Wallet"),
        ("section_03_Understanding_Networks", "Understanding Networks"),
        ("section_04_Sending_Your_First_Transaction", "First Transaction")
    ]
    
    video_clips = []
    
    for section_prefix, section_name in sections:
        print(f"\n🎬 Processing: {section_name}")
        
        # Frame pattern
        frames_pattern = str(output_dir / f"{section_prefix}_frame_*.png")
        
        # Audio file
        audio_file = output_dir / f"{section_prefix.split('_')[1]}_audio.wav"
        
        # Output video
        output_video = output_dir / f"{section_prefix}.mp4"
        
        # Create video
        if create_video_from_frames_and_audio(frames_pattern, str(audio_file), str(output_video)):
            video_clips.append(str(output_video))
    
    # Create combined video
    if video_clips:
        print(f"\n🎬 Combining {len(video_clips)} videos into complete tutorial...")
        
        # Load all clips
        clips = [VideoFileClip(video_file) for video_file in video_clips]
        
        # Add intro text
        intro_text = TextClip("C-Cube Cold Wallet\nComplete Tutorial", 
                             fontsize=60, 
                             color='white', 
                             bg_color='black',
                             size=(1280, 720))
        intro_text = intro_text.set_duration(3)
        
        # Add outro text
        outro_text = TextClip("Thank you for watching!\nStay secure with C-Cube", 
                             fontsize=50, 
                             color='white', 
                             bg_color='black',
                             size=(1280, 720))
        outro_text = outro_text.set_duration(3)
        
        # Combine all clips
        all_clips = [intro_text] + clips + [outro_text]
        final_video = concatenate_videoclips(all_clips)
        
        # Save final video
        final_output = output_dir / "CCube_Complete_Tutorial_Final.mp4"
        final_video.write_videofile(str(final_output), fps=24)
        
        print(f"\n🎉 Complete tutorial created: {final_output}")
        print(f"📊 Total duration: {final_video.duration:.1f} seconds")
    
    print("\n✅ All videos created successfully!")

if __name__ == "__main__":
    main()
