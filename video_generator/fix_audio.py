#!/usr/bin/env python3
"""
Fix Audio in Tutorial Videos
Properly embed robot voice audio into MP4 videos
"""

import os
import subprocess
import glob
from pathlib import Path

def add_audio_to_video(video_file, audio_file, output_file):
    """Add audio to video with proper synchronization"""
    
    print(f"🎵 Adding audio to {video_file.name}...")
    
    # FFmpeg command with proper audio handling
    cmd = [
        'ffmpeg', '-y',
        '-i', str(video_file),    # Video input
        '-i', str(audio_file),    # Audio input
        '-c:v', 'copy',           # Copy video stream
        '-c:a', 'aac',            # AAC audio codec
        '-b:a', '128k',           # Audio bitrate
        '-shortest',              # Match shortest duration
        '-map', '0:v:0',          # Map video from first input
        '-map', '1:a:0',          # Map audio from second input
        str(output_file)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ Audio successfully added")
            return True
        else:
            print(f"   ❌ Failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def create_video_with_audio(frames_pattern, audio_file, output_file, section_name, fps=8):
    """Create video from frames with properly embedded audio"""
    
    print(f"\n🎬 Creating {section_name} with Audio...")
    
    # Get frame files
    frame_files = sorted(glob.glob(frames_pattern))
    if not frame_files:
        print(f"❌ No frames found")
        return False
    
    print(f"   📊 {len(frame_files)} frames, audio: {audio_file.name}")
    
    # Create temporary frames directory
    temp_dir = Path("temp_frames")
    temp_dir.mkdir(exist_ok=True)
    
    # Copy frames with sequential naming
    for i, frame_file in enumerate(frame_files):
        temp_name = temp_dir / f"frame_{i:04d}.png"
        os.system(f"cp '{frame_file}' '{temp_name}'")
    
    # Get audio duration for video length matching
    audio_duration_cmd = [
        'ffprobe', '-i', str(audio_file),
        '-show_entries', 'format=duration',
        '-v', 'quiet', '-of', 'csv=p=0'
    ]
    
    try:
        result = subprocess.run(audio_duration_cmd, capture_output=True, text=True)
        audio_duration = float(result.stdout.strip())
        print(f"   🎵 Audio duration: {audio_duration:.1f} seconds")
    except:
        audio_duration = len(frame_files) / fps
        print(f"   ⚠️  Using estimated duration: {audio_duration:.1f} seconds")
    
    # Create video with proper audio sync
    video_cmd = [
        'ffmpeg', '-y',
        '-framerate', str(fps),
        '-i', str(temp_dir / 'frame_%04d.png'),
        '-i', str(audio_file),
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-r', str(fps),
        '-shortest',
        '-map', '0:v:0',
        '-map', '1:a:0',
        str(output_file)
    ]
    
    try:
        result = subprocess.run(video_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ Video with audio created successfully")
            
            # Clean up temp files
            for temp_file in temp_dir.glob("*.png"):
                temp_file.unlink()
            temp_dir.rmdir()
            
            # Verify audio is present
            verify_cmd = ['ffprobe', '-i', str(output_file), '-hide_banner']
            verify_result = subprocess.run(verify_cmd, capture_output=True, text=True)
            if 'Audio:' in verify_result.stderr:
                print(f"   🎤 Audio track confirmed in video")
            else:
                print(f"   ⚠️  Warning: No audio track detected")
            
            return True
        else:
            print(f"   ❌ Failed: {result.stderr}")
            return False
    
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main():
    """Fix audio in all tutorial videos"""
    
    print("🔧 FIXING AUDIO IN C-CUBE TUTORIAL VIDEOS")
    print("=" * 50)
    
    output_dir = Path("output")
    
    # Tutorial sections with their audio files
    sections = [
        ("section_00_Welcome_to_C-Cube_Cold_Wallet", "section_00_audio.wav", "Welcome_Tutorial_WithAudio.mp4", "Welcome Tutorial"),
        ("section_01_Getting_Started_-_Security_First", "section_01_audio.wav", "Security_Tutorial_WithAudio.mp4", "Security Tutorial"),
        ("section_02_Creating_Your_First_Wallet", "section_02_audio.wav", "Creating_Wallet_Tutorial_WithAudio.mp4", "Wallet Creation Tutorial"),
        ("section_03_Understanding_Networks", "section_03_audio.wav", "Networks_Tutorial_WithAudio.mp4", "Networks Tutorial"),
        ("section_04_Sending_Your_First_Transaction", "section_04_audio.wav", "Transactions_Tutorial_WithAudio.mp4", "Transactions Tutorial")
    ]
    
    successful_videos = []
    
    for section_prefix, audio_name, output_name, display_name in sections:
        frames_pattern = str(output_dir / f"{section_prefix}_frame_*.png")
        audio_file = output_dir / audio_name
        output_file = output_dir / output_name
        
        if audio_file.exists():
            success = create_video_with_audio(frames_pattern, audio_file, output_file, display_name)
            if success:
                successful_videos.append(output_file)
        else:
            print(f"⚠️  Audio file not found: {audio_name}")
    
    # Test audio playback
    if successful_videos:
        print(f"\n🎉 AUDIO INTEGRATION COMPLETE!")
        print(f"📋 Videos with Audio:")
        
        for video in successful_videos:
            size_mb = video.stat().st_size / (1024 * 1024)
            print(f"   🎥 {video.name} ({size_mb:.1f} MB)")
        
        print(f"\n🎵 TESTING AUDIO:")
        print(f"   1. Try playing: {successful_videos[0].name}")
        print(f"   2. Volume should be audible")
        print(f"   3. Robot voice should narrate tutorial")
        
        # Play first video to test
        test_video = successful_videos[0]
        print(f"\n🎬 Opening {test_video.name} for audio test...")
        os.system(f"open '{test_video}'")
        
        print(f"\n💡 If you still don't hear audio:")
        print(f"   • Check your system volume")
        print(f"   • Try a different video player")
        print(f"   • Ensure speakers/headphones connected")
        print(f"   • Test with: afplay {output_dir}/section_00_audio.wav")
    
    else:
        print(f"❌ No videos with audio were created successfully")

if __name__ == "__main__":
    main()
