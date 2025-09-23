#!/usr/bin/env python3
"""
C-Cube Tutorial Video Generator
Advanced Python-based video creation system for C-Cube Cold Wallet tutorials
"""

import os
import sys
import json
import time
from datetime import datetime
from pathlib import Path

# Core video libraries
try:
    from moviepy.editor import *
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
except ImportError as e:
    print(f"❌ Missing required libraries: {e}")
    print("📦 Install with: pip install -r requirements.txt")
    sys.exit(1)

# Audio libraries
try:
    import pyttsx3
    from gtts import gTTS
    from pydub import AudioSegment
except ImportError:
    print("⚠️  Audio libraries not available. Install for voice features.")

# Screen capture libraries
try:
    import pyautogui
    import mss
except ImportError:
    print("⚠️  Screen capture libraries not available.")

class CCubeVideoGenerator:
    """
    Main class for generating C-Cube tutorial videos
    """
    
    def __init__(self, output_dir="output", app_url="http://localhost:3000"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.app_url = app_url
        
        # Video settings
        self.video_settings = {
            'fps': 30,
            'resolution': (1920, 1080),
            'duration': 600,  # 10 minutes max
            'background_color': (0, 0, 0),  # Black background
            'robot_color': (0, 204, 51),    # C-Cube green
        }
        
        # Robot character settings
        self.robot_settings = {
            'voice_speed': 150,
            'voice_pitch': 1.2,
            'animation_speed': 2.0,
            'highlight_color': (0, 255, 255),  # Cyan for highlights
        }
        
        # Tutorial script from the guide
        self.tutorial_script = self.load_tutorial_script()
        
        print("🤖 C-Cube Video Generator initialized")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"🎬 Video settings: {self.video_settings['resolution']} @ {self.video_settings['fps']}fps")
    
    def load_tutorial_script(self):
        """Load and parse the tutorial guide into video segments"""
        script_path = Path("C-Cube_Wallet_Complete_Tutorial_Guide.md")
        
        if not script_path.exists():
            print("❌ Tutorial guide not found!")
            return []
        
        # Parse the markdown guide into video segments
        segments = []
        current_section = None
        current_content = []
        
        with open(script_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines:
            if line.startswith('## '):
                # New section
                if current_section:
                    segments.append({
                        'title': current_section,
                        'content': '\n'.join(current_content),
                        'duration': self.estimate_duration(current_content)
                    })
                current_section = line.strip('## \n')
                current_content = []
            elif line.startswith('### '):
                # Subsection
                current_content.append(line.strip())
            elif line.strip() and not line.startswith('#'):
                # Content
                current_content.append(line.strip())
        
        # Add final section
        if current_section:
            segments.append({
                'title': current_section,
                'content': '\n'.join(current_content),
                'duration': self.estimate_duration(current_content)
            })
        
        print(f"📚 Loaded {len(segments)} tutorial segments")
        return segments
    
    def estimate_duration(self, content_lines):
        """Estimate video duration based on content length"""
        words = sum(len(line.split()) for line in content_lines)
        # Average speaking rate: 150 words per minute
        return max(10, words / 150 * 60)  # Minimum 10 seconds per segment
    
    def create_robot_avatar(self, frame_size=(200, 200)):
        """Create animated robot avatar for the tutorial"""
        width, height = frame_size
        
        # Create robot base image
        img = Image.new('RGBA', frame_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Robot head (circle)
        head_radius = width // 4
        head_center = (width // 2, height // 2)
        draw.ellipse([
            head_center[0] - head_radius,
            head_center[1] - head_radius,
            head_center[0] + head_radius,
            head_center[1] + head_radius
        ], fill=self.video_settings['robot_color'], outline=(255, 255, 255), width=2)
        
        # Robot eyes
        eye_size = head_radius // 4
        left_eye = (head_center[0] - head_radius//2, head_center[1] - head_radius//3)
        right_eye = (head_center[0] + head_radius//2, head_center[1] - head_radius//3)
        
        for eye_pos in [left_eye, right_eye]:
            draw.ellipse([
                eye_pos[0] - eye_size,
                eye_pos[1] - eye_size,
                eye_pos[0] + eye_size,
                eye_pos[1] + eye_size
            ], fill=(255, 255, 255))
        
        # Robot mouth (speaking indicator)
        mouth_width = head_radius
        mouth_height = head_radius // 4
        mouth_pos = (head_center[0] - mouth_width//2, head_center[1] + head_radius//4)
        draw.rectangle([
            mouth_pos[0],
            mouth_pos[1],
            mouth_pos[0] + mouth_width,
            mouth_pos[1] + mouth_height
        ], fill=(255, 255, 255))
        
        return np.array(img)
    
    def animate_robot_speaking(self, duration, fps=30):
        """Create animated robot speaking sequence"""
        frames = []
        total_frames = int(duration * fps)
        
        for frame_num in range(total_frames):
            # Animate robot mouth and eyes for speaking effect
            robot_frame = self.create_robot_avatar()
            
            # Add blinking animation
            if frame_num % 90 == 0:  # Blink every 3 seconds
                # Create blink effect
                pass
            
            # Add mouth movement for speaking
            speaking_intensity = abs(np.sin(frame_num * 0.3))  # Speaking wave
            
            frames.append(robot_frame)
        
        return frames
    
    def generate_voice_audio(self, text, output_file):
        """Generate robot voice audio from text"""
        try:
            # Method 1: Use pyttsx3 for offline TTS
            engine = pyttsx3.init()
            engine.setProperty('rate', self.robot_settings['voice_speed'])
            
            # Get available voices and try to find a robotic one
            voices = engine.getProperty('voices')
            for voice in voices:
                if 'robot' in voice.name.lower() or 'synthetic' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
            
            engine.save_to_file(text, str(output_file))
            engine.runAndWait()
            
            print(f"🎤 Generated voice audio: {output_file}")
            return True
            
        except Exception as e:
            try:
                # Method 2: Use gTTS as fallback
                tts = gTTS(text=text, lang='en', slow=False)
                tts.save(str(output_file))
                print(f"🎤 Generated voice audio (gTTS): {output_file}")
                return True
                
            except Exception as e2:
                print(f"❌ Voice generation failed: {e}, {e2}")
                return False
    
    def capture_app_screenshot(self, element_selector=None):
        """Capture screenshot of the C-Cube application"""
        try:
            # Take full screen screenshot
            with mss.mss() as sct:
                screenshot = sct.grab(sct.monitors[1])  # Primary monitor
                img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
                return np.array(img)
                
        except Exception as e:
            print(f"❌ Screenshot capture failed: {e}")
            # Return placeholder image
            placeholder = np.zeros((1080, 1920, 3), dtype=np.uint8)
            return placeholder
    
    def create_tutorial_segment(self, segment, segment_index):
        """Create a single tutorial video segment"""
        print(f"🎬 Creating segment {segment_index + 1}: {segment['title']}")
        
        # Generate voice audio
        audio_file = self.output_dir / f"segment_{segment_index:02d}_audio.wav"
        voice_text = self.extract_speech_text(segment['content'])
        
        if not self.generate_voice_audio(voice_text, audio_file):
            print(f"⚠️  Skipping segment {segment_index + 1} - audio generation failed")
            return None
        
        # Create video frames
        frames = []
        duration = segment['duration']
        fps = self.video_settings['fps']
        total_frames = int(duration * fps)
        
        for frame_num in range(total_frames):
            # Create base frame
            frame = np.zeros((1080, 1920, 3), dtype=np.uint8)
            
            # Add app screenshot (if available)
            app_screenshot = self.capture_app_screenshot()
            if app_screenshot is not None:
                frame[:app_screenshot.shape[0], :app_screenshot.shape[1]] = app_screenshot
            
            # Add robot avatar
            robot_frame = self.create_robot_avatar()
            # Overlay robot in corner
            robot_x, robot_y = 1920-220, 20
            robot_h, robot_w = robot_frame.shape[:2]
            frame[robot_y:robot_y+robot_h, robot_x:robot_x+robot_w] = robot_frame[:,:,:3]
            
            # Add title overlay
            frame = self.add_title_overlay(frame, segment['title'])
            
            # Add highlights based on content
            frame = self.add_content_highlights(frame, segment['content'], frame_num / total_frames)
            
            frames.append(frame)
        
        # Create video clip
        video_clip = ImageSequenceClip(frames, fps=fps)
        
        # Add audio if available
        if audio_file.exists():
            audio_clip = AudioFileClip(str(audio_file))
            video_clip = video_clip.set_audio(audio_clip)
        
        # Save segment
        segment_file = self.output_dir / f"segment_{segment_index:02d}_{segment['title'].replace(' ', '_')}.mp4"
        video_clip.write_videofile(str(segment_file), fps=fps, verbose=False, logger=None)
        
        print(f"✅ Segment {segment_index + 1} completed: {segment_file}")
        return segment_file
    
    def extract_speech_text(self, content):
        """Extract text suitable for speech from markdown content"""
        lines = content.split('\n')
        speech_lines = []
        
        for line in lines:
            # Skip markdown formatting
            if line.startswith('#') or line.startswith('**') or line.startswith('- '):
                continue
            
            # Clean up the line
            clean_line = line.strip('*_`[](){}')
            if clean_line and len(clean_line) > 10:
                speech_lines.append(clean_line)
        
        return '. '.join(speech_lines[:5])  # Limit to first 5 sentences
    
    def add_title_overlay(self, frame, title):
        """Add title overlay to video frame"""
        # Convert to PIL for text rendering
        img = Image.fromarray(frame)
        draw = ImageDraw.Draw(img)
        
        # Try to load a font, fallback to default
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
        except:
            font = ImageFont.load_default()
        
        # Add title with background
        text_bbox = draw.textbbox((0, 0), title, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Background rectangle
        padding = 20
        bg_x = 50
        bg_y = 50
        draw.rectangle([
            bg_x - padding,
            bg_y - padding,
            bg_x + text_width + padding,
            bg_y + text_height + padding
        ], fill=(0, 0, 0, 180))
        
        # Title text
        draw.text((bg_x, bg_y), title, fill=self.video_settings['robot_color'], font=font)
        
        return np.array(img)
    
    def add_content_highlights(self, frame, content, progress):
        """Add dynamic highlights based on content and progress"""
        # Add animated highlights for key UI elements
        highlight_color = self.robot_settings['highlight_color']
        
        # Example: highlight specific areas based on content
        if 'wallet' in content.lower():
            # Highlight wallet area
            cv2.rectangle(frame, (100, 200), (300, 400), highlight_color, 3)
        
        if 'transaction' in content.lower():
            # Highlight transaction area
            cv2.rectangle(frame, (500, 300), (800, 500), highlight_color, 3)
        
        return frame
    
    def generate_complete_video(self):
        """Generate the complete tutorial video"""
        print("🚀 Starting C-Cube tutorial video generation...")
        
        segment_files = []
        
        # Generate each tutorial segment
        for i, segment in enumerate(self.tutorial_script[:5]):  # Limit to first 5 segments for demo
            segment_file = self.create_tutorial_segment(segment, i)
            if segment_file:
                segment_files.append(segment_file)
        
        if not segment_files:
            print("❌ No segments generated successfully")
            return None
        
        # Combine all segments into final video
        print("🎬 Combining segments into final video...")
        
        clips = [VideoFileClip(str(f)) for f in segment_files]
        final_video = concatenate_videoclips(clips)
        
        # Add intro and outro
        final_video = self.add_intro_outro(final_video)
        
        # Save final video
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        final_file = self.output_dir / f"CCube_Tutorial_{timestamp}.mp4"
        
        final_video.write_videofile(
            str(final_file),
            fps=self.video_settings['fps'],
            verbose=True
        )
        
        print(f"🎉 Tutorial video completed: {final_file}")
        print(f"📊 Duration: {final_video.duration:.1f} seconds")
        print(f"📁 File size: {final_file.stat().st_size / (1024*1024):.1f} MB")
        
        return final_file
    
    def add_intro_outro(self, main_video):
        """Add intro and outro to the video"""
        # Create intro clip
        intro_duration = 5
        intro_clip = self.create_intro_clip(intro_duration)
        
        # Create outro clip
        outro_duration = 3
        outro_clip = self.create_outro_clip(outro_duration)
        
        # Combine intro + main + outro
        final_video = concatenate_videoclips([intro_clip, main_video, outro_clip])
        
        return final_video
    
    def create_intro_clip(self, duration):
        """Create animated intro sequence"""
        # Create frames for intro animation
        frames = []
        fps = self.video_settings['fps']
        total_frames = int(duration * fps)
        
        for frame_num in range(total_frames):
            frame = np.zeros((1080, 1920, 3), dtype=np.uint8)
            
            # Add C-Cube logo animation
            progress = frame_num / total_frames
            
            # Animated title
            frame = self.add_animated_title(frame, "C-Cube Cold Wallet Tutorial", progress)
            
            frames.append(frame)
        
        return ImageSequenceClip(frames, fps=fps)
    
    def create_outro_clip(self, duration):
        """Create outro sequence"""
        frames = []
        fps = self.video_settings['fps']
        total_frames = int(duration * fps)
        
        for frame_num in range(total_frames):
            frame = np.zeros((1080, 1920, 3), dtype=np.uint8)
            
            # Add "Thank you" message
            frame = self.add_title_overlay(frame, "Thank you for watching!")
            
            frames.append(frame)
        
        return ImageSequenceClip(frames, fps=fps)
    
    def add_animated_title(self, frame, title, progress):
        """Add animated title with effects"""
        img = Image.fromarray(frame)
        draw = ImageDraw.Draw(img)
        
        # Animated appearance
        alpha = int(255 * min(1.0, progress * 2))
        
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 72)
        except:
            font = ImageFont.load_default()
        
        # Center the title
        text_bbox = draw.textbbox((0, 0), title, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        x = (1920 - text_width) // 2
        y = (1080 - text_height) // 2
        
        # Add glow effect
        for offset in range(5, 0, -1):
            glow_color = tuple(int(c * 0.3) for c in self.video_settings['robot_color'])
            for dx in [-offset, 0, offset]:
                for dy in [-offset, 0, offset]:
                    draw.text((x + dx, y + dy), title, fill=glow_color, font=font)
        
        # Main title
        draw.text((x, y), title, fill=self.video_settings['robot_color'], font=font)
        
        return np.array(img)

def main():
    """Main function to generate the tutorial video"""
    print("🤖 C-Cube Tutorial Video Generator")
    print("=" * 50)
    
    # Initialize generator
    generator = CCubeVideoGenerator()
    
    # Generate the complete tutorial video
    final_video = generator.generate_complete_video()
    
    if final_video:
        print(f"🎉 SUCCESS! Tutorial video generated: {final_video}")
        print("\n📋 Next steps:")
        print("1. Review the generated video")
        print("2. Test with your C-Cube application")
        print("3. Adjust settings and regenerate if needed")
        print("4. Share with your users!")
    else:
        print("❌ Video generation failed. Check the logs above.")

if __name__ == "__main__":
    main()
