#!/usr/bin/env python3
"""
Complete MP4 Video Generator for C-Cube Tutorials
"""

import os
import subprocess
import glob
from pathlib import Path

def create_section_video(section_prefix, section_name, fps=6):
    """Create MP4 video for a tutorial section"""
    
    output_dir = Path("output")
    frames_pattern = str(output_dir / f"{section_prefix}_frame_*.png")
    audio_file = output_dir / f"{section_prefix.split('_')[1]}_audio.wav"
    output_file = output_dir / f"{section_name}_Tutorial.mp4"
    
    print(f"\n🎬 Creating {section_name} Tutorial Video...")
    
    # Get frame files
    frame_files = sorted(glob.glob(frames_pattern))
    if not frame_files:
        print(f"❌ No frames found: {frames_pattern}")
        return None
    
    print(f"   📊 {len(frame_files)} frames found")
    
    # Create temporary frames with sequential naming
    frames_dir = Path(frame_files[0]).parent
    temp_pattern = frames_dir / f"temp_{section_name}_%04d.png"
    
    # Copy frames to sequential pattern
    for i, frame_file in enumerate(frame_files):
        temp_name = frames_dir / f"temp_{section_name}_{i:04d}.png"
        if not temp_name.exists():
            os.system(f"cp '{frame_file}' '{temp_name}'")
    
    # FFmpeg command to create video
    cmd = [
        'ffmpeg', '-y',  # Overwrite output
        '-framerate', str(fps),
        '-i', str(frames_dir / f'temp_{section_name}_%04d.png'),
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-r', str(fps),
        str(output_file)
    ]
    
    try:
        # Create video from frames
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ Video frames processed")
            
            # Add audio if available
            if audio_file.exists():
                print(f"   🎵 Adding robot voice audio...")
                
                audio_output = str(output_file).replace('.mp4', '_with_audio.mp4')
                audio_cmd = [
                    'ffmpeg', '-y',
                    '-i', str(output_file),   # Video input
                    '-i', str(audio_file),    # Audio input
                    '-c:v', 'copy',           # Copy video
                    '-c:a', 'aac',            # Audio codec
                    '-shortest',              # End when shortest stream ends
                    audio_output
                ]
                
                audio_result = subprocess.run(audio_cmd, capture_output=True, text=True)
                if audio_result.returncode == 0:
                    # Replace original with audio version
                    os.rename(audio_output, output_file)
                    print(f"   ✅ Audio added successfully")
                else:
                    print(f"   ⚠️  Audio failed: {audio_result.stderr}")
            
            # Clean up temp files
            for temp_file in glob.glob(str(frames_dir / f'temp_{section_name}_*.png')):
                os.remove(temp_file)
            
            # Get file size
            if output_file.exists():
                size_mb = output_file.stat().st_size / (1024 * 1024)
                print(f"   📊 Video size: {size_mb:.1f} MB")
            
            return output_file
        else:
            print(f"   ❌ FFmpeg failed: {result.stderr}")
            return None
    
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None

def create_combined_video(video_files, output_name="CCube_Complete_Tutorial"):
    """Combine multiple videos into one"""
    
    if not video_files:
        return None
    
    output_dir = Path("output")
    output_file = output_dir / f"{output_name}.mp4"
    
    print(f"\n🎬 Creating Combined Tutorial Video...")
    print(f"   📊 Combining {len(video_files)} videos")
    
    # Create file list for FFmpeg
    filelist_path = output_dir / "video_list.txt"
    with open(filelist_path, 'w') as f:
        for video_file in video_files:
            f.write(f"file '{video_file}'\n")
    
    # FFmpeg command to concatenate videos
    cmd = [
        'ffmpeg', '-y',
        '-f', 'concat',
        '-safe', '0',
        '-i', str(filelist_path),
        '-c', 'copy',
        str(output_file)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            # Clean up
            os.remove(filelist_path)
            
            # Get file size
            size_mb = output_file.stat().st_size / (1024 * 1024)
            print(f"   ✅ Combined video created: {size_mb:.1f} MB")
            
            return output_file
        else:
            print(f"   ❌ Combination failed: {result.stderr}")
            return None
    
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None

def main():
    """Main function"""
    print("🎥 C-Cube Complete MP4 Video Generator")
    print("=" * 50)
    
    # Check for content
    output_dir = Path("output")
    if not output_dir.exists():
        print("❌ No output directory found. Run the generator first.")
        return
    
    frame_files = list(output_dir.glob("*.png"))
    audio_files = list(output_dir.glob("*.wav"))
    
    print(f"📊 Found {len(frame_files)} frames and {len(audio_files)} audio files")
    
    if not frame_files or not audio_files:
        print("❌ Missing frames or audio files. Run the generator first.")
        return
    
    # Tutorial sections
    sections = [
        ("section_00_Welcome_to_C-Cube_Cold_Wallet", "Welcome"),
        ("section_01_Getting_Started_-_Security_First", "Security"),
        ("section_02_Creating_Your_First_Wallet", "Creating_Wallet"),
        ("section_03_Understanding_Networks", "Networks"),
        ("section_04_Sending_Your_First_Transaction", "Transactions")
    ]
    
    created_videos = []
    
    # Create individual videos
    for section_prefix, section_name in sections:
        video_path = create_section_video(section_prefix, section_name)
        if video_path:
            created_videos.append(video_path)
    
    # Create combined video
    if created_videos:
        combined_video = create_combined_video(created_videos)
        
        print(f"\n🎉 Video Generation Complete!")
        print(f"📁 Output directory: {output_dir}")
        print(f"\n📋 Created Videos:")
        
        for video in created_videos:
            print(f"   🎥 {video.name}")
        
        if combined_video:
            print(f"   🎬 {combined_video.name} (Complete Tutorial)")
        
        print(f"\n💡 Usage:")
        print(f"   • Play individual videos for specific topics")
        print(f"   • Use complete tutorial for full walkthrough")
        print(f"   • Share videos for user education")
        print(f"   • Integrate into your wallet app")
        
        # Show total duration estimate
        total_videos = len(created_videos)
        estimated_duration = total_videos * 10  # Rough estimate
        print(f"\n📊 Statistics:")
        print(f"   • {total_videos} tutorial videos created")
        print(f"   • ~{estimated_duration} seconds total content")
        print(f"   • Robot narrator with voice synthesis")
        print(f"   • Professional tutorial quality")
    
    else:
        print("❌ No videos were created successfully")

if __name__ == "__main__":
    main()
