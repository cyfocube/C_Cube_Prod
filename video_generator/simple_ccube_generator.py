#!/usr/bin/env python3
"""
C-Cube Simple Video Generator
Creates basic tutorial videos with robot narration
"""

import os
import sys
import json
import time
from datetime import datetime
from pathlib import Path

# Core imports
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2

# Audio imports
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

# MoviePy imports
try:
    from moviepy.editor import *
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False

class SimpleCCubeVideoGenerator:
    """Simplified video generator for C-Cube tutorials"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        # Video settings
        self.width = 1280
        self.height = 720
        self.fps = 24
        self.robot_color = (0, 204, 51)  # C-Cube green
        
        print("🤖 Simple C-Cube Video Generator initialized")
        print(f"📁 Output: {self.output_dir}")
        print(f"🎥 Resolution: {self.width}x{self.height} @ {self.fps}fps")
    
    def create_robot_face(self, speaking=False, frame_size=(150, 150)):
        """Create simple robot face"""
        img = Image.new('RGBA', frame_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Robot head (circle)
        margin = 10
        radius = (frame_size[0] - margin * 2) // 2
        center_x, center_y = frame_size[0] // 2, frame_size[1] // 2
        
        # Head outline
        draw.ellipse([
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius
        ], outline=self.robot_color, width=3, fill=(20, 20, 20))
        
        # Eyes
        eye_size = radius // 5
        eye_y = center_y - radius // 3
        left_eye_x = center_x - radius // 2
        right_eye_x = center_x + radius // 2
        
        # Left eye
        draw.ellipse([
            left_eye_x - eye_size, eye_y - eye_size,
            left_eye_x + eye_size, eye_y + eye_size
        ], fill=self.robot_color)
        
        # Right eye
        draw.ellipse([
            right_eye_x - eye_size, eye_y - eye_size,
            right_eye_x + eye_size, eye_y + eye_size
        ], fill=self.robot_color)
        
        # Mouth
        mouth_y = center_y + radius // 4
        mouth_width = radius
        mouth_height = radius // 6
        
        if speaking:
            # Open mouth (speaking)
            draw.ellipse([
                center_x - mouth_width//2, mouth_y - mouth_height,
                center_x + mouth_width//2, mouth_y + mouth_height
            ], fill=self.robot_color)
        else:
            # Closed mouth
            draw.rectangle([
                center_x - mouth_width//2, mouth_y - mouth_height//2,
                center_x + mouth_width//2, mouth_y + mouth_height//2
            ], fill=self.robot_color)
        
        return img
    
    def create_tutorial_frame(self, title, content, robot_speaking=False, progress=0.0):
        """Create a single tutorial frame"""
        # Create black background
        frame = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        draw = ImageDraw.Draw(frame)
        
        # Load font
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
            content_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
        except:
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
        
        # Add title
        title_y = 50
        draw.text((50, title_y), title, fill=self.robot_color, font=title_font)
        
        # Add content (word wrap)
        content_y = 150
        max_width = self.width - 300  # Leave space for robot
        wrapped_content = self.wrap_text(content, content_font, max_width)
        
        for i, line in enumerate(wrapped_content[:15]):  # Max 15 lines
            line_y = content_y + i * 35
            draw.text((50, line_y), line, fill=(255, 255, 255), font=content_font)
        
        # Add robot
        robot = self.create_robot_face(speaking=robot_speaking)
        robot_x = self.width - 200
        robot_y = 50
        
        # Convert robot to RGB and paste
        robot_rgb = Image.new('RGB', robot.size, (0, 0, 0))
        robot_rgb.paste(robot, mask=robot.split()[-1])  # Use alpha as mask
        frame.paste(robot_rgb, (robot_x, robot_y))
        
        # Add progress bar
        if progress > 0:
            bar_width = 300
            bar_height = 10
            bar_x = 50
            bar_y = self.height - 50
            
            # Background
            draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], 
                         fill=(50, 50, 50))
            
            # Progress
            progress_width = int(bar_width * progress)
            draw.rectangle([bar_x, bar_y, bar_x + progress_width, bar_y + bar_height], 
                         fill=self.robot_color)
        
        return frame
    
    def wrap_text(self, text, font, max_width):
        """Wrap text to fit within max_width"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = font.getbbox(test_line)
            width = bbox[2] - bbox[0]
            
            if width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)  # Word too long, add anyway
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def generate_voice_audio(self, text, filename):
        """Generate voice audio for text"""
        if not TTS_AVAILABLE:
            print("⚠️  TTS not available, skipping audio")
            return False
        
        try:
            engine = pyttsx3.init()
            
            # Set robot-like voice properties
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)  # Slower speech
            
            volume = engine.getProperty('volume')
            engine.setProperty('volume', 0.9)
            
            # Save audio
            engine.save_to_file(text, str(filename))
            engine.runAndWait()
            
            print(f"🎤 Generated audio: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ Audio generation failed: {e}")
            return False
    
    def create_video_segment(self, title, content_text, duration=10):
        """Create a video segment"""
        print(f"🎬 Creating segment: {title}")
        
        frames = []
        total_frames = int(duration * self.fps)
        
        # Generate frames
        for frame_num in range(total_frames):
            progress = frame_num / total_frames
            speaking = (frame_num % 30) < 15  # Speaking animation
            
            frame = self.create_tutorial_frame(
                title=title,
                content=content_text,
                robot_speaking=speaking,
                progress=progress
            )
            
            # Convert to numpy array for OpenCV
            frame_array = np.array(frame)
            frames.append(frame_array)
        
        return frames
    
    def save_as_video(self, frames, filename, audio_file=None):
        """Save frames as video file"""
        if not MOVIEPY_AVAILABLE:
            print("⚠️  MoviePy not available, saving as image sequence")
            for i, frame in enumerate(frames[::6]):  # Save every 6th frame
                img = Image.fromarray(frame)
                img.save(self.output_dir / f"{filename}_frame_{i:04d}.png")
            return
        
        try:
            # Create video clip
            clip = ImageSequenceClip([frame for frame in frames], fps=self.fps)
            
            # Add audio if available
            if audio_file and Path(audio_file).exists():
                audio = AudioFileClip(str(audio_file))
                clip = clip.set_audio(audio)
            
            # Save video
            output_path = self.output_dir / f"{filename}.mp4"
            clip.write_videofile(str(output_path), fps=self.fps, verbose=False, logger=None)
            
            print(f"✅ Video saved: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"❌ Video save failed: {e}")
            return None
    
    def create_tutorial_sections(self):
        """Create tutorial sections from the guide"""
        # Basic tutorial sections based on our guide
        sections = [
            {
                "title": "Welcome to C-Cube Cold Wallet",
                "content": "Hi there! I'm your C-Cube assistant. I'll guide you through using the most secure cold wallet for cryptocurrency. Let's start with the basics of what makes C-Cube special.",
                "duration": 8
            },
            {
                "title": "Getting Started - Security First",
                "content": "Before we begin, remember that C-Cube prioritizes your security. Your private keys never leave your device unless you choose to broadcast a transaction. This keeps your crypto safe from online threats.",
                "duration": 10
            },
            {
                "title": "Creating Your First Wallet",
                "content": "Let's create your first wallet. Click 'Setup New Wallet' on the welcome screen. Choose a strong password to encrypt your private key. Write down your recovery phrase immediately and store it safely offline.",
                "duration": 12
            },
            {
                "title": "Understanding Networks",
                "content": "C-Cube supports multiple blockchain networks. You can use Ethereum, Polygon, Binance Smart Chain, Arbitrum, and Optimism. Each network has different fees and features. Start with Ethereum for learning.",
                "duration": 10
            },
            {
                "title": "Sending Your First Transaction",
                "content": "To send cryptocurrency, go to the Sign Transaction tab. Enter the recipient address, amount, and verify all details carefully. Sign the transaction with your password, then broadcast it to the network when ready.",
                "duration": 12
            }
        ]
        
        return sections
    
    def generate_complete_tutorial(self):
        """Generate the complete tutorial video"""
        print("🚀 Generating C-Cube tutorial video...")
        
        sections = self.create_tutorial_sections()
        all_video_clips = []
        
        # Create intro
        print("🎬 Creating intro...")
        intro_frames = self.create_video_segment(
            "C-Cube Cold Wallet Tutorial",
            "Welcome to the complete guide for secure cryptocurrency management with C-Cube!",
            duration=5
        )
        
        if MOVIEPY_AVAILABLE:
            intro_clip = ImageSequenceClip(intro_frames, fps=self.fps)
            all_video_clips.append(intro_clip)
        
        # Create each section
        for i, section in enumerate(sections):
            print(f"🎬 Creating section {i+1}/{len(sections)}: {section['title']}")
            
            # Generate audio
            audio_file = self.output_dir / f"section_{i:02d}_audio.wav"
            self.generate_voice_audio(section['content'], audio_file)
            
            # Generate video frames
            frames = self.create_video_segment(
                section['title'],
                section['content'],
                section['duration']
            )
            
            # Save individual section
            section_filename = f"section_{i:02d}_{section['title'].replace(' ', '_')}"
            
            if MOVIEPY_AVAILABLE:
                clip = ImageSequenceClip(frames, fps=self.fps)
                
                # Add audio if available
                if audio_file.exists():
                    audio = AudioFileClip(str(audio_file))
                    clip = clip.set_audio(audio)
                
                all_video_clips.append(clip)
                
                # Save individual section
                clip.write_videofile(
                    str(self.output_dir / f"{section_filename}.mp4"),
                    fps=self.fps, verbose=False, logger=None
                )
            else:
                # Save as images if no MoviePy
                for j, frame in enumerate(frames[::6]):
                    img = Image.fromarray(frame)
                    img.save(self.output_dir / f"{section_filename}_frame_{j:04d}.png")
        
        # Combine all clips into final video
        if MOVIEPY_AVAILABLE and all_video_clips:
            print("🎬 Combining all sections...")
            final_video = concatenate_videoclips(all_video_clips)
            
            # Add outro
            outro_frames = self.create_video_segment(
                "Thank You!",
                "You're now ready to use C-Cube safely and securely. Remember to keep your recovery phrase safe and always verify transaction details before signing.",
                duration=5
            )
            outro_clip = ImageSequenceClip(outro_frames, fps=self.fps)
            
            # Final combination
            complete_video = concatenate_videoclips([final_video, outro_clip])
            
            # Save final video
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_filename = f"CCube_Complete_Tutorial_{timestamp}.mp4"
            final_path = self.output_dir / final_filename
            
            complete_video.write_videofile(str(final_path), fps=self.fps)
            
            print(f"🎉 Complete tutorial video created: {final_path}")
            print(f"📊 Duration: {complete_video.duration:.1f} seconds")
            
            return final_path
        
        else:
            print("✅ Tutorial sections created as image sequences")
            print(f"📁 Check the output folder: {self.output_dir}")
            return self.output_dir

def main():
    """Main function"""
    print("🤖 C-Cube Simple Video Generator")
    print("=" * 50)
    
    # Create generator
    generator = SimpleCCubeVideoGenerator()
    
    # Generate tutorial
    result = generator.generate_complete_tutorial()
    
    if result:
        print(f"\n🎉 Tutorial generation completed!")
        print(f"📂 Output location: {result}")
        print("\n📋 What was created:")
        print("- Individual tutorial sections")
        print("- Combined complete tutorial video (if MoviePy available)")
        print("- Audio files for each section (if TTS available)")
        
        print("\n💡 Tips:")
        print("- Play the video to see your robot tutorial")
        print("- Use individual sections for specific topics")
        print("- The robot provides visual guidance throughout")
    else:
        print("❌ Tutorial generation failed")

if __name__ == "__main__":
    main()
