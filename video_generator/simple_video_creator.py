#!/usr/bin/env python3
"""
Simple video creator using FFmpeg commands
"""

import os
import subprocess
import glob
from pathlib import Path

def create_video_with_ffmpeg(frames_pattern, audio_file, output_file, fps=6):
    """Create video using FFmpeg"""
    
    # Get frame files
    frame_files = sorted(glob.glob(frames_pattern))
    if not frame_files:
        print(f"No frames found: {frames_pattern}")
        return False
    
    print(f"Creating video from {len(frame_files)} frames")
    
    # Create temporary frames list for ffmpeg
    frames_dir = Path(frame_files[0]).parent
    temp_pattern = frames_dir / "temp_%04d.png"
    
    # Copy/rename frames to sequential pattern ffmpeg expects
    for i, frame_file in enumerate(frame_files):
        temp_name = frames_dir / f"temp_{i:04d}.png"
        if not temp_name.exists():
            os.system(f"cp '{frame_file}' '{temp_name}'")
    
    # FFmpeg command to create video from frames
    cmd = [
        'ffmpeg', '-y',  # Overwrite output file
        '-framerate', str(fps),  # Input framerate
        '-i', str(frames_dir / 'temp_%04d.png'),  # Input pattern
        '-c:v', 'libx264',  # Video codec
        '-pix_fmt', 'yuv420p',  # Pixel format for compatibility
        '-r', str(fps),  # Output framerate
        str(output_file)
    ]
    
    try:
        # Run FFmpeg
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Video created: {output_file}")
            
            # Add audio if available
            if Path(audio_file).exists():
                print(f"🎵 Adding audio: {audio_file}")
                
                # Create version with audio
                audio_output = str(output_file).replace('.mp4', '_with_audio.mp4')
                audio_cmd = [
                    'ffmpeg', '-y',
                    '-i', str(output_file),  # Video input
                    '-i', str(audio_file),   # Audio input
                    '-c:v', 'copy',          # Copy video stream
                    '-c:a', 'aac',           # Audio codec
                    '-shortest',             # End when shortest stream ends
                    audio_output
                ]
                
                audio_result = subprocess.run(audio_cmd, capture_output=True, text=True)
                if audio_result.returncode == 0:
                    print(f"✅ Video with audio created: {audio_output}")
                    # Replace original with audio version
                    os.rename(audio_output, output_file)
                else:
                    print(f"⚠️  Audio addition failed: {audio_result.stderr}")
            
            # Clean up temp files
            for temp_file in glob.glob(str(frames_dir / 'temp_*.png')):
                os.remove(temp_file)
            
            return True
        else:
            print(f"❌ FFmpeg failed: {result.stderr}")
            return False
    
    except FileNotFoundError:
        print("❌ FFmpeg not found. Please install FFmpeg.")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_demo_video():
    """Create a demo video from one section"""
    output_dir = Path("output")
    
    # Use the first section as demo
    section = "section_00_Welcome_to_C-Cube_Cold_Wallet"
    frames_pattern = str(output_dir / f"{section}_frame_*.png")
    audio_file = output_dir / "section_00_audio.wav"
    output_file = output_dir / "demo_tutorial.mp4"
    
    print("🎬 Creating demo tutorial video...")
    print(f"Frames: {frames_pattern}")
    print(f"Audio: {audio_file}")
    print(f"Output: {output_file}")
    
    success = create_video_with_ffmpeg(frames_pattern, str(audio_file), str(output_file))
    
    if success:
        print(f"\n🎉 Demo video created successfully!")
        print(f"📁 Location: {output_file}")
        print(f"🎥 You can now play the video to see your robot tutorial!")
        
        # Show file size
        if output_file.exists():
            size_mb = output_file.stat().st_size / (1024 * 1024)
            print(f"📊 File size: {size_mb:.1f} MB")
    else:
        print("❌ Demo video creation failed")

def main():
    """Main function"""
    print("🤖 C-Cube Video Creator")
    print("=" * 40)
    
    # Check if we have content to work with
    output_dir = Path("output")
    if not output_dir.exists():
        print("❌ No output directory found. Run the generator first.")
        return
    
    # Check for frames
    frame_files = list(output_dir.glob("*.png"))
    audio_files = list(output_dir.glob("*.wav"))
    
    print(f"📊 Found {len(frame_files)} frames and {len(audio_files)} audio files")
    
    if frame_files and audio_files:
        create_demo_video()
    else:
        print("❌ No frames or audio files found. Run the generator first.")

if __name__ == "__main__":
    main()
