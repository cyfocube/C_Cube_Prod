#!/usr/bin/env python3
"""
C-Cube ElevenLabs Robot Background with FFmpeg Subtitle Filter
Uses FFmpeg's subtitle filter for efficient synchronized subtitles
"""

import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

class CCubeElevenLabsRobotSubtitlesFFmpeg:
    """Robot background with FFmpeg subtitle filter"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.width = 1280
        self.height = 720
        
        # Files
        self.source_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional.mp4"
        self.robot_bg = self.output_dir / "tut_agent_Conv_photo2.png"
        
        print("🤖 C-Cube ElevenLabs Robot with FFmpeg Subtitles")
    
    def create_srt_file(self):
        """Create SRT subtitle file with better timing to match audio"""
        subtitle_segments = [
            {"start": "00:00:01,000", "end": "00:00:05,500", "text": "Welcome to C-Cube Cold Wallet"},
            {"start": "00:00:05,500", "end": "00:00:09,000", "text": "your secure offline cryptocurrency storage solution"},
            {"start": "00:00:10,000", "end": "00:00:14,000", "text": "This tutorial will guide you through"},
            {"start": "00:00:14,000", "end": "00:00:17,500", "text": "creating your first wallet"},
            {"start": "00:00:18,000", "end": "00:00:22,000", "text": "and understanding the key security principles"},
            {"start": "00:00:22,000", "end": "00:00:25,500", "text": "that keep your cryptocurrency safe"},
            {"start": "00:00:26,500", "end": "00:00:30,000", "text": "C-Cube is designed with security"},
            {"start": "00:00:30,000", "end": "00:00:32,500", "text": "as the top priority"},
            {"start": "00:00:33,500", "end": "00:00:37,000", "text": "Your private keys are encrypted"},
            {"start": "00:00:37,000", "end": "00:00:40,000", "text": "and stored only on your device"},
            {"start": "00:00:41,000", "end": "00:00:44,000", "text": "never transmitted online"},
            {"start": "00:00:44,000", "end": "00:00:47,500", "text": "or stored on remote servers"},
            {"start": "00:00:48,500", "end": "00:00:51,000", "text": "Key Features:"},
            {"start": "00:00:51,000", "end": "00:00:55,000", "text": "Complete offline operation for maximum security"},
            {"start": "00:00:56,000", "end": "00:00:59,500", "text": "Military-grade AES-256 encryption"},
            {"start": "00:01:00,500", "end": "00:01:04,000", "text": "Support for multiple blockchain networks"},
            {"start": "00:01:05,000", "end": "00:01:09,000", "text": "Open-source code for transparency and trust"},
            {"start": "00:01:10,000", "end": "00:01:13,500", "text": "User-friendly interface for ease of use"},
            {"start": "00:01:15,000", "end": "00:01:18,000", "text": "Before we begin"},
            {"start": "00:01:18,000", "end": "00:01:21,500", "text": "it's important to understand"},
            {"start": "00:01:21,500", "end": "00:01:25,500", "text": "that cryptocurrency security is your responsibility"},
            {"start": "00:01:26,500", "end": "00:01:29,500", "text": "C-Cube provides the tools"},
            {"start": "00:01:29,500", "end": "00:01:33,000", "text": "but you must follow security best practices"},
            {"start": "00:01:34,000", "end": "00:01:37,500", "text": "Always backup your recovery phrases"},
            {"start": "00:01:37,500", "end": "00:01:40,500", "text": "in a secure location"},
            {"start": "00:01:41,500", "end": "00:01:44,500", "text": "These phrases are the only way"},
            {"start": "00:01:44,500", "end": "00:01:47,000", "text": "to recover your wallet"},
            {"start": "00:01:47,500", "end": "00:01:50,500", "text": "if your device is lost or damaged"},
            {"start": "00:01:51,500", "end": "00:01:54,500", "text": "Never share your private keys"},
            {"start": "00:01:54,500", "end": "00:01:57,500", "text": "or recovery phrases with anyone"},
            {"start": "00:01:58,500", "end": "00:02:01,500", "text": "Legitimate services will never ask"},
            {"start": "00:02:01,500", "end": "00:02:04,000", "text": "for this information"},
            {"start": "00:02:05,000", "end": "00:02:08,000", "text": "Use strong, unique passwords"},
            {"start": "00:02:08,000", "end": "00:02:11,500", "text": "and enable all available security features"},
            {"start": "00:02:12,500", "end": "00:02:15,500", "text": "In the next steps"},
            {"start": "00:02:15,500", "end": "00:02:18,500", "text": "we'll walk through creating your first wallet"},
            {"start": "00:02:19,000", "end": "00:02:22,000", "text": "setting up security measures"},
            {"start": "00:02:22,000", "end": "00:02:25,000", "text": "and making your first transaction"},
            {"start": "00:02:26,000", "end": "00:02:29,000", "text": "Remember to start with small amounts"},
            {"start": "00:02:29,000", "end": "00:02:32,000", "text": "while you learn the system"},
            {"start": "00:02:33,000", "end": "00:02:36,000", "text": "then gradually increase"},
            {"start": "00:02:36,000", "end": "00:02:39,000", "text": "as you become more comfortable"},
            {"start": "00:02:40,000", "end": "00:02:43,000", "text": "Thank you for choosing C-Cube"},
            {"start": "00:02:43,000", "end": "00:02:46,500", "text": "for your cryptocurrency security needs"},
            {"start": "00:02:47,500", "end": "00:02:51,000", "text": "Start your secure cryptocurrency journey"},
            {"start": "00:02:51,000", "end": "00:02:54,000", "text": "with C-Cube today"}
        ]
        
        srt_path = self.output_dir / "tutorial_subtitles.srt"
        
        with open(srt_path, 'w', encoding='utf-8') as f:
            for i, segment in enumerate(subtitle_segments, 1):
                f.write(f"{i}\n")
                f.write(f"{segment['start']} --> {segment['end']}\n")
                f.write(f"{segment['text']}\n\n")
        
        print(f"✅ Created subtitle file: {srt_path}")
        return str(srt_path)
    
    def create_robot_background_image(self):
        """Create the robot background with minimal overlay"""
        try:
            # Load robot background
            robot_img = Image.open(self.robot_bg)
            robot_img = robot_img.resize((self.width, self.height), Image.Resampling.LANCZOS)
            print(f"✅ Loaded robot background: {robot_img.size}")
        except Exception as e:
            print(f"⚠️  Using default background: {e}")
            robot_img = Image.new('RGB', (self.width, self.height), (20, 20, 20))
        
        draw = ImageDraw.Draw(robot_img)
        
        # Get fonts
        try:
            body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
            small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        except:
            body_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        # Colors
        primary = (0, 204, 51)
        text_color = (255, 255, 255)
        
        # C-Cube logo (top left)
        logo_text = "C-CUBE"
        draw.text((20, 20), logo_text, fill=primary, font=body_font)
        
        # AI indicator (top right)
        ai_text = "🎙️ AI Narration"
        ai_bbox = draw.textbbox((0, 0), ai_text, font=small_font)
        ai_width = ai_bbox[2] - ai_bbox[0]
        ai_x = self.width - ai_width - 20
        draw.text((ai_x, 20), ai_text, fill=text_color, font=small_font)
        
        return robot_img
    
    def create_subtitled_video_ffmpeg(self):
        """Create video with robot background and FFmpeg subtitle overlay"""
        print("🎬 Creating video with robot background and FFmpeg subtitles...")
        
        # Create robot background image
        robot_img = self.create_robot_background_image()
        robot_path = self.output_dir / "robot_background.png"
        robot_img.save(robot_path, "PNG")
        print(f"✅ Saved robot background: {robot_path}")
        
        # Create SRT subtitle file
        srt_path = self.create_srt_file()
        
        # Output video
        output_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional_RobotBG_Subtitles.mp4"
        
        try:
            # Use FFmpeg to create video with robot background, subtitles, and original audio
            cmd = [
                'ffmpeg', '-y',
                '-loop', '1', '-i', str(robot_path),
                '-i', str(self.source_video),
                '-filter_complex', 
                f"[0:v]scale={self.width}:{self.height}[bg];"
                f"[bg]subtitles='{srt_path}':force_style='Fontsize=16,PrimaryColour=&Hffffff,OutlineColour=&H000000,Outline=1,Alignment=2,MarginV=30'[v]",
                '-map', '[v]',
                '-map', '1:a',
                '-c:v', 'libx264',
                '-c:a', 'copy',
                '-t', '265',  # Ensure full duration
                '-pix_fmt', 'yuv420p',
                '-preset', 'fast',
                str(output_video)
            ]
            
            print("🎬 Running FFmpeg with subtitle overlay...")
            print(f"Command: {' '.join(cmd[:8])} [filter_complex] ...")
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Video with synchronized subtitles created!")
                print(f"📁 Output: {output_video}")
                
                # Clean up temp files
                robot_path.unlink()
                # Keep the SRT file for reference
                
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
    
    def create_subtitled_video(self):
        """Main function to create video with synchronized subtitles"""
        print("\n🤖 Starting FFmpeg Subtitle Creation...")
        print("=" * 70)
        
        if not self.source_video.exists():
            print(f"❌ Source video not found: {self.source_video}")
            return None
        
        video_path = self.create_subtitled_video_ffmpeg()
        
        if video_path:
            print(f"\n🎉 SUCCESS! ElevenLabs tutorial with synchronized subtitles!")
            print(f"📁 Output: {video_path}")
            print("🤖 Features:")
            print("   🎙️  Original ElevenLabs professional narration")
            print("   📝 Synchronized subtitles matching spoken words")
            print("   👁️  Robot background image")
            print("   🎨 Professional C-Cube styling")
            print("   🔊 High-quality audio preserved")
            print("   ⚡ Efficient FFmpeg processing")
            
            return video_path
        else:
            print("❌ Failed to create subtitled video")
            return None

def main():
    """Create ElevenLabs video with FFmpeg synchronized subtitles"""
    print("🤖 C-CUBE ELEVENLABS ROBOT WITH FFMPEG SUBTITLES")
    print("📝 Creating subtitles that sync with spoken audio using FFmpeg")
    print("=" * 70)
    
    creator = CCubeElevenLabsRobotSubtitlesFFmpeg()
    video_path = creator.create_subtitled_video()
    
    if video_path:
        print(f"\n🚀 FFMPEG SUBTITLE CREATION COMPLETE!")
        print(f"📁 New Video: {video_path}")
        print("✨ Your ElevenLabs tutorial now has synchronized subtitles!")

if __name__ == "__main__":
    main()