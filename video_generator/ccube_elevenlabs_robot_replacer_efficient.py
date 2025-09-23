#!/usr/bin/env python3
"""
C-Cube ElevenLabs Robot Background Replacer - Efficient Version
Creates a shorter robot version of the ElevenLabs tutorial
"""

import os
import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess
import json
import random

class CCubeElevenLabsRobotReplacerEfficient:
    """Efficiently replace background with robots"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.width = 1280
        self.height = 720
        self.fps = 15
        
        # Source video with ElevenLabs audio
        self.source_video = "output/CCube_Tutorial_ElevenLabs_Professional.mp4"
        self.robot_bg = "output/tut_agent_Conv_photo.png"
        
        print("🤖 C-Cube ElevenLabs Robot Replacer - Efficient Version")
        print(f"🎥 Source Video: {self.source_video}")
        print(f"🖼️  Robot Background: {self.robot_bg}")
    
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
            robot_img = robot_img.resize((self.width, self.height), Image.Resampling.LANCZOS)
            print(f"✅ Loaded robot background: {robot_img.size}")
            return robot_img
        except Exception as e:
            print(f"⚠️  Warning: Could not load robot image: {e}")
            return Image.new('RGB', (self.width, self.height), (20, 20, 20))
    
    def create_robot_variations(self):
        """Create a few robot frame variations to cycle through"""
        print("🎨 Creating robot frame variations...")
        
        robot_base = self.load_robot_background()
        variations = []
        
        # Create 8 different variations with different blinking patterns
        blink_patterns = [
            (False, False),  # No blink
            (False, False),  # No blink
            (False, False),  # No blink  
            (True, False),   # Robot 1 blinks
            (False, False),  # No blink
            (False, True),   # Robot 2 blinks
            (False, False),  # No blink
            (True, True),    # Both blink (rare)
        ]
        
        for i, (blink1, blink2) in enumerate(blink_patterns):
            frame_img = self.create_eye_blink_mask(robot_base, blink1, blink2)
            final_frame = self.add_elevenlabs_overlay(frame_img, i)
            variations.append(final_frame)
            
            # Save variation
            var_path = self.output_dir / f"robot_variation_{i}.png"
            final_frame.save(var_path, "PNG")
        
        print(f"✅ Created {len(variations)} robot variations")
        return variations
    
    def create_eye_blink_mask(self, robot_base, blink_robot1=False, blink_robot2=False):
        """Create blinking effect by darkening eye areas"""
        img = robot_base.copy()
        draw = ImageDraw.Draw(img)
        
        # Eye positions - you may need to adjust these based on your robot image
        robot1_left_eye = (300, 200, 330, 220)
        robot1_right_eye = (350, 200, 380, 220)
        robot2_left_eye = (800, 200, 830, 220)
        robot2_right_eye = (850, 200, 880, 220)
        
        if blink_robot1:
            draw.ellipse(robot1_left_eye, fill=(0, 0, 0))
            draw.ellipse(robot1_right_eye, fill=(0, 0, 0))
        
        if blink_robot2:
            draw.ellipse(robot2_left_eye, fill=(0, 0, 0))
            draw.ellipse(robot2_right_eye, fill=(0, 0, 0))
        
        return img
    
    def add_elevenlabs_overlay(self, base_img, variation_num=0):
        """Add overlay text indicating ElevenLabs professional narration"""
        img = base_img.copy()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Colors
        primary = (0, 204, 51)
        secondary = (0, 255, 65)
        text_color = (255, 255, 255)
        elevenlabs_color = (138, 43, 226)
        overlay_bg = (0, 0, 0, 180)
        
        # Bottom overlay
        overlay_height = 120
        overlay_y = self.height - overlay_height
        
        overlay = Image.new('RGBA', (self.width, overlay_height), overlay_bg)
        img.paste(overlay, (0, overlay_y), overlay)
        
        # Title
        title = "C-Cube Cold Wallet Tutorial"
        title_y = overlay_y + 15
        title_bbox = draw.textbbox((0, 0), title, font=fonts['title'])
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (self.width - title_width) // 2
        
        draw.text((title_x + 2, title_y + 2), title, fill=(0, 0, 0), font=fonts['title'])
        draw.text((title_x, title_y), title, fill=primary, font=fonts['title'])
        
        # ElevenLabs branding
        elevenlabs_text = "🎙️ Professional AI Narration by ElevenLabs"
        elevenlabs_y = title_y + 55
        elevenlabs_bbox = draw.textbbox((0, 0), elevenlabs_text, font=fonts['body'])
        elevenlabs_width = elevenlabs_bbox[2] - elevenlabs_bbox[0]
        elevenlabs_x = (self.width - elevenlabs_width) // 2
        draw.text((elevenlabs_x, elevenlabs_y), elevenlabs_text, fill=elevenlabs_color, font=fonts['body'])
        
        # C-Cube logo
        logo_text = "C-CUBE"
        draw.text((20, 20), logo_text, fill=primary, font=fonts['body'])
        
        # ElevenLabs indicator
        api_text = "🔊 ElevenLabs AI"
        api_bbox = draw.textbbox((0, 0), api_text, font=fonts['small'])
        api_width = api_bbox[2] - api_bbox[0]
        api_x = self.width - api_width - 20
        draw.text((api_x, 20), api_text, fill=elevenlabs_color, font=fonts['small'])
        
        return img
    
    def create_video_with_ffmpeg(self):
        """Use FFmpeg to directly overlay robot background onto existing video"""
        print("🎬 Creating video with FFmpeg overlay...")
        
        output_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional_RobotBG.mp4"
        
        # Create a simple robot background video
        robot_base = self.load_robot_background()
        
        # Create a base robot frame with overlay
        base_frame = self.add_elevenlabs_overlay(robot_base)
        base_frame_path = self.output_dir / "robot_base_frame.png"
        base_frame.save(base_frame_path, "PNG")
        
        try:
            # Use FFmpeg to create video with robot background and original audio
            cmd = [
                'ffmpeg', '-y',
                '-loop', '1',
                '-i', str(base_frame_path),
                '-i', self.source_video,
                '-c:v', 'libx264',
                '-c:a', 'copy',
                '-map', '0:v',
                '-map', '1:a',
                '-shortest',
                '-pix_fmt', 'yuv420p',
                '-r', '15',
                str(output_video)
            ]
            
            print("🎬 Running FFmpeg...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Video created successfully: {output_video}")
                
                # Clean up temp file
                base_frame_path.unlink()
                
                return str(output_video)
            else:
                print(f"❌ Video creation failed: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Error creating video: {e}")
            return None
    
    def create_animated_video_simple(self):
        """Create a simple animated version with fewer frames"""
        print("🎬 Creating simple animated version...")
        
        output_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional_RobotBG_Animated.mp4"
        
        # Create 30 frames that will loop (2 seconds worth)
        frames_dir = self.output_dir / "simple_robot_frames"
        frames_dir.mkdir(exist_ok=True)
        
        robot_base = self.load_robot_background()
        frame_files = []
        
        for i in range(30):
            # Simple blinking pattern
            blink1 = (i % 15 == 0)  # Robot 1 blinks every 15 frames
            blink2 = (i % 20 == 0)  # Robot 2 blinks every 20 frames
            
            frame_img = self.create_eye_blink_mask(robot_base, blink1, blink2)
            final_frame = self.add_elevenlabs_overlay(frame_img, i)
            
            frame_path = frames_dir / f"frame_{i:03d}.png"
            final_frame.save(frame_path, "PNG")
            frame_files.append(str(frame_path))
        
        # Create frame list for ffmpeg
        frame_list_file = frames_dir / "frame_list.txt"
        with open(frame_list_file, 'w') as f:
            # Loop the 30 frames for the duration of the audio
            for _ in range(133):  # 133 loops * 30 frames = ~265 seconds at 15fps
                for frame_file in frame_files:
                    f.write(f"file '{frame_file}'\n")
                    f.write(f"duration {1/15}\n")
            # Add last frame
            f.write(f"file '{frame_files[-1]}'\n")
        
        try:
            # Create video from frames with original audio
            cmd = [
                'ffmpeg', '-y',
                '-f', 'concat',
                '-safe', '0',
                '-i', str(frame_list_file),
                '-i', self.source_video,
                '-c:v', 'libx264',
                '-c:a', 'copy',
                '-map', '0:v',
                '-map', '1:a',
                '-shortest',
                '-pix_fmt', 'yuv420p',
                str(output_video)
            ]
            
            print("🎬 Creating animated video...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Animated video created: {output_video}")
                
                # Clean up
                for frame_file in frame_files:
                    os.unlink(frame_file)
                frames_dir.rmdir()
                
                return str(output_video)
            else:
                print(f"❌ Animated video creation failed: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Error creating animated video: {e}")
            return None
    
    def replace_background(self):
        """Main function to replace video background"""
        print("\n🤖 Starting ElevenLabs Robot Background Replacement...")
        print("=" * 70)
        
        if not os.path.exists(self.source_video):
            print(f"❌ Source video not found: {self.source_video}")
            return None
        
        # Try animated version first
        print("🎯 Creating animated robot version...")
        animated_video = self.create_animated_video_simple()
        
        if animated_video:
            print(f"\n🎉 SUCCESS! ElevenLabs tutorial with animated robots!")
            print(f"📁 Output: {animated_video}")
            print("🤖 Features:")
            print("   🎙️  Original ElevenLabs professional narration")
            print("   👁️  Animated blinking robot eyes")
            print("   🎨 Professional C-Cube styling")
            print("   🔊 High-quality audio preserved")
            
            return animated_video
        else:
            # Fallback to simple static version
            print("🎯 Creating static robot version...")
            static_video = self.create_video_with_ffmpeg()
            return static_video

def main():
    """Replace ElevenLabs video background with animated robots"""
    print("🤖 C-CUBE ELEVENLABS ROBOT BACKGROUND REPLACER - EFFICIENT")
    print("🎬 Adding animated robot background to ElevenLabs tutorial")
    print("=" * 70)
    
    replacer = CCubeElevenLabsRobotReplacerEfficient()
    video_path = replacer.replace_background()
    
    if video_path:
        print(f"\n🚀 TRANSFORMATION COMPLETE!")
        print(f"📁 New Video: {video_path}")
        print("✨ Your ElevenLabs tutorial now has animated robots!")

if __name__ == "__main__":
    main()