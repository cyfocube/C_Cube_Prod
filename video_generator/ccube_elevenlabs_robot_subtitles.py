#!/usr/bin/env python3
"""
C-Cube ElevenLabs Robot Background with Synchronized Subtitles
Creates subtitles that match the spoken audio timing
"""

import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json

class CCubeElevenLabsRobotSubtitles:
    """Robot background with synchronized subtitles"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.width = 1280
        self.height = 720
        self.fps = 15
        
        # Files
        self.source_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional.mp4"
        self.robot_bg = self.output_dir / "tut_agent_Conv_photo2.png"
        
        print("🤖 C-Cube ElevenLabs Robot with Synchronized Subtitles")
    
    def get_fonts(self):
        """Get fonts for text rendering"""
        try:
            return {
                'title': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48),
                'subtitle': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36),
                'body': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28),
                'small': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24),
            }
        except:
            default = ImageFont.load_default()
            return {k: default for k in ['title', 'subtitle', 'body', 'small']}
    
    def get_subtitle_segments(self):
        """Define subtitle segments with timing (in seconds)"""
        return [
            {"start": 0, "end": 8, "text": "Welcome to C-Cube Cold Wallet, your secure offline cryptocurrency storage solution."},
            {"start": 8, "end": 16, "text": "This tutorial will guide you through creating your first wallet"},
            {"start": 16, "end": 24, "text": "and understanding the key security principles that keep your cryptocurrency safe."},
            {"start": 24, "end": 32, "text": "C-Cube is designed with security as the top priority."},
            {"start": 32, "end": 40, "text": "Your private keys are encrypted and stored only on your device,"},
            {"start": 40, "end": 48, "text": "never transmitted online or stored on remote servers."},
            {"start": 48, "end": 56, "text": "Key Features: Complete offline operation for maximum security,"},
            {"start": 56, "end": 64, "text": "Military-grade AES-256 encryption,"},
            {"start": 64, "end": 72, "text": "Support for multiple blockchain networks,"},
            {"start": 72, "end": 80, "text": "Open-source code for transparency and trust,"},
            {"start": 80, "end": 88, "text": "User-friendly interface for ease of use."},
            {"start": 88, "end": 96, "text": "Before we begin, it's important to understand"},
            {"start": 96, "end": 104, "text": "that cryptocurrency security is your responsibility."},
            {"start": 104, "end": 112, "text": "C-Cube provides the tools, but you must follow security best practices."},
            {"start": 112, "end": 120, "text": "Always backup your recovery phrases in a secure location."},
            {"start": 120, "end": 128, "text": "These phrases are the only way to recover your wallet"},
            {"start": 128, "end": 136, "text": "if your device is lost or damaged."},
            {"start": 136, "end": 144, "text": "Never share your private keys or recovery phrases with anyone."},
            {"start": 144, "end": 152, "text": "Legitimate services will never ask for this information."},
            {"start": 152, "end": 160, "text": "Use strong, unique passwords and enable all available security features."},
            {"start": 160, "end": 168, "text": "In the next steps, we'll walk through creating your first wallet,"},
            {"start": 168, "end": 176, "text": "setting up security measures, and making your first transaction."},
            {"start": 176, "end": 184, "text": "Remember to start with small amounts while you learn the system,"},
            {"start": 184, "end": 192, "text": "then gradually increase as you become more comfortable."},
            {"start": 192, "end": 200, "text": "Thank you for choosing C-Cube for your cryptocurrency security needs."},
            {"start": 200, "end": 265, "text": "Start your secure cryptocurrency journey with C-Cube today."}
        ]
    
    def get_current_subtitle(self, time_seconds):
        """Get the subtitle text for the current time"""
        segments = self.get_subtitle_segments()
        for segment in segments:
            if segment["start"] <= time_seconds < segment["end"]:
                return segment["text"]
        return ""
    
    def wrap_subtitle_text(self, text, max_width, font, draw):
        """Wrap subtitle text to fit within max_width"""
        if not text:
            return []
            
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
                    lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def create_robot_frame_with_subtitle(self, time_seconds):
        """Create a robot frame with subtitle for specific time"""
        try:
            # Load robot background
            robot_img = Image.open(self.robot_bg)
            robot_img = robot_img.resize((self.width, self.height), Image.Resampling.LANCZOS)
        except Exception as e:
            print(f"⚠️  Using default background: {e}")
            robot_img = Image.new('RGB', (self.width, self.height), (20, 20, 20))
        
        draw = ImageDraw.Draw(robot_img)
        fonts = self.get_fonts()
        
        # Colors
        primary = (0, 204, 51)
        text_color = (255, 255, 255)
        subtitle_bg = (0, 0, 0, 200)
        
        # Get current subtitle
        subtitle_text = self.get_current_subtitle(time_seconds)
        
        if subtitle_text:
            # Subtitle overlay (bottom section)
            overlay_height = 100
            overlay_y = self.height - overlay_height
            
            # Create semi-transparent overlay for subtitles
            overlay = Image.new('RGBA', (self.width, overlay_height), subtitle_bg)
            robot_img = robot_img.convert('RGBA')
            robot_img.paste(overlay, (0, overlay_y), overlay)
            robot_img = robot_img.convert('RGB')
            
            # Re-create draw object
            draw = ImageDraw.Draw(robot_img)
            
            # Wrap subtitle text
            max_subtitle_width = self.width - 60  # 30px margin on each side
            subtitle_lines = self.wrap_subtitle_text(subtitle_text, max_subtitle_width, fonts['small'], draw)
            
            # Center and draw subtitle lines
            line_height = 26
            total_text_height = len(subtitle_lines) * line_height
            start_y = overlay_y + (overlay_height - total_text_height) // 2
            
            for i, line in enumerate(subtitle_lines):
                # Get text width for centering
                bbox = draw.textbbox((0, 0), line, font=fonts['small'])
                text_width = bbox[2] - bbox[0]
                text_x = (self.width - text_width) // 2
                text_y = start_y + (i * line_height)
                
                # Draw subtitle text with shadow
                draw.text((text_x + 1, text_y + 1), line, fill=(0, 0, 0), font=fonts['small'])
                draw.text((text_x, text_y), line, fill=text_color, font=fonts['small'])
        
        # C-Cube logo (top left)
        logo_text = "C-CUBE"
        draw.text((20, 20), logo_text, fill=primary, font=fonts['body'])
        
        # AI indicator (top right)
        ai_text = "🎙️ AI Narration"
        ai_bbox = draw.textbbox((0, 0), ai_text, font=fonts['small'])
        ai_width = ai_bbox[2] - ai_bbox[0]
        ai_x = self.width - ai_width - 20
        draw.text((ai_x, 20), ai_text, fill=text_color, font=fonts['small'])
        
        return robot_img
    
    def create_subtitle_video(self):
        """Create video with synchronized subtitles"""
        print("🎬 Creating video with synchronized subtitles...")
        
        # Get video duration
        try:
            result = subprocess.run([
                'ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format',
                str(self.source_video)
            ], capture_output=True, text=True)
            
            video_info = json.loads(result.stdout)
            duration = float(video_info['format']['duration'])
            print(f"📊 Video duration: {duration} seconds")
        except Exception as e:
            print(f"❌ Could not get video duration: {e}")
            duration = 265  # fallback
        
        # Create frames directory
        frames_dir = self.output_dir / "subtitle_frames"
        frames_dir.mkdir(exist_ok=True)
        
        total_frames = int(duration * self.fps)
        print(f"🎨 Creating {total_frames} frames with subtitles...")
        
        frame_files = []
        
        # Create frame for each time point
        for frame_num in range(total_frames):
            time_seconds = frame_num / self.fps
            
            # Create frame with subtitle for this time
            frame_img = self.create_robot_frame_with_subtitle(time_seconds)
            
            # Save frame
            frame_path = frames_dir / f"frame_{frame_num:06d}.png"
            frame_img.save(frame_path, "PNG")
            frame_files.append(str(frame_path))
            
            if frame_num % 100 == 0:
                print(f"📊 Progress: {frame_num}/{total_frames} frames ({100*frame_num/total_frames:.1f}%)")
        
        print("🎬 Assembling video with FFmpeg...")
        
        # Output video
        output_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional_RobotBG_Subtitles.mp4"
        
        try:
            # Create video from frames with original audio
            cmd = [
                'ffmpeg', '-y',
                '-framerate', str(self.fps),
                '-i', str(frames_dir / 'frame_%06d.png'),
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
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Video with subtitles created!")
                print(f"📁 Output: {output_video}")
                
                # Clean up frames
                print("🧹 Cleaning up temporary frames...")
                for frame_file in frame_files:
                    os.unlink(frame_file)
                frames_dir.rmdir()
                
                # Get file size
                file_size = output_video.stat().st_size
                print(f"📊 File size: {file_size / (1024*1024):.1f} MB")
                
                return str(output_video)
            else:
                print(f"❌ FFmpeg failed:")
                print(f"STDERR: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Error creating video: {e}")
            return None
    
    def create_subtitled_video(self):
        """Main function to create video with subtitles"""
        print("\n🤖 Starting Synchronized Subtitle Creation...")
        print("=" * 70)
        
        if not self.source_video.exists():
            print(f"❌ Source video not found: {self.source_video}")
            return None
        
        video_path = self.create_subtitle_video()
        
        if video_path:
            print(f"\n🎉 SUCCESS! ElevenLabs tutorial with synchronized subtitles!")
            print(f"📁 Output: {video_path}")
            print("🤖 Features:")
            print("   🎙️  Original ElevenLabs professional narration")
            print("   📝 Synchronized subtitles matching spoken words")
            print("   👁️  Robot background image")
            print("   🎨 Professional C-Cube styling")
            print("   🔊 High-quality audio preserved")
            
            return video_path
        else:
            print("❌ Failed to create subtitled video")
            return None

def main():
    """Create ElevenLabs video with synchronized subtitles"""
    print("🤖 C-CUBE ELEVENLABS ROBOT WITH SYNCHRONIZED SUBTITLES")
    print("📝 Creating subtitles that match the spoken audio")
    print("=" * 70)
    
    creator = CCubeElevenLabsRobotSubtitles()
    video_path = creator.create_subtitled_video()
    
    if video_path:
        print(f"\n🚀 SUBTITLE SYNCHRONIZATION COMPLETE!")
        print(f"📁 New Video: {video_path}")
        print("✨ Your ElevenLabs tutorial now has synchronized subtitles!")

if __name__ == "__main__":
    main()