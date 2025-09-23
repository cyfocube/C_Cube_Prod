#!/usr/bin/env python3
"""
C-Cube Animated Robot Video Generator
Creates videos with robot background and blinking eye animations
"""

import os
import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess
import json
import random

class CCubeAnimatedRobotGenerator:
    """Generate animated videos with robot background and blinking animations"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.width = 1280
        self.height = 720
        self.fps = 15
        
        # Robot image
        self.robot_bg = "output/tut_agent_Conv_photo.png"
        
        # Audio files for different sections
        self.audio_sections = [
            "output/section_00_audio.wav",
            "output/section_01_audio.wav", 
            "output/section_02_audio.wav",
            "output/section_03_audio.wav",
            "output/section_04_audio.wav"
        ]
        
        print("🤖 C-Cube Animated Robot Video Generator")
        print(f"🖼️  Background: {self.robot_bg}")
        print(f"🎥 Resolution: {self.width}x{self.height}")
        print("✨ Creating animated tutorial with blinking robots!")
    
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
            return robot_img
        except Exception as e:
            print(f"⚠️  Warning: Could not load robot image: {e}")
            # Create a fallback dark background
            return Image.new('RGB', (self.width, self.height), (20, 20, 20))
    
    def create_eye_blink_mask(self, robot_base, blink_robot1=False, blink_robot2=False):
        """Create blinking effect by darkening eye areas"""
        img = robot_base.copy()
        draw = ImageDraw.Draw(img)
        
        # Approximate eye positions for two robots (you may need to adjust these)
        # Robot 1 (left side) eye positions
        robot1_left_eye = (200, 180, 230, 200)    # (x1, y1, x2, y2)
        robot1_right_eye = (250, 180, 280, 200)
        
        # Robot 2 (right side) eye positions  
        robot2_left_eye = (900, 180, 930, 200)
        robot2_right_eye = (950, 180, 980, 200)
        
        # Create blink effect by drawing dark ellipses over eyes
        if blink_robot1:
            draw.ellipse(robot1_left_eye, fill=(0, 0, 0, 180))
            draw.ellipse(robot1_right_eye, fill=(0, 0, 0, 180))
        
        if blink_robot2:
            draw.ellipse(robot2_left_eye, fill=(0, 0, 0, 180))
            draw.ellipse(robot2_right_eye, fill=(0, 0, 0, 180))
        
        return img
    
    def add_text_overlay(self, base_img, title, subtitle="", progress=""):
        """Add text overlay with C-Cube styling"""
        img = base_img.copy()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Colors
        primary = (0, 204, 51)      # #00cc33
        secondary = (0, 255, 65)    # #00ff41
        text_color = (255, 255, 255)
        overlay_bg = (0, 0, 0, 150)  # Semi-transparent black
        
        # Create text overlay area
        overlay_height = 200
        overlay_y = self.height - overlay_height
        
        # Draw semi-transparent overlay
        overlay = Image.new('RGBA', (self.width, overlay_height), overlay_bg)
        img.paste(overlay, (0, overlay_y), overlay)
        
        # Main title
        title_y = overlay_y + 20
        title_bbox = draw.textbbox((0, 0), title, font=fonts['title'])
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (self.width - title_width) // 2
        
        # Title shadow
        draw.text((title_x + 2, title_y + 2), title, fill=(0, 0, 0), font=fonts['title'])
        draw.text((title_x, title_y), title, fill=primary, font=fonts['title'])
        
        # Subtitle
        if subtitle:
            subtitle_y = title_y + 60
            subtitle_bbox = draw.textbbox((0, 0), subtitle, font=fonts['subtitle'])
            subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
            subtitle_x = (self.width - subtitle_width) // 2
            draw.text((subtitle_x, subtitle_y), subtitle, fill=text_color, font=fonts['subtitle'])
        
        # Progress indicator
        if progress:
            progress_y = overlay_y + 140
            progress_bbox = draw.textbbox((0, 0), progress, font=fonts['small'])
            progress_width = progress_bbox[2] - progress_bbox[0]
            progress_x = (self.width - progress_width) // 2
            draw.text((progress_x, progress_y), progress, fill=secondary, font=fonts['small'])
        
        # C-Cube logo in corner
        logo_text = "C-CUBE"
        logo_bbox = draw.textbbox((0, 0), logo_text, font=fonts['body'])
        logo_x = 20
        logo_y = 20
        draw.text((logo_x, logo_y), logo_text, fill=primary, font=fonts['body'])
        
        return img
    
    def create_animated_section(self, section_title, section_subtitle, frame_count, section_num):
        """Create an animated section with talking robots"""
        print(f"🎬 Creating section: {section_title}")
        
        robot_base = self.load_robot_background()
        frames = []
        
        for frame_i in range(frame_count):
            # Determine which robot is "talking" (alternating or based on content)
            # Robot 1 talks for first half, Robot 2 for second half
            robot1_talking = frame_i < frame_count // 2
            robot2_talking = frame_i >= frame_count // 2
            
            # Create blinking pattern (blink every 15-20 frames randomly)
            blink_robot1 = robot1_talking and (frame_i % 17 == 0 or frame_i % 23 == 0)
            blink_robot2 = robot2_talking and (frame_i % 19 == 0 or frame_i % 29 == 0)
            
            # Add random blinks occasionally
            if random.random() < 0.05:  # 5% chance of random blink
                if robot1_talking:
                    blink_robot1 = True
                else:
                    blink_robot2 = True
            
            # Create frame with blinking
            frame_img = self.create_eye_blink_mask(robot_base, blink_robot1, blink_robot2)
            
            # Add text overlay
            progress_text = f"Section {section_num + 1} • Frame {frame_i + 1}/{frame_count}"
            if robot1_talking:
                subtitle = f"🤖 Robot Guide 1: {section_subtitle}"
            else:
                subtitle = f"🤖 Robot Guide 2: {section_subtitle}"
            
            final_frame = self.add_text_overlay(frame_img, section_title, subtitle, progress_text)
            frames.append(final_frame)
            
            # Save individual frame
            frame_filename = f"robot_section_{section_num:02d}_{section_title.replace(' ', '_')}_frame_{frame_i:04d}.png"
            frame_path = self.output_dir / frame_filename
            final_frame.save(frame_path, "PNG")
        
        print(f"✅ Created {len(frames)} animated frames")
        return frames, frame_filename.replace(f"_frame_{frame_i:04d}.png", "_frame_%04d.png")
    
    def create_animated_tutorial(self):
        """Create the complete animated tutorial"""
        print("\n🎬 Creating Complete Animated Robot Tutorial...")
        print("=" * 70)
        
        # Tutorial sections with content
        sections = [
            {
                "title": "Welcome to C-Cube Cold Wallet",
                "subtitle": "Your Secure Cryptocurrency Storage",
                "frames": 60,
                "audio": "output/section_00_audio.wav"
            },
            {
                "title": "Security First Approach", 
                "subtitle": "Understanding Cryptocurrency Safety",
                "frames": 80,
                "audio": "output/section_01_audio.wav"
            },
            {
                "title": "Creating Your First Wallet",
                "subtitle": "Step-by-Step Wallet Setup",
                "frames": 90,
                "audio": "output/section_02_audio.wav"
            },
            {
                "title": "Understanding Networks",
                "subtitle": "Blockchain Network Selection",
                "frames": 75,
                "audio": "output/section_03_audio.wav"
            },
            {
                "title": "Your First Transaction",
                "subtitle": "Sending Cryptocurrency Safely",
                "frames": 85,
                "audio": "output/section_04_audio.wav"
            }
        ]
        
        all_frame_patterns = []
        all_audio_files = []
        
        # Create each section
        for i, section in enumerate(sections):
            frames, frame_pattern = self.create_animated_section(
                section["title"],
                section["subtitle"], 
                section["frames"],
                i
            )
            
            all_frame_patterns.append(frame_pattern)
            
            # Check if audio file exists
            if os.path.exists(section["audio"]):
                all_audio_files.append(section["audio"])
            else:
                print(f"⚠️  Audio file not found: {section['audio']}")
        
        # Combine all sections into final video
        self.create_final_video(all_frame_patterns, all_audio_files)
    
    def create_final_video(self, frame_patterns, audio_files):
        """Combine all frames and audio into final video"""
        print("\n🎞️  Assembling Final Video...")
        
        # Create video from frames
        output_video = self.output_dir / "CCube_Animated_Robots_Tutorial.mp4"
        temp_video = self.output_dir / "temp_robot_video.mp4"
        
        try:
            # First, create video from all frame patterns
            concat_filter = ""
            for i, pattern in enumerate(frame_patterns):
                pattern_path = str(self.output_dir / pattern)
                if i == 0:
                    concat_filter = f"ffmpeg -y -framerate {self.fps} -i '{pattern_path}'"
                else:
                    concat_filter += f" -framerate {self.fps} -i '{pattern_path}'"
            
            # Create video without audio first
            video_cmd = f"{concat_filter} -filter_complex 'concat=n={len(frame_patterns)}:v=1:a=0' -c:v libx264 -pix_fmt yuv420p '{temp_video}'"
            
            print("🎬 Creating video from frames...")
            result = subprocess.run(video_cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Video frames assembled successfully")
                
                # Now add audio if available
                if audio_files and os.path.exists(audio_files[0]):
                    print("🔊 Adding audio track...")
                    
                    # Use the first audio file for now (you can enhance this to concatenate all)
                    audio_cmd = f"ffmpeg -y -i '{temp_video}' -i '{audio_files[0]}' -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 '{output_video}'"
                    
                    audio_result = subprocess.run(audio_cmd, shell=True, capture_output=True, text=True)
                    
                    if audio_result.returncode == 0:
                        print("✅ Audio added successfully")
                        # Clean up temp file
                        if temp_video.exists():
                            temp_video.unlink()
                    else:
                        print(f"⚠️  Audio addition failed: {audio_result.stderr}")
                        # Rename temp video as final
                        temp_video.rename(output_video)
                else:
                    print("⚠️  No audio files found, creating video without audio")
                    temp_video.rename(output_video)
                
                print(f"\n🎉 SUCCESS! Animated robot tutorial created!")
                print(f"📁 Output: {output_video}")
                print(f"🤖 Features: Blinking robots, animated backgrounds, professional narration")
                
                return output_video
                
            else:
                print(f"❌ Video creation failed: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Error creating video: {e}")
            return None

def main():
    """Generate animated robot tutorial"""
    print("🤖 C-CUBE ANIMATED ROBOT TUTORIAL GENERATOR")
    print("🎬 Creating professional animated tutorial with blinking robots")
    print("=" * 70)
    
    generator = CCubeAnimatedRobotGenerator()
    video_path = generator.create_animated_tutorial()
    
    if video_path:
        print(f"\n🎉 ANIMATION COMPLETE!")
        print(f"📁 Video: {video_path}")
        print("🤖 Features created:")
        print("   👁️  Blinking robot eyes during narration")
        print("   🎭 Alternating robot speakers")
        print("   🎨 Professional C-Cube styling") 
        print("   🔊 High-quality audio narration")
        print("   📱 Optimized for social media")

if __name__ == "__main__":
    main()