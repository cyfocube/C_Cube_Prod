#!/usr/bin/env python3
"""
C-Cube ElevenLabs Robot Background Replacer
Takes the existing ElevenLabs tutorial and replaces background with animated robots
"""

import os
import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess
import json
import random
import tempfile

class CCubeElevenLabsRobotReplacer:
    """Replace background in ElevenLabs video with animated robots"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.width = 1280
        self.height = 720
        self.fps = 15
        
        # Source video with ElevenLabs audio
        self.source_video = "output/CCube_Tutorial_ElevenLabs_Professional.mp4"
        self.robot_bg = "output/tut_agent_Conv_photo.png"
        
        # ElevenLabs API key
        self.elevenlabs_api_key = "sk_0eefffd1f15a4dd4521cac51d19cfced520fa2a082026e30"
        
        print("🤖 C-Cube ElevenLabs Robot Background Replacer")
        print(f"🎥 Source Video: {self.source_video}")
        print(f"🖼️  Robot Background: {self.robot_bg}")
        print("✨ Adding animated robot background to ElevenLabs tutorial!")
    
    def get_video_info(self):
        """Get information about the source video"""
        try:
            cmd = f'ffprobe -v quiet -print_format json -show_streams "{self.source_video}"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                info = json.loads(result.stdout)
                video_stream = next((s for s in info['streams'] if s['codec_type'] == 'video'), None)
                audio_stream = next((s for s in info['streams'] if s['codec_type'] == 'audio'), None)
                
                if video_stream:
                    duration = float(video_stream.get('duration', 0))
                    fps = eval(video_stream.get('r_frame_rate', '15/1'))
                    total_frames = int(duration * fps)
                    
                    print(f"📊 Video Info:")
                    print(f"   Duration: {duration:.1f} seconds")
                    print(f"   FPS: {fps}")
                    print(f"   Total Frames: {total_frames}")
                    print(f"   Has Audio: {'Yes' if audio_stream else 'No'}")
                    
                    return {
                        'duration': duration,
                        'fps': fps,
                        'total_frames': total_frames,
                        'has_audio': audio_stream is not None
                    }
            
            print("⚠️  Could not get video info, using defaults")
            return {'duration': 265, 'fps': 15, 'total_frames': 3975, 'has_audio': True}
            
        except Exception as e:
            print(f"⚠️  Error getting video info: {e}")
            return {'duration': 265, 'fps': 15, 'total_frames': 3975, 'has_audio': True}
    
    def get_fonts(self):
        """Get fonts for text rendering"""
        try:
            return {
                'title': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48),
                'subtitle': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36),
                'body': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28),
                'small': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20),
            }
        except:
            default = ImageFont.load_default()
            return {k: default for k in ['title', 'subtitle', 'body', 'small']}
    
    def load_robot_background(self):
        """Load and prepare the robot background image"""
        try:
            robot_img = Image.open(self.robot_bg)
            # Resize to fit our video dimensions
            robot_img = robot_img.resize((self.width, self.height), Image.Resampling.LANCZOS)
            print(f"✅ Loaded robot background: {robot_img.size}")
            return robot_img
        except Exception as e:
            print(f"⚠️  Warning: Could not load robot image: {e}")
            # Create a fallback dark background
            return Image.new('RGB', (self.width, self.height), (20, 20, 20))
    
    def create_eye_blink_mask(self, robot_base, blink_robot1=False, blink_robot2=False):
        """Create blinking effect by darkening eye areas"""
        img = robot_base.copy()
        draw = ImageDraw.Draw(img)
        
        # Adjusted eye positions for the actual robot image
        # You may need to fine-tune these coordinates based on your robot image
        
        # Robot 1 (left robot) eye positions - adjust these coordinates
        robot1_left_eye = (300, 200, 330, 220)    # (x1, y1, x2, y2)
        robot1_right_eye = (350, 200, 380, 220)
        
        # Robot 2 (right robot) eye positions - adjust these coordinates  
        robot2_left_eye = (800, 200, 830, 220)
        robot2_right_eye = (850, 200, 880, 220)
        
        # Create blink effect by drawing dark ellipses over eyes
        if blink_robot1:
            # Draw black ellipses to simulate closed eyes
            draw.ellipse(robot1_left_eye, fill=(0, 0, 0))
            draw.ellipse(robot1_right_eye, fill=(0, 0, 0))
        
        if blink_robot2:
            draw.ellipse(robot2_left_eye, fill=(0, 0, 0))
            draw.ellipse(robot2_right_eye, fill=(0, 0, 0))
        
        return img
    
    def add_elevenlabs_overlay(self, base_img, frame_number, total_frames):
        """Add overlay text indicating ElevenLabs professional narration"""
        img = base_img.copy()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Colors
        primary = (0, 204, 51)      # #00cc33
        secondary = (0, 255, 65)    # #00ff41
        text_color = (255, 255, 255)
        elevenlabs_color = (138, 43, 226)  # Purple for ElevenLabs
        overlay_bg = (0, 0, 0, 180)  # Semi-transparent black
        
        # Create bottom overlay area
        overlay_height = 120
        overlay_y = self.height - overlay_height
        
        # Draw semi-transparent overlay
        overlay = Image.new('RGBA', (self.width, overlay_height), overlay_bg)
        img.paste(overlay, (0, overlay_y), overlay)
        
        # Main title
        title = "C-Cube Cold Wallet Tutorial"
        title_y = overlay_y + 15
        title_bbox = draw.textbbox((0, 0), title, font=fonts['title'])
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (self.width - title_width) // 2
        
        # Title with shadow
        draw.text((title_x + 2, title_y + 2), title, fill=(0, 0, 0), font=fonts['title'])
        draw.text((title_x, title_y), title, fill=primary, font=fonts['title'])
        
        # ElevenLabs branding
        elevenlabs_text = "🎙️ Professional AI Narration by ElevenLabs"
        elevenlabs_y = title_y + 55
        elevenlabs_bbox = draw.textbbox((0, 0), elevenlabs_text, font=fonts['body'])
        elevenlabs_width = elevenlabs_bbox[2] - elevenlabs_bbox[0]
        elevenlabs_x = (self.width - elevenlabs_width) // 2
        draw.text((elevenlabs_x, elevenlabs_y), elevenlabs_text, fill=elevenlabs_color, font=fonts['body'])
        
        # Progress indicator
        progress_text = f"Frame {frame_number + 1:,} of {total_frames:,}"
        progress_y = overlay_y + 85
        progress_bbox = draw.textbbox((0, 0), progress_text, font=fonts['small'])
        progress_width = progress_bbox[2] - progress_bbox[0]
        progress_x = (self.width - progress_width) // 2
        draw.text((progress_x, progress_y), progress_text, fill=secondary, font=fonts['small'])
        
        # C-Cube logo in corner
        logo_text = "C-CUBE"
        logo_bbox = draw.textbbox((0, 0), logo_text, font=fonts['body'])
        logo_x = 20
        logo_y = 20
        draw.text((logo_x, logo_y), logo_text, fill=primary, font=fonts['body'])
        
        # ElevenLabs API indicator in top right
        api_text = "🔊 ElevenLabs AI"
        api_bbox = draw.textbbox((0, 0), api_text, font=fonts['small'])
        api_width = api_bbox[2] - api_bbox[0]
        api_x = self.width - api_width - 20
        api_y = 20
        draw.text((api_x, api_y), api_text, fill=elevenlabs_color, font=fonts['small'])
        
        return img
    
    def create_robot_frames(self, total_frames):
        """Create all frames with robot background and blinking animations"""
        print(f"🎬 Creating {total_frames} robot frames...")
        
        robot_base = self.load_robot_background()
        frame_files = []
        
        # Create temporary directory for frames
        frames_dir = self.output_dir / "elevenlabs_robot_frames"
        frames_dir.mkdir(exist_ok=True)
        
        for frame_i in range(total_frames):
            if frame_i % 200 == 0:  # Progress update every 200 frames
                print(f"📊 Progress: {frame_i}/{total_frames} frames ({frame_i/total_frames*100:.1f}%)")
            
            # Determine speaking patterns (alternating robots every 30 seconds or so)
            cycle_length = int(self.fps * 30)  # 30 seconds per robot
            current_cycle = frame_i // cycle_length
            robot1_speaking = (current_cycle % 2 == 0)
            robot2_speaking = not robot1_speaking
            
            # Create realistic blinking patterns
            # More frequent blinking for the speaking robot
            if robot1_speaking:
                blink_robot1 = (frame_i % 45 == 0) or (frame_i % 67 == 0) or (random.random() < 0.02)
                blink_robot2 = (frame_i % 89 == 0) or (random.random() < 0.01)
            else:
                blink_robot1 = (frame_i % 89 == 0) or (random.random() < 0.01)  
                blink_robot2 = (frame_i % 45 == 0) or (frame_i % 67 == 0) or (random.random() < 0.02)
            
            # Create frame with blinking
            frame_img = self.create_eye_blink_mask(robot_base, blink_robot1, blink_robot2)
            
            # Add ElevenLabs professional overlay
            final_frame = self.add_elevenlabs_overlay(frame_img, frame_i, total_frames)
            
            # Save frame
            frame_filename = f"elevenlabs_robot_frame_{frame_i:06d}.png"
            frame_path = frames_dir / frame_filename
            final_frame.save(frame_path, "PNG", optimize=True)
            frame_files.append(str(frame_path))
        
        print(f"✅ Created {len(frame_files)} robot frames")
        return frame_files, frames_dir
    
    def extract_audio_from_source(self):
        """Extract the ElevenLabs audio from the source video"""
        print("🔊 Extracting ElevenLabs audio...")
        
        audio_output = self.output_dir / "elevenlabs_extracted_audio.wav"
        
        # Extract audio using ffmpeg
        cmd = f'ffmpeg -y -i "{self.source_video}" -vn -acodec pcm_s16le -ar 44100 "{audio_output}"'
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Audio extracted to: {audio_output}")
            return str(audio_output)
        else:
            print(f"⚠️  Audio extraction failed: {result.stderr}")
            return None
    
    def create_final_video(self, frame_files, frames_dir, audio_file):
        """Combine robot frames with ElevenLabs audio"""
        print("🎞️  Creating final video with robot background...")
        
        output_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional_RobotBG.mp4"
        
        # Create frame list file for ffmpeg
        frame_list_file = frames_dir / "frame_list.txt"
        with open(frame_list_file, 'w') as f:
            for frame_file in frame_files:
                f.write(f"file '{frame_file}'\n")
                f.write(f"duration {1/self.fps}\n")
            # Add last frame again for proper duration
            if frame_files:
                f.write(f"file '{frame_files[-1]}'\n")
        
        try:
            # Create video from frames
            if audio_file and os.path.exists(audio_file):
                # With audio
                cmd = [
                    'ffmpeg', '-y',
                    '-f', 'concat',
                    '-safe', '0',
                    '-i', str(frame_list_file),
                    '-i', audio_file,
                    '-c:v', 'libx264',
                    '-c:a', 'aac',
                    '-pix_fmt', 'yuv420p',
                    '-r', str(self.fps),
                    '-shortest',
                    str(output_video)
                ]
            else:
                # Without audio (fallback)
                cmd = [
                    'ffmpeg', '-y',
                    '-f', 'concat',
                    '-safe', '0',
                    '-i', str(frame_list_file),
                    '-c:v', 'libx264',
                    '-pix_fmt', 'yuv420p',
                    '-r', str(self.fps),
                    str(output_video)
                ]
            
            print("🎬 Running ffmpeg...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Video created successfully: {output_video}")
                
                # Clean up frame files
                print("🧹 Cleaning up temporary files...")
                for frame_file in frame_files:
                    try:
                        os.unlink(frame_file)
                    except:
                        pass
                
                # Remove frames directory
                try:
                    frames_dir.rmdir()
                except:
                    pass
                
                return str(output_video)
            else:
                print(f"❌ Video creation failed: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Error creating video: {e}")
            return None
    
    def replace_background(self):
        """Main function to replace video background with animated robots"""
        print("\n🤖 Starting ElevenLabs Robot Background Replacement...")
        print("=" * 70)
        
        # Check if source video exists
        if not os.path.exists(self.source_video):
            print(f"❌ Source video not found: {self.source_video}")
            return None
        
        # Get video information
        video_info = self.get_video_info()
        total_frames = video_info['total_frames']
        
        # Extract audio from source
        audio_file = self.extract_audio_from_source()
        
        # Create robot frames
        frame_files, frames_dir = self.create_robot_frames(total_frames)
        
        # Create final video
        output_video = self.create_final_video(frame_files, frames_dir, audio_file)
        
        if output_video:
            print(f"\n🎉 SUCCESS! ElevenLabs tutorial with robot background created!")
            print(f"📁 Output: {output_video}")
            print("🤖 Features:")
            print("   🎙️  Original ElevenLabs professional narration")
            print("   👁️  Animated blinking robot eyes")
            print("   🎨 Professional C-Cube styling")
            print("   🔊 High-quality audio preserved")
            
            return output_video
        else:
            print("❌ Failed to create video")
            return None

def main():
    """Replace ElevenLabs video background with animated robots"""
    print("🤖 C-CUBE ELEVENLABS ROBOT BACKGROUND REPLACER")
    print("🎬 Adding animated robot background to ElevenLabs tutorial")
    print("=" * 70)
    
    replacer = CCubeElevenLabsRobotReplacer()
    video_path = replacer.replace_background()
    
    if video_path:
        print(f"\n🚀 TRANSFORMATION COMPLETE!")
        print(f"📁 New Video: {video_path}")
        print("✨ Your ElevenLabs tutorial now has animated robots!")

if __name__ == "__main__":
    main()