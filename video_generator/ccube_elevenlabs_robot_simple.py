#!/usr/bin/env python3
"""
C-Cube ElevenLabs Robot Background Replacer - Simple Version
Creates a robot background version with ElevenLabs audio
"""

import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

class CCubeElevenLabsRobotSimple:
    """Simple robot background replacement"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.width = 1280
        self.height = 720
        
        # Files
        self.source_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional.mp4"
        self.robot_bg = self.output_dir / "tut_agent_Conv_photo2.png"
        
        print("🤖 C-Cube ElevenLabs Robot Replacer - Simple Version")
    
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
    
    def get_tutorial_transcript(self):
        """Get the tutorial transcript text"""
        return """Welcome to C-Cube Cold Wallet, your secure offline cryptocurrency storage solution. This tutorial will guide you through creating your first wallet and understanding the key security principles that keep your cryptocurrency safe. C-Cube is designed with security as the top priority. Your private keys are encrypted and stored only on your device, never transmitted online or stored on remote servers. Key Features: Complete offline operation for maximum security, Military-grade AES-256 encryption, Support for multiple blockchain networks, Open-source code for transparency and trust, User-friendly interface for ease of use. Before we begin, it's important to understand that cryptocurrency security is your responsibility. C-Cube provides the tools, but you must follow security best practices. Always backup your recovery phrases in a secure location. These phrases are the only way to recover your wallet if your device is lost or damaged. Never share your private keys or recovery phrases with anyone. Legitimate services will never ask for this information. Use strong, unique passwords and enable all available security features. In the next steps, we'll walk through creating your first wallet, setting up security measures, and making your first transaction. Remember to start with small amounts while you learn the system, then gradually increase as you become more comfortable. Thank you for choosing C-Cube for your cryptocurrency security needs."""

    def wrap_text(self, text, max_width, font, draw):
        """Wrap text to fit within max_width"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = draw.textbbox((0, 0), test_line, font=font)
            line_width = bbox[2] - bbox[0]
            
            if line_width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)  # Single word is too long, add anyway
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines

    def create_robot_frame(self):
        """Create a single robot frame with transcript overlay"""
        try:
            # Load robot background
            robot_img = Image.open(self.robot_bg)
            robot_img = robot_img.resize((self.width, self.height), Image.Resampling.LANCZOS)
            print(f"✅ Loaded robot background: {robot_img.size}")
        except Exception as e:
            print(f"⚠️  Using default background: {e}")
            robot_img = Image.new('RGB', (self.width, self.height), (20, 20, 20))
        
        # Add overlay
        draw = ImageDraw.Draw(robot_img)
        fonts = self.get_fonts()
        
        # Colors
        primary = (0, 204, 51)
        text_color = (255, 255, 255)
        overlay_bg = (0, 0, 0, 180)
        
        # Create larger overlay for transcript
        overlay_height = 200
        overlay_y = self.height - overlay_height
        
        # Create semi-transparent overlay
        overlay = Image.new('RGBA', (self.width, overlay_height), overlay_bg)
        robot_img = robot_img.convert('RGBA')
        robot_img.paste(overlay, (0, overlay_y), overlay)
        robot_img = robot_img.convert('RGB')
        
        # Re-create draw object for RGB image
        draw = ImageDraw.Draw(robot_img)
        
        # Get transcript and wrap text
        transcript = self.get_tutorial_transcript()
        max_text_width = self.width - 40  # 20px margin on each side
        
        # Wrap text to fit the overlay area
        wrapped_lines = self.wrap_text(transcript, max_text_width, fonts['small'], draw)
        
        # Calculate how many lines can fit in the overlay
        line_height = 18
        max_lines = (overlay_height - 40) // line_height  # 20px margin top/bottom
        
        # Show only the first portion of the transcript that fits
        display_lines = wrapped_lines[:max_lines]
        
        # Draw transcript text
        text_y = overlay_y + 20
        for line in display_lines:
            draw.text((20, text_y), line, fill=text_color, font=fonts['small'])
            text_y += line_height
        
        # C-Cube logo (smaller, top left)
        logo_text = "C-CUBE"
        draw.text((20, 20), logo_text, fill=primary, font=fonts['body'])
        
        # Add a small indicator that this is AI narrated
        ai_text = "🎙️ AI Narration"
        ai_bbox = draw.textbbox((0, 0), ai_text, font=fonts['small'])
        ai_width = ai_bbox[2] - ai_bbox[0]
        ai_x = self.width - ai_width - 20
        draw.text((ai_x, 20), ai_text, fill=text_color, font=fonts['small'])
        
        return robot_img
    
    def create_robot_video(self):
        """Create robot background video using FFmpeg"""
        print("🎬 Creating robot background video...")
        
        # Create the robot frame
        robot_frame = self.create_robot_frame()
        frame_path = self.output_dir / "robot_frame.png"
        robot_frame.save(frame_path, "PNG")
        print(f"✅ Saved robot frame: {frame_path}")
        
        # Output video
        output_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional_RobotBG.mp4"
        
        try:
            # Use FFmpeg to create video with robot background and original audio
            cmd = [
                'ffmpeg', '-y',
                '-loop', '1',
                '-i', str(frame_path),
                '-i', str(self.source_video),
                '-c:v', 'libx264',
                '-c:a', 'copy',
                '-map', '0:v',
                '-map', '1:a',
                '-shortest',
                '-pix_fmt', 'yuv420p',
                '-preset', 'fast',
                str(output_video)
            ]
            
            print("🎬 Running FFmpeg...")
            print(f"Command: {' '.join(cmd)}")
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Video created successfully!")
                print(f"📁 Output: {output_video}")
                
                # Clean up temp file
                frame_path.unlink()
                
                # Get file size
                file_size = output_video.stat().st_size
                print(f"📊 File size: {file_size / (1024*1024):.1f} MB")
                
                return str(output_video)
            else:
                print(f"❌ FFmpeg failed:")
                print(f"STDOUT: {result.stdout}")
                print(f"STDERR: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Error creating video: {e}")
            return None
    
    def replace_background(self):
        """Main function to replace video background"""
        print("\n🤖 Starting Simple Robot Background Replacement...")
        print("=" * 70)
        
        if not self.source_video.exists():
            print(f"❌ Source video not found: {self.source_video}")
            return None
        
        video_path = self.create_robot_video()
        
        if video_path:
            print(f"\n🎉 SUCCESS! ElevenLabs tutorial with robot background!")
            print(f"📁 Output: {video_path}")
            print("🤖 Features:")
            print("   🎙️  Original ElevenLabs professional narration")
            print("   👁️  Robot background image")
            print("   🎨 Professional C-Cube styling")
            print("   🔊 High-quality audio preserved")
            
            return video_path
        else:
            print("❌ Failed to create robot background video")
            return None

def main():
    """Replace ElevenLabs video background with robot image"""
    print("🤖 C-CUBE ELEVENLABS ROBOT BACKGROUND REPLACER")
    print("🎬 Adding robot background to ElevenLabs tutorial")
    print("=" * 70)
    
    replacer = CCubeElevenLabsRobotSimple()
    video_path = replacer.replace_background()
    
    if video_path:
        print(f"\n🚀 TRANSFORMATION COMPLETE!")
        print(f"📁 New Video: {video_path}")
        print("✨ Your ElevenLabs tutorial now has a robot background!")

if __name__ == "__main__":
    main()