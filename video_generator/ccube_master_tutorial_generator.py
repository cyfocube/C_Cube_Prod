#!/usr/bin/env python3
"""
C-Cube Master Tutorial Video Generator
Creates a comprehensive single video using the complete tutorial guide
with modern robot voice narration and enhanced visuals
"""

import os
import subprocess
import glob
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import time
import json

class CCubeMasterTutorialGenerator:
    """Generate the ultimate C-Cube tutorial video"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        # Video settings - High quality
        self.width = 1920  # 1080p resolution
        self.height = 1080
        self.fps = 30
        self.robot_color = (0, 204, 51)  # C-Cube signature green
        self.accent_color = (51, 153, 255)  # Modern blue accent
        
        print("🎥 C-Cube Master Tutorial Video Generator")
        print(f"📁 Output: {self.output_dir}")
        print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
        print("🎯 Target: Complete user education in one comprehensive video")
    
    def create_advanced_robot_face(self, speaking=False, emotion="neutral", frame_size=(240, 240)):
        """Create advanced animated robot face with emotions"""
        img = Image.new('RGBA', frame_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Robot head with modern design
        margin = 20
        head_size = frame_size[0] - margin * 2
        center_x, center_y = frame_size[0] // 2, frame_size[1] // 2
        
        # Head with gradient effect simulation
        head_rect = [
            center_x - head_size//2, center_y - head_size//2,
            center_x + head_size//2, center_y + head_size//2
        ]
        
        # Multiple layers for depth
        for i in range(3):
            offset = i * 2
            alpha = 50 + i * 20
            draw.rounded_rectangle([
                head_rect[0] + offset, head_rect[1] + offset,
                head_rect[2] - offset, head_rect[3] - offset
            ], radius=25 - i*2, outline=(*self.robot_color, alpha), width=2)
        
        # Main head
        draw.rounded_rectangle(head_rect, radius=25, outline=self.robot_color, width=4, fill=(8, 8, 12))
        
        # Advanced LED-style eyes with emotion
        eye_size = head_size // 7
        eye_y = center_y - head_size // 4
        left_eye_x = center_x - head_size // 4
        right_eye_x = center_x + head_size // 4
        
        # Eye brightness and color based on state
        if speaking:
            eye_brightness = 255
            pulse = int(time.time() * 8) % 2  # Fast pulse when speaking
        else:
            eye_brightness = 200
            pulse = int(time.time() * 2) % 2  # Slow pulse when listening
            
        eye_color = (0, eye_brightness - pulse * 30, 51)
        
        # Eye shapes based on emotion
        if emotion == "excited":
            eye_height = eye_size
        elif emotion == "focused":
            eye_height = eye_size // 2
        else:  # neutral
            eye_height = eye_size * 3 // 4
        
        # Left eye
        draw.rounded_rectangle([
            left_eye_x - eye_size, eye_y - eye_height//2,
            left_eye_x + eye_size, eye_y + eye_height//2
        ], radius=eye_height//2, fill=eye_color)
        
        # Right eye
        draw.rounded_rectangle([
            right_eye_x - eye_size, eye_y - eye_height//2,
            right_eye_x + eye_size, eye_y + eye_height//2
        ], radius=eye_height//2, fill=eye_color)
        
        # Eye pupils for more personality
        pupil_size = eye_size // 3
        pupil_color = (0, 255, 100) if speaking else (0, 200, 80)
        
        draw.ellipse([
            left_eye_x - pupil_size//2, eye_y - pupil_size//2,
            left_eye_x + pupil_size//2, eye_y + pupil_size//2
        ], fill=pupil_color)
        
        draw.ellipse([
            right_eye_x - pupil_size//2, eye_y - pupil_size//2,
            right_eye_x + pupil_size//2, eye_y + pupil_size//2
        ], fill=pupil_color)
        
        # Advanced mouth with different speaking states
        mouth_y = center_y + head_size // 4
        mouth_width = head_size // 2
        
        if speaking:
            # Animated speaking mouth with sound visualization
            mouth_height = head_size // 6 + (int(time.time() * 12) % 3)
            draw.ellipse([
                center_x - mouth_width//2, mouth_y - mouth_height//2,
                center_x + mouth_width//2, mouth_y + mouth_height//2
            ], fill=self.robot_color)
            
            # Sound wave indicators
            for i in range(4):
                wave_x = center_x + mouth_width//2 + 15 + (i * 10)
                wave_size = 2 + i + (int(time.time() * 10 + i) % 3)
                wave_alpha = 255 - i * 40
                wave_color = (0, wave_alpha, 51)
                draw.ellipse([
                    wave_x - wave_size, mouth_y - wave_size,
                    wave_x + wave_size, mouth_y + wave_size
                ], outline=wave_color, width=2)
        else:
            # Subtle smile when not speaking
            mouth_height = 4
            draw.rounded_rectangle([
                center_x - mouth_width//2, mouth_y - mouth_height//2,
                center_x + mouth_width//2, mouth_y + mouth_height//2
            ], radius=mouth_height//2, fill=self.robot_color)
        
        # Status indicator on forehead
        indicator_x = center_x
        indicator_y = center_y - head_size//2 + 15
        indicator_size = 6
        
        if speaking:
            indicator_color = (255, 100, 100)  # Red when speaking
        else:
            indicator_color = (100, 255, 100)  # Green when listening
            
        draw.ellipse([
            indicator_x - indicator_size, indicator_y - indicator_size,
            indicator_x + indicator_size, indicator_y + indicator_size
        ], fill=indicator_color)
        
        # Add subtle antenna
        antenna_x = center_x
        antenna_y = center_y - head_size//2 - 8
        antenna_height = 12
        antenna_color = self.robot_color if speaking else (0, 150, 40)
        
        draw.rounded_rectangle([
            antenna_x - 2, antenna_y - antenna_height,
            antenna_x + 2, antenna_y
        ], radius=2, fill=antenna_color)
        
        # Antenna tip
        draw.ellipse([
            antenna_x - 4, antenna_y - antenna_height - 4,
            antenna_x + 4, antenna_y - antenna_height + 4
        ], fill=(255, 255, 255) if speaking else antenna_color)
        
        return img
    
    def create_master_tutorial_frame(self, title, content, section_number, total_sections, 
                                   robot_speaking=False, progress=0.0, section_progress=0.0, 
                                   key_points=None, visual_elements=None):
        """Create an advanced tutorial frame with enhanced visuals"""
        # Modern dark background with subtle patterns
        frame = Image.new('RGB', (self.width, self.height), (3, 3, 8))
        draw = ImageDraw.Draw(frame)
        
        # Add animated background pattern
        pattern_alpha = 15
        pattern_spacing = 60
        pattern_offset = int(time.time() * 10) % pattern_spacing
        
        for x in range(-pattern_spacing, self.width + pattern_spacing, pattern_spacing):
            for y in range(-pattern_spacing, self.height + pattern_spacing, pattern_spacing):
                adj_x = x + pattern_offset
                adj_y = y + pattern_offset
                if 0 <= adj_x < self.width and 0 <= adj_y < self.height:
                    draw.rectangle([adj_x, adj_y, adj_x + 2, adj_y + 2], 
                                 fill=(pattern_alpha, pattern_alpha, pattern_alpha + 5))
        
        # Load fonts with fallbacks
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 52)
            content_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30)
            section_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
            small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
        except:
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
            section_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        # Enhanced header with branding
        header_height = 140
        # Gradient background simulation
        for i in range(header_height):
            alpha = int(80 * (1 - i / header_height))
            draw.line([(0, i), (self.width, i)], fill=(0, 0, 0, alpha))
        
        # Bottom border
        draw.rectangle([0, header_height-4, self.width, header_height], fill=self.robot_color)
        
        # C-CUBE logo with enhanced styling
        logo_text = "C-CUBE"
        logo_x = 60
        logo_y = 35
        
        # Logo shadow effect
        draw.text((logo_x + 2, logo_y + 2), logo_text, fill=(0, 0, 0), font=title_font)
        draw.text((logo_x, logo_y), logo_text, fill=self.robot_color, font=title_font)
        
        # Subtitle
        subtitle_text = "COLD WALLET TUTORIAL"
        draw.text((logo_x, logo_y + 60), subtitle_text, fill=(150, 150, 150), font=small_font)
        
        # Section information panel
        info_panel_x = self.width - 400
        info_panel_width = 350
        info_panel_height = 100
        
        # Panel background
        draw.rounded_rectangle([
            info_panel_x, 20, 
            info_panel_x + info_panel_width, 20 + info_panel_height
        ], radius=10, fill=(20, 20, 30), outline=(50, 50, 60), width=2)
        
        # Section counter
        section_text = f"SECTION {section_number}/{total_sections}"
        draw.text((info_panel_x + 20, 35), section_text, fill=self.accent_color, font=section_font)
        
        # Status indicator
        status_text = "🔴 LIVE" if robot_speaking else "⚪ READY"
        draw.text((info_panel_x + 20, 65), status_text, fill=(255, 100, 100) if robot_speaking else (100, 200, 100), font=small_font)
        
        # Section progress
        progress_text = f"{section_progress*100:.0f}% COMPLETE"
        draw.text((info_panel_x + 20, 85), progress_text, fill=(200, 200, 200), font=small_font)
        
        # Main title with enhanced styling
        title_y = header_height + 50
        max_title_width = self.width - 400  # Leave space for robot
        
        # Title shadow
        draw.text((62, title_y + 2), title, fill=(0, 0, 0), font=title_font)
        draw.text((60, title_y), title, fill=self.robot_color, font=title_font)
        
        # Content area with better formatting
        content_start_y = title_y + 80
        content_area_width = self.width - 420  # Space for robot and margin
        
        # Split content into paragraphs for better readability
        paragraphs = content.split('. ')
        wrapped_content = []
        
        for paragraph in paragraphs:
            if paragraph.strip():
                paragraph_lines = self.wrap_text(paragraph + '.', content_font, content_area_width)
                wrapped_content.extend(paragraph_lines)
                wrapped_content.append("")  # Add spacing between paragraphs
        
        # Display content with smart truncation
        line_height = 38
        max_lines = (self.height - content_start_y - 200) // line_height
        
        for i, line in enumerate(wrapped_content[:max_lines]):
            if line.strip():  # Skip empty lines for display
                line_y = content_start_y + i * line_height
                
                # Highlight key terms
                display_line = line
                if any(term in line.lower() for term in ['security', 'password', 'recovery phrase', 'private key']):
                    text_color = (255, 200, 100)  # Highlight security terms
                elif any(term in line.lower() for term in ['c-cube', 'wallet', 'blockchain']):
                    text_color = self.robot_color  # Highlight product terms
                else:
                    # Fade effect for readability
                    alpha = 255 if i < max_lines - 5 else max(80, 255 - (i - (max_lines - 5)) * 35)
                    text_color = (alpha, alpha, alpha)
                
                draw.text((60, line_y), display_line, fill=text_color, font=content_font)
        
        # Enhanced robot panel
        robot_panel_x = self.width - 300
        robot_panel_y = 180
        robot_panel_width = 280
        robot_panel_height = 320
        
        # Robot panel with modern design
        draw.rounded_rectangle([
            robot_panel_x, robot_panel_y,
            robot_panel_x + robot_panel_width, robot_panel_y + robot_panel_height
        ], radius=20, fill=(15, 15, 25), outline=self.robot_color, width=3)
        
        # Panel header
        panel_header_height = 40
        draw.rounded_rectangle([
            robot_panel_x, robot_panel_y,
            robot_panel_x + robot_panel_width, robot_panel_y + panel_header_height
        ], radius=20, fill=self.robot_color)
        
        # Panel title
        panel_title = "AI TUTOR"
        title_bbox = draw.textbbox((0, 0), panel_title, font=section_font)
        title_width = title_bbox[2] - title_bbox[0]
        draw.text((robot_panel_x + (robot_panel_width - title_width) // 2, robot_panel_y + 8), 
                 panel_title, fill=(255, 255, 255), font=section_font)
        
        # Robot avatar
        robot_y = robot_panel_y + panel_header_height + 20
        robot = self.create_advanced_robot_face(
            speaking=robot_speaking, 
            emotion="excited" if section_number <= 3 else "focused",
            frame_size=(240, 240)
        )
        
        # Convert and paste robot
        robot_rgb = Image.new('RGB', robot.size, (15, 15, 25))
        robot_rgb.paste(robot, mask=robot.split()[-1])
        frame.paste(robot_rgb, (robot_panel_x + 20, robot_y))
        
        # Robot status
        status_y = robot_y + 250
        robot_status = "EXPLAINING..." if robot_speaking else "LISTENING..."
        status_color = (255, 100, 100) if robot_speaking else (100, 255, 100)
        
        status_bbox = draw.textbbox((0, 0), robot_status, font=small_font)
        status_width = status_bbox[2] - status_bbox[0]
        draw.text((robot_panel_x + (robot_panel_width - status_width) // 2, status_y), 
                 robot_status, fill=status_color, font=small_font)
        
        # Enhanced progress bar system
        if progress > 0:
            # Main progress bar
            main_bar_width = self.width - 120
            main_bar_height = 12
            main_bar_x = 60
            main_bar_y = self.height - 120
            
            # Background with border
            draw.rounded_rectangle([
                main_bar_x - 2, main_bar_y - 2,
                main_bar_x + main_bar_width + 2, main_bar_y + main_bar_height + 2
            ], radius=main_bar_height//2 + 2, fill=(50, 50, 60))
            
            draw.rounded_rectangle([
                main_bar_x, main_bar_y,
                main_bar_x + main_bar_width, main_bar_y + main_bar_height
            ], radius=main_bar_height//2, fill=(25, 25, 35))
            
            # Progress fill with gradient effect
            progress_width = int(main_bar_width * progress)
            if progress_width > 0:
                draw.rounded_rectangle([
                    main_bar_x, main_bar_y,
                    main_bar_x + progress_width, main_bar_y + main_bar_height
                ], radius=main_bar_height//2, fill=self.robot_color)
                
                # Highlight effect
                highlight_width = min(20, progress_width)
                draw.rounded_rectangle([
                    main_bar_x + progress_width - highlight_width, main_bar_y + 2,
                    main_bar_x + progress_width, main_bar_y + main_bar_height - 2
                ], radius=main_bar_height//2 - 2, fill=(100, 255, 150))
            
            # Progress text
            progress_text = f"OVERALL PROGRESS: {progress*100:.1f}%"
            draw.text((main_bar_x, main_bar_y - 30), progress_text, fill=(200, 200, 200), font=small_font)
            
            # Section progress bar
            section_bar_y = main_bar_y + 30
            section_bar_height = 6
            
            draw.rounded_rectangle([
                main_bar_x, section_bar_y,
                main_bar_x + main_bar_width, section_bar_y + section_bar_height
            ], radius=section_bar_height//2, fill=(40, 40, 50))
            
            section_progress_width = int(main_bar_width * section_progress)
            if section_progress_width > 0:
                draw.rounded_rectangle([
                    main_bar_x, section_bar_y,
                    main_bar_x + section_progress_width, section_bar_y + section_bar_height
                ], radius=section_bar_height//2, fill=self.accent_color)
            
            # Section progress text
            section_text = f"SECTION PROGRESS: {section_progress*100:.0f}%"
            draw.text((main_bar_x, section_bar_y + 15), section_text, fill=(150, 150, 150), font=small_font)
        
        # Key points panel (if provided)
        if key_points and len(key_points) > 0:
            points_panel_x = 60
            points_panel_y = self.height - 280
            points_panel_width = min(500, self.width - 400)
            
            draw.rounded_rectangle([
                points_panel_x, points_panel_y,
                points_panel_x + points_panel_width, points_panel_y + 100
            ], radius=10, fill=(20, 25, 35), outline=(80, 80, 90), width=1)
            
            draw.text((points_panel_x + 15, points_panel_y + 10), "KEY POINTS:", 
                     fill=self.accent_color, font=small_font)
            
            for i, point in enumerate(key_points[:3]):  # Max 3 points
                point_y = points_panel_y + 35 + i * 20
                draw.text((points_panel_x + 15, point_y), f"• {point}", 
                         fill=(200, 200, 200), font=small_font)
        
        return frame
    
    def wrap_text(self, text, font, max_width):
        """Wrap text to fit within max_width with improved word breaking"""
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
                    # Handle very long words
                    if len(word) > 30:
                        lines.append(word[:30] + "...")
                    else:
                        lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def generate_premium_voice_audio(self, text, filename, voice_style="modern"):
        """Generate premium quality robot voice with modern TTS"""
        print(f"🎤 Generating premium voice: {filename}")
        
        try:
            # Enhanced voice generation with multiple options
            if voice_style == "modern":
                # Use more advanced voices available on macOS
                voices = ['Samantha', 'Alex', 'Victoria', 'Daniel', 'Karen']
                voice = voices[hash(text) % len(voices)]
                rate = '185'  # Slightly faster for engagement
            else:
                voice = 'Alex'
                rate = '180'
            
            # Generate base audio
            temp_file = str(filename).replace('.wav', '_temp.wav')
            
            cmd = [
                'say', '-v', voice, '-r', rate,
                '--quality=127',  # Highest quality
                '-o', temp_file, text
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Apply audio effects for robot voice using FFmpeg
                effects_cmd = [
                    'ffmpeg', '-y',
                    '-i', temp_file,
                    '-af', 'aecho=0.8:0.88:60:0.4,aecho=0.8:0.88:120:0.3,bass=g=2,treble=g=1.5',
                    '-ar', '44100',
                    '-ac', '2',
                    str(filename)
                ]
                
                effects_result = subprocess.run(effects_cmd, capture_output=True, text=True)
                
                # Clean up temp file
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                
                if effects_result.returncode == 0:
                    print(f"   ✅ Premium voice with effects generated")
                    return True
                else:
                    # Fallback to basic voice if effects fail
                    os.rename(temp_file, str(filename))
                    print(f"   ⚠️  Basic voice generated (effects failed)")
                    return True
            else:
                print(f"   ❌ Voice generation failed: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"   ❌ Error generating voice: {e}")
            return False
    
    def create_comprehensive_tutorial_sections(self):
        """Create the complete tutorial sections with enhanced content"""
        sections = [
            {
                "title": "Welcome to C-Cube Cold Wallet",
                "content": "Hey there! Welcome to C-Cube, your new secure cold wallet companion. I'm here to guide you through everything you need to know about managing your cryptocurrency safely and efficiently. Think of me as your personal crypto tutor - I'll explain everything step by step, answer your questions, and make sure you're confident using every feature. C-Cube is different from other wallets because it offers true cold storage where your private keys never touch the internet, multi-chain support for multiple networks, a user-friendly cyber-themed interface, advanced security with password encryption, and it runs as a native desktop application on Windows, Mac, and Linux.",
                "duration": 18,
                "key_points": ["True cold storage security", "Multi-chain support", "Desktop application"],
                "emotion": "excited"
            },
            {
                "title": "Getting Started - Your First Launch",
                "content": "When you first open C-Cube, you'll see a security prompt. Don't worry - this isn't scary, it's protective! You'll see a warning about the risks of cryptocurrency. This isn't meant to scare you, but to ensure you understand the responsibility. Click 'I Understand and Accept the Risks' to continue. Think of this like signing a waiver before rock climbing - you need to know what you're getting into. Next, you'll see our beautiful welcome screen with the C-Cube logo. This is your gateway to secure crypto management. You'll have two main options: 'Setup New Wallet' for newcomers to crypto or C-Cube, or 'Access Existing Wallet' if you already have a wallet you want to import.",
                "duration": 20,
                "key_points": ["Security acknowledgment", "Welcome screen options", "Setup vs Import"],
                "emotion": "focused"
            },
            {
                "title": "Creating Your First Wallet",
                "content": "Alright, let's create your first wallet! This is like opening your first bank account, but way cooler because you're in complete control. When you click 'Setup New Wallet,' you'll see options for different wallet types. Single Network Wallet is perfect for beginners - tied to one specific blockchain like Ethereum, simpler to manage, and great for learning the ropes. Multi-Chain Wallet is for the ambitious - works across all supported networks, more advanced but more flexible, ideal once you're comfortable with crypto. My recommendation: Start with a single network wallet on Ethereum. You can always create more wallets later! Next comes password protection, which is highly recommended. Use a password to encrypt your private key on your device. Choose something memorable but not obvious, at least 8 characters with numbers and symbols.",
                "duration": 25,
                "key_points": ["Single vs Multi-chain wallets", "Password protection", "Start with Ethereum"],
                "emotion": "excited"
            },
            {
                "title": "The Sacred Recovery Phrase",
                "content": "Let me be crystal clear about this: Your recovery phrase is the master key to your cryptocurrency. Once created, C-Cube will show you three critical pieces of information: your wallet address like your crypto email address, your private key which is the secret that controls your funds and you must NEVER share this, and your recovery phrase of 12 words that can restore your wallet. Here's what you absolutely must do: Write it down on paper immediately, store it in a fireproof safe, make multiple copies in different locations, never store it digitally with no screenshots or cloud storage, and test your backup by restoring it on a test device. Never do this: Share it with anyone, store it on your computer or phone, take a photo of it, email it to yourself, or store it in the cloud. Real talk: People have lost millions of dollars by not properly securing their recovery phrase. Don't be one of them!",
                "duration": 22,
                "key_points": ["Write on paper immediately", "Store in fireproof safe", "Never share with anyone"],
                "emotion": "focused"
            },
            {
                "title": "Understanding Security Features",
                "content": "C-Cube has several layers of security. Let me walk you through each one so you understand how your funds are protected. Layer 1 is Cold Storage Design - your wallet operates offline by default, and even if your computer is compromised, your keys aren't accessible to hackers. You only go 'online' when you specifically choose to broadcast a transaction. Layer 2 is Password Encryption - your private key is encrypted with your password, so even if someone accesses your computer, they can't use your wallet without the password. Stronger password equals stronger protection. Layer 3 is Transaction Signing - every transaction must be manually signed by you, so no transaction can happen without your explicit approval. Always verify the details before signing! Layer 4 is Network Verification - C-Cube verifies you're connecting to legitimate networks, preventing connection to malicious fake networks. Trust the wallet's network selection.",
                "duration": 25,
                "key_points": ["Four security layers", "Cold storage design", "Manual transaction signing"],
                "emotion": "focused"
            },
            {
                "title": "Managing Multiple Wallets",
                "content": "As you grow in your crypto journey, you'll likely want multiple wallets for different purposes. C-Cube makes this easy! Think of wallets like different pockets in your jacket: Main Wallet for your primary savings where you keep most funds, Trading Wallet for active trading with smaller amounts, Privacy Wallet for anonymous transactions, and Network-Specific Wallets with one for each blockchain you use. Creating additional wallets is simple from the main interface. Look for the plus or 'Add Wallet' button, choose between creating new or importing existing, follow the same process as your first wallet, and each wallet gets its own unique address and keys. Switching between wallets is easy with the wallet dropdown in the top navigation. C-Cube shows you which wallet is currently active, and each wallet displays its balance and network.",
                "duration": 22,
                "key_points": ["Multiple wallet purposes", "Easy wallet switching", "Unique addresses per wallet"],
                "emotion": "neutral"
            },
            {
                "title": "Network Selection and Multi-Chain Support",
                "content": "One of C-Cube's superpowers is supporting multiple blockchain networks. Think of blockchain networks like different countries with their own currencies. Ethereum is the original smart contract platform with highest security but higher fees, best for large transactions and important DeFi operations. Polygon is Ethereum's faster, cheaper cousin with same functionality and lower cost, best for daily transactions, gaming, and NFTs. Binance Smart Chain offers high speed and low cost, popular for trading, best for DeFi farming and fast transactions. Arbitrum is an Ethereum scaling solution with lower fees than main Ethereum, best for DeFi with Ethereum security. Optimism is another Ethereum scaling solution using optimistic rollup technology, best for Ethereum apps with lower costs. Each network has different balances, tokens, transaction fees, and speeds. What changes when you switch networks: balances show different amounts, different tokens are available, transaction costs vary significantly, and some networks are faster than others.",
                "duration": 28,
                "key_points": ["5 supported networks", "Different fees and speeds", "Same wallet, different balances"],
                "emotion": "excited"
            },
            {
                "title": "Sending Your First Transaction",
                "content": "Now for the exciting part - actually using your cryptocurrency! Sending transactions is like writing digital checks, but with superpowers. Before you send your first transaction, follow this pre-flight checklist: Verify you have enough balance including gas fees, double-check the recipient address, confirm you're on the correct network, understand the transaction will be irreversible, and have your wallet password ready if encrypted. There are three types of transactions: Native Coin Transfers for sending ETH, MATIC, BNB which is the simplest type, Token Transfers for sending ERC-20 and BEP-20 tokens which requires token contract address but still pays gas fees in native coin, and Smart Contract Interactions for more complex transactions like interacting with DeFi protocols with custom data fields. The step-by-step process: Fill out the form by selecting transaction type and choosing recipient, review transaction details and verify all information, sign the transaction by entering your wallet password, then broadcast by choosing when to send it to the network.",
                "duration": 28,
                "key_points": ["Pre-flight checklist", "Three transaction types", "Review before signing"],
                "emotion": "excited"
            },
            {
                "title": "Understanding Gas Fees",
                "content": "Gas fees are like postage stamps for the blockchain. You pay miners or validators to process your transaction. Factors affecting gas fees include network congestion where more users equals higher fees, transaction complexity where simple sends cost less than complex smart contract interactions, and speed preference where you pay more for faster confirmation. Gas fee tips to save money: Check current network fees before sending, consider using Layer 2 networks for lower fees, batch multiple transactions when possible, and send during off-peak hours for lower fees. Recipient address safety follows the golden rule: Always verify recipient addresses! Use safe methods to get addresses like copying from the recipient's official wallet, using QR code scanning when available, selecting from your own wallets in C-Cube, or copying from verified exchange withdrawal pages. Red flags include addresses sent via email or text, addresses from unverified sources, addresses that look similar but not identical, and pressure to send quickly without verification.",
                "duration": 25,
                "key_points": ["Gas fees like postage", "Layer 2 for lower fees", "Always verify addresses"],
                "emotion": "focused"
            },
            {
                "title": "Token Management Made Easy",
                "content": "Tokens are like apps on your phone - they run on the blockchain platform and give you additional functionality. C-Cube makes managing tokens incredibly easy. Tokens are digital assets that run on existing blockchains, like having different types of gift cards that all work in the same mall. Each token has its own purpose, value, and community. Common token standards include ERC-20 for Ethereum which is the most common, BEP-20 for Binance Smart Chain tokens, and your wallet address works across compatible networks with the same format but different networks. You can add tokens three ways: From the Token Database by browsing popular tokens for your current network, Custom Token Addition by finding the token's contract address from official sources, or Auto-Discovery where C-Cube can scan your wallet for tokens and automatically finds tokens you've received. Always verify token legitimacy by checking the contract address against official sources, verifying on block explorers like Etherscan or BSCScan, cross-referencing with official websites, and being wary of tokens with similar names.",
                "duration": 26,
                "key_points": ["Tokens like apps", "Three ways to add tokens", "Always verify legitimacy"],
                "emotion": "neutral"
            },
            {
                "title": "Transaction History and Monitoring",
                "content": "Your transaction history is like your crypto bank statement - it tells the story of your digital financial journey. C-Cube makes it easy to track and understand your transactions. Your transaction history records every transaction you send or receive, token transfers and exchanges, smart contract interactions, and even failed transactions because these matter too. Transaction details shown include date and time when it occurred, type whether send, receive, token transfer or contract interaction, amount that was transferred, recipient or sender who was involved, transaction hash as unique identifier on blockchain, status whether confirmed, pending or failed, and gas fees that you paid. Use transaction history for tax purposes by exporting regularly and keeping records of purchase prices and dates, for budgeting by monitoring spending patterns and tracking gas fee expenses, and for security by regularly reviewing for unauthorized transactions and monitoring for unexpected incoming transactions.",
                "duration": 24,
                "key_points": ["Complete transaction record", "Tax and budgeting tool", "Security monitoring"],
                "emotion": "focused"
            },
            {
                "title": "Advanced Features for Power Users",
                "content": "Ready to level up? Let's explore C-Cube's advanced features that give you more control and flexibility over your crypto management. Multi-Network Wallet Management lets you seamlessly move between networks with the same wallet, understand how the same address works across compatible networks, manage different balances on different networks, and optimize for gas fees across networks. Advanced Transaction Features include Custom Gas Fee Settings to override automatic gas calculations and set custom gas price and limit, Transaction Data Fields to add custom data and interact with smart contracts directly, and Batch Transaction Planning to plan multiple transactions in sequence and optimize gas usage. Wallet Security Advanced Options include understanding encrypted versus unencrypted storage implications, choosing appropriate security level for your use case, private key management for exporting keys securely, and recovery and backup strategies with multiple backup copies and tested recovery procedures.",
                "duration": 26,
                "key_points": ["Multi-network management", "Custom gas settings", "Advanced security options"],
                "emotion": "focused"
            },
            {
                "title": "Security Best Practices",
                "content": "Security isn't just a feature - it's a mindset. Let me share the most important practices to keep your crypto safe. Follow the security hierarchy: Level 1 Physical Security with secure computer passwords, encrypted storage, recovery phrase in fireproof safe, and never leaving wallet open on shared computers. Level 2 Digital Security with strong unique passwords, two-factor authentication where possible, updated operating system, and antivirus software. Level 3 Operational Security by verifying all addresses before sending, starting with small test transactions, never sharing private keys or recovery phrases, and being skeptical of unsolicited contact. Level 4 Social Engineering Protection by never giving wallet information over the phone, ignoring urgent requests for private keys, verifying support contacts through official channels, and trusting but verifying all wallet-related communications. Password security for C-Cube requires minimum 12 characters with mix of uppercase, lowercase, numbers and symbols, avoiding dictionary words, not reusing passwords from other accounts, and using a reputable password manager.",
                "duration": 28,
                "key_points": ["Four security levels", "Strong password practices", "Beware social engineering"],
                "emotion": "focused"
            },
            {
                "title": "Troubleshooting Common Issues",
                "content": "Even the best wallet users encounter issues sometimes. Here's your guide to solving the most common problems quickly and safely. For wallet access issues like 'I can't access my wallet,' possible causes and solutions include: If you forgot your password, use your recovery phrase to restore the wallet and create a new password during restoration. If your recovery phrase isn't working, check word spelling and order carefully, ensure you're using the correct number of words, and verify you're restoring to the same wallet type. If your wallet isn't showing, check if you're on the correct network, verify wallet selection in the interface, and look for wallet in multi-chain view. For balance and display issues like 'My balance shows zero' or 'Tokens are missing,' diagnostic steps include network verification to confirm you're viewing the correct network, token addition by manually adding missing tokens using contract addresses, and synchronization issues by refreshing the wallet interface and checking internet connection. Stay calm - your funds are safe on the blockchain, verify you have correct recovery information, and try wallet restoration process.",
                "duration": 26,
                "key_points": ["Stay calm, funds are safe", "Recovery phrase solutions", "Network verification"],
                "emotion": "focused"
            },
            {
                "title": "Your C-Cube Journey Begins Now",
                "content": "Congratulations! You've just completed a comprehensive tour of C-Cube Cold Wallet. You now have the knowledge to safely and confidently manage your cryptocurrency assets. Throughout this guide, you've mastered creating and securing your first wallet, understanding multi-network support, sending and receiving transactions safely, managing tokens across different blockchains, implementing advanced security practices, troubleshooting common issues, and using advanced features for power users. Remember the golden rules: Security first by never sharing your private keys or recovery phrase, always verifying transaction details before signing, keeping backups secure and accessible, and staying skeptical of unsolicited communications. Start small by beginning with small transactions to learn, gradually increasing amounts as confidence grows, testing new features with minimal risk, and learning from every transaction. Stay informed by following official C-Cube updates, understanding the networks you're using, keeping up with security best practices, and engaging with the community responsibly. Cryptocurrency and blockchain technology represent the future of finance. By using C-Cube, you're participating in a financial revolution that puts control back in your hands. Welcome to the future of finance. Welcome to C-Cube. Your journey starts now!",
                "duration": 30,
                "key_points": ["Journey complete", "Golden rules mastered", "Financial revolution begins"],
                "emotion": "excited"
            }
        ]
        
        return sections
    
    def create_master_tutorial_video(self):
        """Generate the ultimate C-Cube tutorial video"""
        print("\n🚀 Generating C-Cube Master Tutorial Video...")
        print("🎯 Creating comprehensive cryptocurrency education experience")
        
        sections = self.create_comprehensive_tutorial_sections()
        total_sections = len(sections)
        all_frames = []
        all_audio_files = []
        
        # Calculate total duration
        total_duration = sum(section['duration'] for section in sections)
        print(f"📊 Total video duration: {total_duration/60:.1f} minutes")
        print(f"🎬 Estimated frames: {total_duration * self.fps:,}")
        
        # Create frames and audio for each section
        current_progress = 0
        
        for i, section in enumerate(sections):
            print(f"\n📹 Creating Section {i+1}/{total_sections}: {section['title']}")
            print(f"   ⏱️  Duration: {section['duration']} seconds")
            
            # Generate premium audio
            audio_file = self.output_dir / f"master_section_{i:02d}.wav"
            self.generate_premium_voice_audio(section['content'], audio_file, "modern")
            if audio_file.exists():
                all_audio_files.append(audio_file)
            
            # Calculate progress
            section_start_progress = current_progress / total_duration
            section_end_progress = (current_progress + section['duration']) / total_duration
            
            # Generate frames for this section
            frames_in_section = int(section['duration'] * self.fps)
            
            for frame_num in range(frames_in_section):
                frame_progress_in_section = frame_num / frames_in_section
                overall_progress = section_start_progress + (section_end_progress - section_start_progress) * frame_progress_in_section
                
                # Advanced speaking animation pattern
                cycle_length = 90  # Frames per speaking cycle
                cycle_position = frame_num % cycle_length
                speaking = cycle_position < 60  # Speaking for 2/3 of cycle
                
                frame = self.create_master_tutorial_frame(
                    title=section['title'],
                    content=section['content'],
                    section_number=i+1,
                    total_sections=total_sections,
                    robot_speaking=speaking,
                    progress=overall_progress,
                    section_progress=frame_progress_in_section,
                    key_points=section.get('key_points', [])
                )
                
                all_frames.append(frame)
                
                # Progress indicator
                if frame_num % 150 == 0:  # Every 5 seconds
                    frames_completed = len(all_frames)
                    total_estimated_frames = total_duration * self.fps
                    completion_pct = (frames_completed / total_estimated_frames) * 100
                    print(f"      🎬 Progress: {completion_pct:.1f}% ({frames_completed:,} frames)")
            
            current_progress += section['duration']
            print(f"   ✅ Section {i+1} completed: {len(all_frames):,} total frames")
        
        print(f"\n🎬 Creating master video with {len(all_frames):,} frames...")
        print(f"💾 Estimated file operations: {len(all_frames)} frame saves + audio processing")
        
        # Save frames with progress tracking
        temp_dir = Path("temp_master_frames")
        temp_dir.mkdir(exist_ok=True)
        
        print("   💾 Saving frames to disk...")
        batch_size = 500
        for batch_start in range(0, len(all_frames), batch_size):
            batch_end = min(batch_start + batch_size, len(all_frames))
            print(f"      Saving batch {batch_start//batch_size + 1}: frames {batch_start}-{batch_end}")
            
            for i in range(batch_start, batch_end):
                frame_path = temp_dir / f"frame_{i:07d}.png"
                all_frames[i].save(frame_path, "PNG", optimize=True)
        
        # Combine all audio files with crossfade
        print("   🎵 Processing audio tracks...")
        combined_audio = self.output_dir / "master_tutorial_audio.wav"
        
        if all_audio_files:
            # Create audio list with crossfade for smooth transitions
            audio_list_file = self.output_dir / "master_audio_files.txt"
            with open(audio_list_file, 'w') as f:
                for audio_file in all_audio_files:
                    f.write(f"file '{audio_file.absolute()}'\n")
            
            # Concatenate with crossfade
            concat_cmd = [
                'ffmpeg', '-y', '-f', 'concat', '-safe', '0',
                '-i', str(audio_list_file),
                '-af', 'acrossfade=d=0.5',  # 0.5 second crossfade
                str(combined_audio)
            ]
            
            print("      🎵 Concatenating audio files...")
            result = subprocess.run(concat_cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print("      ✅ Audio processing complete")
            
            audio_list_file.unlink()  # Clean up
        
        # Create final high-quality video
        output_video = self.output_dir / "CCube_Master_Tutorial_Complete.mp4"
        
        print("   🎥 Rendering final master video...")
        print("      This may take several minutes for optimal quality...")
        
        video_cmd = [
            'ffmpeg', '-y',
            '-framerate', str(self.fps),
            '-i', str(temp_dir / 'frame_%07d.png'),
            '-i', str(combined_audio) if combined_audio.exists() else '/dev/null',
            '-c:v', 'libx264',
            '-preset', 'slow',  # Higher quality preset
            '-crf', '18',  # Higher quality (lower CRF)
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-b:a', '256k',  # Higher audio bitrate
            '-r', str(self.fps),
            '-movflags', '+faststart',  # Optimize for streaming
            '-shortest',
            str(output_video)
        ]
        
        result = subprocess.run(video_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Clean up temporary files
            print("   🧹 Cleaning up temporary files...")
            frame_count = 0
            for frame_file in temp_dir.glob("*.png"):
                frame_file.unlink()
                frame_count += 1
            temp_dir.rmdir()
            
            # Clean up individual audio files
            for audio_file in all_audio_files:
                audio_file.unlink()
            if combined_audio.exists():
                combined_audio.unlink()
            
            # Get final video statistics
            file_size_mb = output_video.stat().st_size / (1024 * 1024)
            duration_minutes = total_duration / 60
            
            print(f"\n🏆 MASTER TUTORIAL VIDEO COMPLETE!")
            print("=" * 60)
            print(f"📁 Location: {output_video}")
            print(f"📊 File Size: {file_size_mb:.1f} MB")
            print(f"⏱️  Duration: {duration_minutes:.1f} minutes ({total_duration} seconds)")
            print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
            print(f"🎵 Audio: Premium robot voice with sound effects")
            print(f"🤖 Features: Advanced AI tutor, progress tracking, modern UI")
            print(f"📚 Content: Complete C-Cube user education guide")
            print(f"🎯 Sections: {total_sections} comprehensive tutorials")
            print(f"🎨 Frames: {frame_count:,} individually crafted frames")
            print("=" * 60)
            print("✨ Ready for professional cryptocurrency education!")
            
            return output_video
        else:
            print(f"❌ Video creation failed: {result.stderr}")
            return None

def main():
    """Main function to generate the master tutorial"""
    print("🎬 C-CUBE MASTER TUTORIAL GENERATOR")
    print("🚀 Creating the ultimate cryptocurrency education video")
    print("=" * 60)
    
    generator = CCubeMasterTutorialGenerator()
    result = generator.create_master_tutorial_video()
    
    if result:
        print(f"\n🎉 SUCCESS! Opening your master tutorial video...")
        # Open the video file
        os.system(f"open '{result}'")
        print(f"🎯 Your comprehensive C-Cube tutorial is ready!")
        print(f"💡 Share this video to educate users about secure cryptocurrency management")
    else:
        print("\n❌ Failed to create master tutorial video")
        print("💡 Check the error messages above for troubleshooting")

if __name__ == "__main__":
    main()