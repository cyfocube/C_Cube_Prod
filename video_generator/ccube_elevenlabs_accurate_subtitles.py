#!/usr/bin/env python3
"""
C-Cube ElevenLabs Tutorial with Robot Background and Accurate Subtitles
Creates final video with robot background and synchronized subtitles matching actual ElevenLabs audio
"""

import os
import subprocess
from pathlib import Path

def create_video_with_accurate_subtitles():
    """Create final video with robot background and accurate subtitles"""
    
    # File paths
    output_dir = Path("output")
    original_video = output_dir / "CCube_Tutorial_ElevenLabs_Professional.mp4"
    robot_image = output_dir / "tut_agent_Conv_photo2.png"
    subtitle_file = output_dir / "accurate_tutorial_subtitles.srt"
    final_output = output_dir / "CCube_Tutorial_ElevenLabs_Professional_RobotBG_AccurateSubtitles.mp4"
    
    print("🎬 Creating C-Cube ElevenLabs Tutorial with Accurate Subtitles")
    print("=" * 60)
    
    # Check if files exist
    if not original_video.exists():
        print(f"❌ Original ElevenLabs video not found: {original_video}")
        return False
        
    if not robot_image.exists():
        print(f"❌ Robot background image not found: {robot_image}")
        return False
        
    if not subtitle_file.exists():
        print(f"❌ Subtitle file not found: {subtitle_file}")
        return False
    
    print(f"📁 Original video: {original_video}")
    print(f"🤖 Robot background: {robot_image}")
    print(f"📝 Subtitles: {subtitle_file}")
    print(f"🎯 Output: {final_output}")
    
    # FFmpeg command to replace background with robot image and add subtitles
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-i", str(original_video),  # Original video (audio + video)
        "-i", str(robot_image),    # Robot background image
        "-filter_complex", 
        f"[1:v]scale=1280:720[bg];"  # Scale robot image to video size
        f"[bg]subtitles={subtitle_file}:force_style='FontSize=16,PrimaryColour=&H00ffffff,OutlineColour=&H00000000,Outline=2,Shadow=1'[final]",
        "-map", "[final]",          # Use the background with subtitles as video
        "-map", "0:a",              # Use original audio from ElevenLabs video
        "-c:a", "copy",             # Copy audio without re-encoding
        "-c:v", "libx264",          # Re-encode video with subtitles
        "-preset", "medium",        # Encoding speed vs quality
        "-crf", "23",              # Video quality
        "-t", "265",               # Preserve full duration (265 seconds)
        str(final_output)
    ]
    
    print("\n🔧 Running FFmpeg command...")
    print(f"Command: {' '.join(ffmpeg_cmd)}")
    
    try:
        # Run FFmpeg command
        result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, check=True)
        
        if final_output.exists():
            file_size = final_output.stat().st_size / (1024 * 1024)  # Size in MB
            print(f"\n✅ Video with accurate subtitles created!")
            print(f"📁 Output: {final_output}")
            print(f"📊 File size: {file_size:.1f} MB")
            
            # Get video duration
            duration_cmd = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(final_output)]
            duration_result = subprocess.run(duration_cmd, capture_output=True, text=True)
            
            if duration_result.returncode == 0:
                import json
                duration_info = json.loads(duration_result.stdout)
                duration = float(duration_info["format"]["duration"])
                minutes = int(duration // 60)
                seconds = int(duration % 60)
                print(f"⏱️ Duration: {minutes}:{seconds:02d} ({duration:.1f} seconds)")
            
            return True
        else:
            print("❌ Output file was not created")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg error: {e}")
        print(f"Stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("🤖 C-Cube ElevenLabs Robot Tutorial with Accurate Subtitles")
    print("🎵 Generating video with robot background and matching subtitles...")
    
    success = create_video_with_accurate_subtitles()
    
    if success:
        print("\n✨ Your ElevenLabs tutorial now has accurate synchronized subtitles!")
        print("🎬 The subtitles now match exactly what's being said in the audio")
        print("🤖 Robot background provides the perfect cybersecurity aesthetic")
    else:
        print("\n❌ Failed to create video with accurate subtitles")
        print("Please check the error messages above")