#!/usr/bin/env python3
"""
C-Cube ElevenLabs AI Voice Tutorial Generator
Creates professional tutorial video with ElevenLabs AI voice technology
"""

import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import time
import requests
import json

class CCubeElevenLabsTutorialGenerator:
    """Generate C-Cube tutorial video with ElevenLabs AI voice"""
    
    def __init__(self, api_key=None):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        # ElevenLabs API configuration
        self.api_key = api_key or os.getenv('ELEVENLABS_API_KEY')
        self.base_url = "https://api.elevenlabs.io/v1"
        
        # Video settings
        self.width = 1280
        self.height = 720
        self.fps = 15
        self.robot_color = (0, 204, 51)
        
        # ElevenLabs voice configurations for different moods
        self.voice_configs = {
            'robotic_friendly': {
                'voice_id': 'pNInz6obpgDQGcFmaJgB',  # Adam - can be made robotic
                'model_id': 'eleven_monolingual_v1',
                'voice_settings': {
                    'stability': 0.8,
                    'similarity_boost': 0.7,
                    'style': 0.3,
                    'use_speaker_boost': True
                }
            },
            'robotic_technical': {
                'voice_id': 'EXAVITQu4vr4xnSDxMaL',  # Bella - clear and technical
                'model_id': 'eleven_monolingual_v1',
                'voice_settings': {
                    'stability': 0.9,
                    'similarity_boost': 0.8,
                    'style': 0.2,
                    'use_speaker_boost': True
                }
            },
            'robotic_authoritative': {
                'voice_id': 'VR6AewLTigWG4xSOukaG',  # Arnold - deep and authoritative
                'model_id': 'eleven_monolingual_v1',
                'voice_settings': {
                    'stability': 0.9,
                    'similarity_boost': 0.9,
                    'style': 0.1,
                    'use_speaker_boost': True
                }
            }
        }
        
        print("🤖 C-Cube ElevenLabs AI Voice Tutorial Generator")
        print(f"📁 Output: {self.output_dir}")
        print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
        print("🎵 Voice: ElevenLabs AI with robotic processing")
        
        if not self.api_key:
            print("⚠️  No ElevenLabs API key found. Will use fallback TTS.")
            print("   Set ELEVENLABS_API_KEY environment variable for best results.")
    
    def create_advanced_robot_face(self, speaking=False, emotion='neutral'):
        """Create advanced robotic face with emotion and enhanced animations"""
        size = (140, 140)
        img = Image.new('RGBA', size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        center_x, center_y = size[0] // 2, size[1] // 2
        
        # Advanced hexagonal robotic head with emotion-based styling
        head_points = []
        emotion_modifier = 1.1 if emotion == 'excited' else 0.9 if emotion == 'serious' else 1.0
        
        for i in range(6):
            angle = i * 60
            base_radius = 45 * emotion_modifier
            x = center_x + base_radius * (1 if i % 2 == 0 else 0.85) * (1 if angle < 180 else 1)
            y = center_y + base_radius * (0.85 if i % 2 == 0 else 1) * (1 if 90 < angle < 270 else 1)
            head_points.append((x, y))
        
        # Dynamic head color based on emotion and speaking
        if emotion == 'excited':
            head_fill = (12, 18, 25)
            outline_color = (0, 255, 120)
        elif emotion == 'serious':
            head_fill = (8, 8, 15)
            outline_color = (255, 100, 0)
        else:
            head_fill = (8, 12, 18)
            outline_color = self.robot_color
        
        draw.polygon(head_points, outline=outline_color, width=3, fill=head_fill)
        
        # Advanced LED eyes with emotion and AI processing indicators
        current_time = time.time()
        pulse_intensity = int(current_time * 10) % 30
        
        if emotion == 'excited':
            base_eye_color = (0, 255, 150)
        elif emotion == 'serious':
            base_eye_color = (255, 150, 0)
        else:
            base_eye_color = (0, 255, 100)
        
        eye_color = base_eye_color if speaking else tuple(int(c * 0.7) for c in base_eye_color)
        
        # Left eye - advanced LED matrix style
        eye_width, eye_height = 20, 10
        left_eye_x = center_x - 30
        left_eye_y = center_y - 15
        
        # Main eye rectangle
        draw.rectangle([left_eye_x, left_eye_y, left_eye_x + eye_width, left_eye_y + eye_height], 
                      fill=eye_color)
        
        # LED segments for robotic feel
        for i in range(3):
            segment_x = left_eye_x + 2 + i * 6
            segment_brightness = 255 if speaking and (current_time * 8 + i) % 2 < 1 else 180
            segment_color = (0, segment_brightness, int(segment_brightness * 0.4))
            draw.rectangle([segment_x, left_eye_y + 2, segment_x + 4, left_eye_y + eye_height - 2], 
                          fill=segment_color)
        
        # Right eye - mirror of left
        right_eye_x = center_x + 10
        draw.rectangle([right_eye_x, left_eye_y, right_eye_x + eye_width, left_eye_y + eye_height], 
                      fill=eye_color)
        
        for i in range(3):
            segment_x = right_eye_x + 2 + i * 6
            segment_brightness = 255 if speaking and (current_time * 8 + i) % 2 < 1 else 180
            segment_color = (0, segment_brightness, int(segment_brightness * 0.4))
            draw.rectangle([segment_x, left_eye_y + 2, segment_x + 4, left_eye_y + eye_height - 2], 
                          fill=segment_color)
        
        # Advanced robotic mouth with AI processing visualization
        mouth_y = center_y + 20
        
        if speaking:
            # AI voice processing visualization - dynamic waveform
            num_bars = 8
            bar_width = 3
            bar_spacing = 4
            start_x = center_x - (num_bars * (bar_width + bar_spacing)) // 2
            
            for i in range(num_bars):
                bar_x = start_x + i * (bar_width + bar_spacing)
                # Complex waveform simulation
                wave_height = 8 + int(6 * abs(time.time() * 15 + i * 0.8) % 1)
                wave_brightness = 200 + int(55 * abs(time.time() * 12 + i * 0.6) % 1)
                
                if emotion == 'excited':
                    bar_color = (0, wave_brightness, 100)
                elif emotion == 'serious':
                    bar_color = (wave_brightness, int(wave_brightness * 0.6), 0)
                else:
                    bar_color = (0, wave_brightness, 51)
                
                draw.rectangle([bar_x, mouth_y - wave_height//2, 
                               bar_x + bar_width, mouth_y + wave_height//2], 
                              fill=bar_color)
                
                # Add small connection lines for circuit effect
                if i < num_bars - 1:
                    line_color = tuple(int(c * 0.3) for c in bar_color)
                    draw.line([(bar_x + bar_width, mouth_y), 
                              (bar_x + bar_width + bar_spacing, mouth_y)], 
                             fill=line_color, width=1)
        else:
            # Idle state - single LED line with subtle pulse
            mouth_width = 35
            pulse_width = int(mouth_width * (0.8 + 0.2 * abs(time.time() * 2) % 1))
            mouth_x = center_x - pulse_width // 2
            
            draw.rectangle([mouth_x, mouth_y - 2, mouth_x + pulse_width, mouth_y + 2], 
                          fill=outline_color)
        
        # Advanced AI status antenna with data transmission visualization
        antenna_x = center_x
        antenna_y = center_y - 55
        
        # Main antenna
        draw.rectangle([antenna_x - 1, antenna_y, antenna_x + 1, antenna_y + 15], 
                      fill=outline_color)
        
        # AI processing status LED with advanced patterns
        if speaking:
            # Data transmission pattern
            led_size = 5
            led_colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255)]
            color_idx = int(current_time * 5) % len(led_colors)
            status_color = led_colors[color_idx]
        else:
            led_size = 3
            status_color = (100, 255, 100)
        
        draw.ellipse([antenna_x - led_size, antenna_y - led_size, 
                     antenna_x + led_size, antenna_y + led_size], 
                    fill=status_color)
        
        # Additional circuit details for enhanced robotic appearance
        circuit_color = tuple(int(c * 0.4) for c in outline_color)
        
        # Left circuit pattern
        draw.rectangle([center_x - 50, center_y + 30, center_x - 35, center_y + 32], 
                      fill=circuit_color)
        draw.rectangle([center_x - 45, center_y + 25, center_x - 43, center_y + 35], 
                      fill=circuit_color)
        
        # Right circuit pattern
        draw.rectangle([center_x + 35, center_y + 30, center_x + 50, center_y + 32], 
                      fill=circuit_color)
        draw.rectangle([center_x + 43, center_y + 25, center_x + 45, center_y + 35], 
                      fill=circuit_color)
        
        # Add small LED indicators on sides
        side_led_color = (100, 200, 100) if speaking else (50, 100, 50)
        draw.ellipse([center_x - 58, center_y + 28, center_x - 54, center_y + 32], 
                    fill=side_led_color)
        draw.ellipse([center_x + 54, center_y + 28, center_x + 58, center_y + 32], 
                    fill=side_led_color)
        
        return img
    
    def create_professional_frame(self, title, content, section_num, total_sections, 
                                speaking=False, progress=0.0, emotion='neutral'):
        """Create professional tutorial frame with enhanced AI styling"""
        frame = Image.new('RGB', (self.width, self.height), (2, 4, 8))
        draw = ImageDraw.Draw(frame)
        
        # Advanced tech grid background
        grid_spacing = 60
        grid_alpha = 8
        for x in range(0, self.width, grid_spacing):
            alpha_var = grid_alpha + int(3 * abs(x / grid_spacing + time.time() * 0.5) % 1)
            draw.line([(x, 0), (x, self.height)], 
                     fill=(alpha_var, alpha_var + 2, alpha_var + 4), width=1)
        for y in range(0, self.height, grid_spacing):
            alpha_var = grid_alpha + int(3 * abs(y / grid_spacing + time.time() * 0.3) % 1)
            draw.line([(0, y), (self.width, y)], 
                     fill=(alpha_var, alpha_var + 2, alpha_var + 4), width=1)
        
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
            content_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
            small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 15)
            tech_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 13)
        except:
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
            tech_font = ImageFont.load_default()
        
        # Professional header with AI branding
        header_height = 75
        
        # Gradient header background
        for i in range(header_height):
            alpha = int(80 * (1 - i / header_height))
            if alpha > 0:
                draw.line([(0, i), (self.width, i)], fill=(0, 0, 0, alpha))
        
        # AI accent lines
        accent_colors = [(0, 255, 120), (100, 255, 200), (50, 200, 255)]
        for i, color in enumerate(accent_colors):
            y_pos = header_height - 6 + i * 2
            alpha = 255 if speaking else 150
            line_color = tuple(int(c * alpha / 255) for c in color)
            draw.line([(0, y_pos), (self.width, y_pos)], fill=line_color, width=1)
        
        # Enhanced logo with AI elements
        logo_text = "C-CUBE"
        # Logo shadow for depth
        draw.text((22, 24), logo_text, fill=(0, 30, 0), font=title_font)
        # Main logo
        draw.text((20, 22), logo_text, fill=self.robot_color, font=title_font)
        
        # AI system subtitle with version
        ai_subtitle = "AI TUTORIAL SYSTEM • ElevenLabs POWERED"
        draw.text((20, 52), ai_subtitle, fill=(80, 150, 200), font=tech_font)
        
        # Professional info panel with AI status
        panel_x = self.width - 350
        panel_width = 330
        panel_height = 68
        
        # Panel with professional styling
        draw.rounded_rectangle([panel_x, 4, panel_x + panel_width, 4 + panel_height], 
                             radius=10, fill=(8, 12, 20), outline=(60, 120, 180), width=2)
        
        # AI processing indicator corners
        corner_size = 12
        corner_color = (0, 200, 100) if speaking else (100, 100, 100)
        
        # Top corners
        draw.rectangle([panel_x + 5, 9, panel_x + 5 + corner_size, 11], fill=corner_color)
        draw.rectangle([panel_x + panel_width - 5 - corner_size, 9, 
                       panel_x + panel_width - 5, 11], fill=corner_color)
        
        # Section information
        section_text = f"SECTION {section_num:02d} OF {total_sections:02d}"
        draw.text((panel_x + 15, 18), section_text, fill=(120, 200, 255), font=small_font)
        
        # AI processing status with dynamic indicator
        if speaking:
            processing_dots = "●" * (int(time.time() * 3) % 3 + 1) + "○" * (3 - int(time.time() * 3) % 3 - 1)
            ai_status = f"🤖 AI PROCESSING {processing_dots}"
            status_color = (255, 120, 120)
        else:
            ai_status = "🤖 AI STANDBY • READY"
            status_color = (120, 255, 120)
        
        draw.text((panel_x + 15, 36), ai_status, fill=status_color, font=small_font)
        
        # Real-time progress with ETA
        progress_text = f"COMPLETION: {progress*100:.1f}%"
        eta_seconds = (1 - progress) * 200  # Estimated remaining time
        eta_text = f"ETA: {eta_seconds:.0f}s"
        
        draw.text((panel_x + 15, 54), progress_text, fill=(180, 180, 180), font=tech_font)
        draw.text((panel_x + 180, 54), eta_text, fill=(150, 200, 150), font=tech_font)
        
        # Enhanced title with smart color coding
        title_y = header_height + 25
        
        # Dynamic title color based on content type
        if any(term in title.lower() for term in ['security', 'recovery', 'protection']):
            title_color = (255, 200, 100)  # Gold for security
            title_glow = (80, 60, 0)
        elif any(term in title.lower() for term in ['welcome', 'getting started', 'journey']):
            title_color = (100, 255, 150)  # Green for welcome
            title_glow = (0, 80, 30)
        elif any(term in title.lower() for term in ['advanced', 'features', 'troubleshooting']):
            title_color = (150, 200, 255)  # Blue for technical
            title_glow = (30, 40, 80)
        else:
            title_color = self.robot_color
            title_glow = (0, 40, 10)
        
        # Title with glow effect
        if len(title) > 45:
            title_words = title.split()
            mid = len(title_words) // 2
            title_line1 = ' '.join(title_words[:mid])
            title_line2 = ' '.join(title_words[mid:])
            
            # Glow
            draw.text((22, title_y + 2), title_line1, fill=title_glow, font=title_font)
            draw.text((22, title_y + 37), title_line2, fill=title_glow, font=title_font)
            # Main text
            draw.text((20, title_y), title_line1, fill=title_color, font=title_font)
            draw.text((20, title_y + 35), title_line2, fill=title_color, font=title_font)
            content_y = title_y + 80
        else:
            draw.text((22, title_y + 2), title, fill=title_glow, font=title_font)
            draw.text((20, title_y), title, fill=title_color, font=title_font)
            content_y = title_y + 45
        
        # Enhanced content display with AI-powered formatting
        content_width = self.width - 220
        words = content.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if len(test_line) * 12 <= content_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
        if current_line:
            lines.append(' '.join(current_line))
        
        # AI-powered content highlighting
        max_lines = (self.height - content_y - 120) // 24
        for i, line in enumerate(lines[:max_lines]):
            if line.strip():
                line_y = content_y + i * 24
                
                # Advanced color coding with context awareness
                if any(term in line.lower() for term in ['critical', 'important', 'never', 'warning']):
                    text_color = (255, 150, 150)  # Red for warnings
                elif any(term in line.lower() for term in ['security', 'password', 'recovery phrase', 'private key']):
                    text_color = (255, 220, 120)  # Gold for security
                elif any(term in line.lower() for term in ['c-cube', 'wallet', 'blockchain', 'crypto']):
                    text_color = (120, 255, 180)  # Green for product
                elif any(term in line.lower() for term in ['gas', 'fee', 'transaction', 'network', 'ethereum']):
                    text_color = (180, 220, 255)  # Blue for technical
                elif any(term in line.lower() for term in ['congratulations', 'success', 'complete', 'ready']):
                    text_color = (150, 255, 150)  # Bright green for success
                else:
                    # Fade effect for better visual hierarchy
                    fade_factor = max(0.6, 1.0 - (i / max_lines) * 0.4)
                    base_brightness = int(240 * fade_factor)
                    text_color = (base_brightness, base_brightness, base_brightness)
                
                # Add subtle shadow for professional look
                shadow_color = tuple(int(c * 0.15) for c in text_color)
                draw.text((21, line_y + 1), line, fill=shadow_color, font=content_font)
                draw.text((20, line_y), line, fill=text_color, font=content_font)
        
        # Professional AI tutor panel
        robot_panel_x = self.width - 180
        robot_panel_y = 95
        robot_panel_width = 170
        robot_panel_height = 200
        
        # Advanced panel styling
        draw.rounded_rectangle([
            robot_panel_x, robot_panel_y,
            robot_panel_x + robot_panel_width, robot_panel_y + robot_panel_height
        ], radius=15, fill=(6, 10, 16), outline=(80, 150, 200), width=2)
        
        # Professional panel header with AI branding
        header_rect = [robot_panel_x, robot_panel_y, 
                      robot_panel_x + robot_panel_width, robot_panel_y + 35]
        
        # Gradient header
        header_gradient_color = (0, 150, 200) if speaking else (80, 120, 150)
        draw.rounded_rectangle(header_rect, radius=15, fill=header_gradient_color)
        draw.rectangle([robot_panel_x, robot_panel_y + 22, 
                       robot_panel_x + robot_panel_width, robot_panel_y + 35], 
                      fill=header_gradient_color)
        
        # AI tutor title
        panel_title = "ElevenLabs AI TUTOR"
        title_bbox = draw.textbbox((0, 0), panel_title, font=tech_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = robot_panel_x + (robot_panel_width - title_width) // 2
        draw.text((title_x, robot_panel_y + 12), panel_title, fill=(255, 255, 255), font=tech_font)
        
        # AI robot avatar with emotion
        robot_y = robot_panel_y + 40
        robot = self.create_advanced_robot_face(speaking=speaking, emotion=emotion)
        
        robot_rgb = Image.new('RGB', robot.size, (6, 10, 16))
        robot_rgb.paste(robot, mask=robot.split()[-1])
        frame.paste(robot_rgb, (robot_panel_x + 15, robot_y))
        
        # Advanced AI status display
        status_y = robot_y + 150
        
        if speaking:
            status_indicators = ["⚡", "🔊", "🤖", "✨"]
            current_indicator = status_indicators[int(time.time() * 4) % len(status_indicators)]
            status_text = f"{current_indicator} GENERATING"
            status_color = (100, 255, 150)
            
            # Add processing animation
            processing_bar_width = robot_panel_width - 30
            processing_progress = (time.time() * 2) % 1
            bar_fill_width = int(processing_bar_width * processing_progress)
            
            bar_y = status_y + 20
            draw.rectangle([robot_panel_x + 15, bar_y, 
                           robot_panel_x + 15 + processing_bar_width, bar_y + 4], 
                          fill=(30, 30, 40))
            if bar_fill_width > 0:
                draw.rectangle([robot_panel_x + 15, bar_y, 
                               robot_panel_x + 15 + bar_fill_width, bar_y + 4], 
                              fill=(0, 200, 100))
        else:
            status_text = "💤 STANDBY"
            status_color = (150, 150, 150)
        
        # Center status text
        status_bbox = draw.textbbox((0, 0), status_text, font=tech_font)
        status_width = status_bbox[2] - status_bbox[0]
        status_x = robot_panel_x + (robot_panel_width - status_width) // 2
        draw.text((status_x, status_y), status_text, fill=status_color, font=tech_font)
        
        # Professional progress system
        if progress > 0:
            # Main progress bar with professional styling
            bar_width = self.width - 80
            bar_height = 10
            bar_x = 40
            bar_y = self.height - 70
            
            # Professional progress bar background
            draw.rounded_rectangle([bar_x - 5, bar_y - 5, bar_x + bar_width + 5, bar_y + bar_height + 5], 
                                 radius=8, fill=(20, 30, 40))
            draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], 
                                 radius=5, fill=(10, 15, 25))
            
            # Dynamic progress fill
            progress_width = int(bar_width * progress)
            if progress_width > 0:
                # Multi-color progress based on completion
                if progress < 0.33:
                    progress_color = (255, 150, 50)  # Orange for beginning
                elif progress < 0.66:
                    progress_color = (255, 200, 50)  # Yellow for middle
                else:
                    progress_color = (50, 255, 150)  # Green for near completion
                
                draw.rounded_rectangle([bar_x, bar_y, bar_x + progress_width, bar_y + bar_height], 
                                     radius=5, fill=progress_color)
                
                # Progress glow effect
                if progress_width > 20:
                    glow_width = min(25, progress_width)
                    glow_color = tuple(int(c * 1.3) if c * 1.3 <= 255 else 255 for c in progress_color)
                    draw.rounded_rectangle([bar_x + progress_width - glow_width, bar_y + 2, 
                                          bar_x + progress_width, bar_y + bar_height - 2], 
                                         radius=3, fill=glow_color)
            
            # Professional progress information
            progress_info = f"TUTORIAL PROGRESS: {progress*100:.1f}% • ElevenLabs AI VOICE"
            draw.text((bar_x, bar_y - 30), progress_info, fill=(120, 180, 255), font=tech_font)
            
            # Technical details
            sections_completed = int(progress * total_sections)
            tech_details = f"SECTIONS: {sections_completed}/{total_sections} • VOICE: AI GENERATED"
            draw.text((bar_x + bar_width - 350, bar_y - 30), tech_details, 
                     fill=(100, 200, 150), font=tech_font)
        
        return frame
    
    def generate_elevenlabs_voice(self, text, filename, voice_type='robotic_friendly'):
        """Generate professional voice using ElevenLabs API"""
        print(f"🎵 Generating ElevenLabs AI voice: {filename.name}")
        
        if not self.api_key:
            print("   ⚠️  No API key - using fallback TTS")
            return self.generate_fallback_voice(text, filename)
        
        try:
            # Get voice configuration
            config = self.voice_configs.get(voice_type, self.voice_configs['robotic_friendly'])
            
            # Prepare text for AI voice generation
            enhanced_text = self.enhance_text_for_ai_voice(text, voice_type)
            
            # ElevenLabs API request
            url = f"{self.base_url}/text-to-speech/{config['voice_id']}"
            
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": self.api_key
            }
            
            data = {
                "text": enhanced_text,
                "model_id": config['model_id'],
                "voice_settings": config['voice_settings']
            }
            
            response = requests.post(url, json=data, headers=headers, timeout=60)
            
            if response.status_code == 200:
                # Save as MP3 first
                temp_mp3 = str(filename).replace('.wav', '.mp3')
                with open(temp_mp3, 'wb') as f:
                    f.write(response.content)
                
                # Convert to WAV and apply robotic effects
                wav_file = str(filename)
                
                # Apply robotic processing with FFmpeg
                robotic_cmd = [
                    'ffmpeg', '-y',
                    '-i', temp_mp3,
                    '-af', 'aecho=0.8:0.88:60:0.4,chorus=0.7:0.9:55:0.4:0.25:2,bass=g=1.1,treble=g=1.4',
                    '-ar', '44100',
                    '-ac', '1',
                    wav_file
                ]
                
                robotic_result = subprocess.run(robotic_cmd, capture_output=True, text=True, timeout=30)
                
                # Clean up temp file
                if os.path.exists(temp_mp3):
                    os.remove(temp_mp3)
                
                if robotic_result.returncode == 0:
                    print(f"   ✅ ElevenLabs AI voice with robotic effects generated")
                    return True
                else:
                    print(f"   ⚠️  Robotic effects failed, using basic conversion")
                    # Fallback: simple conversion
                    simple_cmd = ['ffmpeg', '-y', '-i', temp_mp3, wav_file]
                    subprocess.run(simple_cmd, capture_output=True)
                    return True
            else:
                error_msg = response.json().get('detail', {}).get('message', 'Unknown error')
                print(f"   ❌ ElevenLabs API error: {error_msg}")
                return self.generate_fallback_voice(text, filename)
                
        except Exception as e:
            print(f"   ❌ ElevenLabs generation failed: {e}")
            return self.generate_fallback_voice(text, filename)
    
    def generate_fallback_voice(self, text, filename):
        """Fallback voice generation using system TTS"""
        print(f"   🔄 Using fallback system TTS")
        
        try:
            enhanced_text = self.enhance_text_for_ai_voice(text, 'robotic_technical')
            
            # Use Alex voice with robotic settings
            cmd = [
                'say', '-v', 'Alex', '-r', '165',
                '-o', str(filename), enhanced_text
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                print(f"   ✅ Fallback voice generated")
                return True
            else:
                print(f"   ❌ Fallback voice failed: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"   ❌ Fallback voice error: {e}")
            return False
    
    def enhance_text_for_ai_voice(self, text, voice_type):
        """Enhance text for AI voice generation with robotic characteristics"""
        # Voice-specific enhancements
        if voice_type == 'robotic_friendly':
            replacements = {
                'Welcome to C-Cube': 'Welcome to C-Cube cryptocurrency management system',
                'Hello': 'Greetings',
                'you need to': 'you must',
                'Congratulations!': 'Operation completed successfully',
            }
        elif voice_type == 'robotic_authoritative':
            replacements = {
                'Important': 'Critical information',
                'Warning': 'Security alert',
                'Never': 'Under no circumstances',
                'Don\'t': 'Do not',
            }
        else:  # robotic_technical
            replacements = {
                'This is': 'This system is',
                'you can': 'users can',
                'Let me': 'I will now',
                'simple': 'straightforward',
            }
        
        enhanced_text = text
        for old, new in replacements.items():
            enhanced_text = enhanced_text.replace(old, new)
        
        # Add robotic speech patterns
        enhanced_text = enhanced_text.replace('. ', '... ')
        enhanced_text = enhanced_text.replace('C-Cube', 'C-Cube system')
        enhanced_text = enhanced_text.replace('wallet', 'cryptocurrency wallet')
        
        # Add emphasis for important terms
        enhanced_text = enhanced_text.replace('security', 'security protocols')
        enhanced_text = enhanced_text.replace('recovery phrase', 'recovery phrase sequence')
        
        return enhanced_text
    
    def create_elevenlabs_tutorial_sections(self):
        """Create tutorial sections optimized for ElevenLabs AI voice"""
        sections = [
            {
                "title": "Welcome to C-Cube Cold Wallet",
                "content": "Greetings. I am your artificial intelligence cryptocurrency tutor. Welcome to C-Cube, your advanced secure cold wallet management system. C-Cube provides true cold storage architecture, comprehensive multi-chain network support, intuitive user interface design, military-grade security protocols, and operates as a native desktop application across all platforms.",
                "duration": 12,
                "voice_type": "robotic_friendly",
                "emotion": "excited"
            },
            {
                "title": "Getting Started - First Launch", 
                "content": "Upon initial system activation, you will encounter a security acknowledgment protocol. This is a protective measure, not a warning. The system displays cryptocurrency risk information for your safety. Click 'I Understand and Accept the Risks' to proceed to the main interface. The welcome screen presents two operational modes: 'Setup New Wallet' for first-time users, or 'Access Existing Wallet' for importing existing credentials.",
                "duration": 15,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Creating Your First Wallet",
                "content": "Initiating wallet creation protocol. The system offers two configuration options: Single Network Wallet for optimal beginner experience, or Multi-Chain Wallet for advanced multi-blockchain operations. I recommend initializing with Ethereum network for maximum compatibility. Configure strong password protection to encrypt your private cryptographic keys. Upon completion, the system generates your unique wallet address, private key, and twelve-word recovery phrase sequence.",
                "duration": 18,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Critical Recovery Phrase Security",
                "content": "Critical security protocol alert. Your recovery phrase sequence is the master cryptographic key to all your digital assets. Execute these security procedures immediately: Write the phrase on physical paper using permanent ink. Store in a fireproof security container or safe deposit box. Create multiple backup copies in separate secure locations. Under no circumstances digitize this information. Security violation warnings: Never share with any individual or entity. Never photograph or screenshot. Never store in cloud storage systems. Historical data indicates millions of dollars lost due to inadequate recovery phrase security protocols. Do not become a casualty statistic.",
                "duration": 22,
                "voice_type": "robotic_authoritative",
                "emotion": "serious"
            },
            {
                "title": "Understanding Security Architecture",
                "content": "C-Cube implements a comprehensive four-layer security architecture system. Layer one: Cold storage design maintains offline operation by default, preventing network-based attacks. Layer two: Advanced encryption algorithms protect private key data using military-grade standards. Layer three: Transaction signing requires explicit manual user authorization for every operation. Layer four: Network verification protocols prevent malicious connection attempts. Monitor the visual security indicators throughout the user interface for optimal protection status.",
                "duration": 18,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Managing Multiple Wallet Instances",
                "content": "Advanced users may require multiple wallet instances for specialized cryptocurrency operations. Recommended configuration strategy: Primary wallet for long-term asset storage and security. Trading wallet for active market operations and frequent transactions. Privacy wallet for anonymous transactions and enhanced confidentiality. Create additional wallet instances through the main interface menu and switch between them using the integrated dropdown navigation system.",
                "duration": 16,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Network Selection and Multi-Chain Support",
                "content": "C-Cube supports five major blockchain networks, each with distinct characteristics. Ethereum: Maximum security and compatibility with higher transaction costs. Polygon: Rapid transaction processing with significantly reduced fees. Binance Smart Chain: High-speed operations with minimal cost structure. Arbitrum and Optimism: Advanced Layer 2 scaling solutions for enhanced efficiency. Each network maintains independent balance calculations, token ecosystems, fee structures, and processing speeds. Switch between networks using the integrated network selector interface.",
                "duration": 20,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Executing Your First Transaction",
                "content": "Initiating transaction execution protocol. Pre-flight verification checklist: Confirm sufficient balance including estimated gas fees. Verify recipient address accuracy through multiple verification methods. Validate correct network selection for the intended recipient. Acknowledge transaction irreversibility before proceeding. Complete the transaction form with accurate recipient data and amount. Review all transaction parameters carefully. Execute cryptographic signing process. Broadcast the signed transaction to the blockchain network. Always conduct initial tests with minimal amounts to verify system functionality.",
                "duration": 20,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Understanding Gas Fee Mechanisms",
                "content": "Gas fees function as blockchain network transaction postage and computational resource compensation. Fee calculation variables include: current network congestion levels, transaction computational complexity, and user-selected processing speed preferences. Optimization strategies for cost reduction: Utilize Layer 2 scaling networks when possible. Batch multiple operations into single transactions. Execute transactions during low-traffic time periods. Always verify recipient addresses through multiple independent methods to prevent irreversible asset loss.",
                "duration": 18,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Advanced Token Management",
                "content": "Digital tokens are programmable cryptocurrency assets operating on blockchain platforms through smart contract protocols. Add tokens to your wallet through three methods: integrated token database selection for popular assets, custom contract address input for specialized tokens, or automatic discovery protocols for received tokens. Always verify token legitimacy using official project sources and reputable blockchain explorer services before any interaction. Maintain organized token portfolio structures for optimal asset management.",
                "duration": 16,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Transaction History Analysis",
                "content": "The system maintains comprehensive transaction log databases including all sent transactions, received transfers, token exchange operations, and smart contract interactions. Utilize this historical data for tax documentation requirements, personal budget analysis, and security audit monitoring. Regularly review transaction logs for unauthorized or suspicious activity patterns. Export transaction records for external accounting software integration and regulatory compliance documentation.",
                "duration": 16,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Advanced Feature Access",
                "content": "Power users can access advanced system functionalities including: comprehensive multi-network wallet management, custom gas fee configuration options, transaction data field manipulation capabilities, and direct smart contract interaction protocols. These advanced features enable decentralized finance protocol engagement, custom blockchain operation execution, and sophisticated cryptocurrency management strategies for experienced users with technical expertise.",
                "duration": 16,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Comprehensive Security Best Practices",
                "content": "Implement comprehensive multi-layered security protocols for optimal protection. Physical security measures: strong authentication systems and secure device storage. Digital security protocols: regularly updated operating systems and security software. Operational security procedures: systematic address verification and transaction confirmation processes. Social engineering protection: maintain skeptical verification of all unsolicited communications. Utilize unique strong password generation, professional password management systems, and maintain constant vigilance against fraudulent communication attempts.",
                "duration": 20,
                "voice_type": "robotic_authoritative",
                "emotion": "serious"
            },
            {
                "title": "System Troubleshooting Procedures",
                "content": "Common system operational issues include: wallet access authentication problems, balance display synchronization errors, transaction processing delays, and network connectivity failures. Resolution procedures: Use recovery phrase sequence for wallet access restoration. Verify correct network selection for accurate balance display. Practice patience during blockchain network congestion periods as processing delays are normal. Remember: your cryptocurrency assets remain permanently secure on the blockchain regardless of interface connectivity issues.",
                "duration": 18,
                "voice_type": "robotic_technical",
                "emotion": "neutral"
            },
            {
                "title": "Your C-Cube Journey Initialization Complete",
                "content": "Operation completed successfully. You now possess comprehensive knowledge for secure C-Cube cryptocurrency management system operation. Remember these core operational protocols: Always prioritize security measures above convenience. Adopt incremental learning approaches for complex topics. Maintain continuous information updates about cryptocurrency developments. You are now an active participant in the global financial revolution. Every expert cryptocurrency user began their journey as a novice learner. Welcome to the future of decentralized finance. Your C-Cube operational protocol is now fully active and ready for deployment.",
                "duration": 20,
                "voice_type": "robotic_friendly",
                "emotion": "excited"
            }
        ]
        
        return sections
    
    def create_elevenlabs_tutorial_video(self):
        """Generate professional tutorial video with ElevenLabs AI voice"""
        print("\n🎬 Generating Professional ElevenLabs AI Tutorial Video...")
        
        sections = self.create_elevenlabs_tutorial_sections()
        total_sections = len(sections)
        total_duration = sum(section['duration'] for section in sections)
        
        print(f"📊 Total duration: {total_duration/60:.1f} minutes")
        print(f"🎬 Total sections: {total_sections}")
        print("🎵 Voice: ElevenLabs AI with professional robotic processing")
        
        all_frames = []
        audio_files = []
        
        current_progress = 0
        
        for i, section in enumerate(sections):
            print(f"\n🤖 Section {i+1}/{total_sections}: {section['title']}")
            
            # Generate ElevenLabs AI voice
            audio_file = self.output_dir / f"elevenlabs_section_{i:02d}.wav"
            voice_type = section.get('voice_type', 'robotic_friendly')
            generated_audio = self.generate_elevenlabs_voice(section['content'], audio_file, voice_type)
            
            if generated_audio:
                audio_files.append(str(audio_file))
            
            # Calculate progress
            section_start_progress = current_progress / total_duration
            section_end_progress = (current_progress + section['duration']) / total_duration
            
            # Generate professional frames
            frames_in_section = int(section['duration'] * self.fps)
            emotion = section.get('emotion', 'neutral')
            
            for frame_num in range(frames_in_section):
                frame_progress = frame_num / frames_in_section
                overall_progress = section_start_progress + (section_end_progress - section_start_progress) * frame_progress
                
                # Advanced speaking animation pattern
                speaking_cycle = 40  # Longer cycle for more natural animation
                cycle_pos = frame_num % speaking_cycle
                speaking = cycle_pos < 28  # Speaking 70% of the time
                
                frame = self.create_professional_frame(
                    title=section['title'],
                    content=section['content'],
                    section_num=i+1,
                    total_sections=total_sections,
                    speaking=speaking,
                    progress=overall_progress,
                    emotion=emotion
                )
                
                all_frames.append(frame)
            
            current_progress += section['duration']
            print(f"   ✅ Section {i+1} completed: {frames_in_section} frames generated")
        
        # Save frames with optimization
        print(f"\n💾 Saving {len(all_frames)} professional frames...")
        frames_dir = self.output_dir / "elevenlabs_frames"
        frames_dir.mkdir(exist_ok=True)
        
        for i, frame in enumerate(all_frames):
            if i % 150 == 0:
                print(f"   Processed {i}/{len(all_frames)} frames")
            frame_path = frames_dir / f"frame_{i:05d}.png"
            frame.save(frame_path, "PNG", optimize=True, quality=85)
        
        print("✅ All professional frames saved!")
        
        # Create final video with ElevenLabs audio
        if audio_files:
            # Create audio concatenation list
            audio_list_file = self.output_dir / "elevenlabs_audio_list.txt"
            with open(audio_list_file, 'w') as f:
                for audio_file in audio_files:
                    f.write(f"file '{Path(audio_file).absolute()}'\n")
            
            output_video = self.output_dir / "CCube_Tutorial_ElevenLabs_Professional.mp4"
            
            print("\n🎬 Rendering final professional video with ElevenLabs AI voice...")
            
            video_cmd = [
                'ffmpeg', '-y',
                '-framerate', str(self.fps),
                '-i', str(frames_dir / 'frame_%05d.png'),
                '-f', 'concat', '-safe', '0', '-i', str(audio_list_file),
                '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',  # Higher quality
                '-pix_fmt', 'yuv420p',
                '-c:a', 'aac', '-b:a', '320k',  # High quality audio
                '-shortest',
                str(output_video)
            ]
            
            result = subprocess.run(video_cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Clean up temporary files
                for frame_file in frames_dir.glob("*.png"):
                    frame_file.unlink()
                frames_dir.rmdir()
                
                for audio_file in audio_files:
                    if os.path.exists(audio_file):
                        os.remove(audio_file)
                
                audio_list_file.unlink()
                
                # Get final video statistics
                file_size_mb = output_video.stat().st_size / (1024 * 1024)
                
                print(f"\n🎉 PROFESSIONAL ELEVENLABS AI TUTORIAL COMPLETE!")
                print("=" * 70)
                print(f"📁 Location: {output_video}")
                print(f"📊 File Size: {file_size_mb:.1f} MB")
                print(f"⏱️  Duration: {total_duration/60:.1f} minutes")
                print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
                print(f"🎵 Voice: ElevenLabs AI with professional robotic processing")
                print(f"🎨 Style: Professional tech interface with advanced AI animations")
                print(f"✨ Quality: High-definition with premium audio (320kbps)")
                print("=" * 70)
                print("🚀 Ready for professional cryptocurrency education deployment!")
                
                return output_video
            else:
                print(f"❌ Video creation failed: {result.stderr}")
                return None
        
        return None

def main():
    """Main function to generate ElevenLabs AI tutorial"""
    print("🎬 C-CUBE ELEVENLABS AI TUTORIAL GENERATOR")
    print("🚀 Creating professional AI-powered cryptocurrency education")
    print("=" * 70)
    
    # Check for API key
    api_key = os.getenv('ELEVENLABS_API_KEY')
    if api_key:
        print(f"✅ ElevenLabs API key detected: {api_key[:8]}...")
    else:
        print("⚠️  No ElevenLabs API key found. Will use enhanced system TTS.")
        print("   For best results, set ELEVENLABS_API_KEY environment variable.")
        print("   Get your free API key at: https://elevenlabs.io")
    
    generator = CCubeElevenLabsTutorialGenerator(api_key=api_key)
    result = generator.create_elevenlabs_tutorial_video()
    
    if result:
        print(f"\n🎉 SUCCESS! Opening your professional ElevenLabs AI tutorial...")
        os.system(f"open '{result}'")
        print(f"🤖 Your professional AI-powered tutorial is ready for deployment!")
    else:
        print("\n❌ Failed to create professional tutorial video")

if __name__ == "__main__":
    main()