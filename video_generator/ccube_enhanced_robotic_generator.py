#!/usr/bin/env python3
"""
C-Cube Enhanced Robotic Voice Tutorial Generator
Creates tutorial video with modern robotic voice and conversational tone
"""

import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import time

class CCubeRoboticTutorialGenerator:
    """Generate C-Cube tutorial video with enhanced robotic voice"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        # Video settings
        self.width = 1280
        self.height = 720
        self.fps = 15
        self.robot_color = (0, 204, 51)
        
        print("🤖 C-Cube Enhanced Robotic Voice Tutorial Generator")
        print(f"📁 Output: {self.output_dir}")
        print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
        print("🎵 Voice: Enhanced robotic with conversational tone")
    
    def create_robot_face(self, speaking=False):
        """Create modern robotic face with animations"""
        size = (120, 120)
        img = Image.new('RGBA', size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        center_x, center_y = size[0] // 2, size[1] // 2
        
        # Modern robot head
        head_size = 40
        draw.ellipse([center_x - head_size, center_y - head_size, 
                     center_x + head_size, center_y + head_size], 
                    outline=self.robot_color, width=3, fill=(8, 8, 15))
        
        # LED eyes
        eye_color = (0, 255, 100) if speaking else (0, 180, 80)
        eye_size = 6
        # Left eye
        draw.ellipse([center_x - 20, center_y - 10, center_x - 20 + eye_size, center_y - 10 + eye_size], 
                    fill=eye_color)
        # Right eye
        draw.ellipse([center_x + 14, center_y - 10, center_x + 14 + eye_size, center_y - 10 + eye_size], 
                    fill=eye_color)
        
        # Robotic mouth
        if speaking:
            # Animated bars for speaking
            for i in range(3):
                bar_x = center_x - 10 + i * 7
                bar_height = 4 + int(3 * abs(time.time() * 8 + i) % 1)
                draw.rectangle([bar_x, center_y + 10 - bar_height//2, 
                               bar_x + 4, center_y + 10 + bar_height//2], 
                              fill=(0, 200, 51))
        else:
            # Static line
            draw.rectangle([center_x - 12, center_y + 9, center_x + 12, center_y + 11], 
                          fill=self.robot_color)
        
        # Status antenna
        draw.line([(center_x, center_y - head_size), (center_x, center_y - head_size - 8)], 
                 fill=self.robot_color, width=2)
        status_color = (255, 100, 100) if speaking else (100, 255, 100)
        draw.ellipse([center_x - 3, center_y - head_size - 11, 
                     center_x + 3, center_y - head_size - 5], fill=status_color)
        
        return img
    
    def create_tutorial_frame(self, title, content, section_num, total_sections, speaking=False, progress=0.0):
        """Create tutorial frame with modern design"""
        frame = Image.new('RGB', (self.width, self.height), (5, 5, 12))
        draw = ImageDraw.Draw(frame)
        
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
            content_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
            small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14)
        except:
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        # Header
        header_height = 60
        draw.rectangle([0, 0, self.width, header_height], fill=(15, 15, 25))
        draw.rectangle([0, header_height-2, self.width, header_height], fill=self.robot_color)
        
        # Logo
        draw.text((20, 18), "C-CUBE", fill=self.robot_color, font=title_font)
        draw.text((20, 42), "ROBOTIC TUTORIAL SYSTEM", fill=(100, 150, 100), font=small_font)
        
        # Section info panel
        panel_x = self.width - 280
        draw.rectangle([panel_x, 10, panel_x + 260, 50], fill=(10, 15, 20), width=2)
        draw.text((panel_x + 10, 15), f"SECTION {section_num:02d}/{total_sections:02d}", 
                 fill=(100, 200, 255), font=small_font)
        
        ai_status = "🤖 AI SPEAKING" if speaking else "🤖 AI READY"
        status_color = (255, 80, 80) if speaking else (80, 255, 80)
        draw.text((panel_x + 10, 32), ai_status, fill=status_color, font=small_font)
        
        # Title
        title_y = header_height + 20
        draw.text((20, title_y), title, fill=self.robot_color, font=title_font)
        
        # Content
        content_y = title_y + 40
        words = content.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if len(test_line) < 85:  # Simplified width check
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
        if current_line:
            lines.append(' '.join(current_line))
        
        # Display content lines
        max_lines = (self.height - content_y - 80) // 22
        for i, line in enumerate(lines[:max_lines]):
            if line.strip():
                line_y = content_y + i * 22
                
                # Color coding for different types of content
                if any(term in line.lower() for term in ['security', 'password', 'recovery phrase']):
                    text_color = (255, 200, 100)  # Gold for security
                elif any(term in line.lower() for term in ['c-cube', 'wallet', 'blockchain']):
                    text_color = (100, 255, 150)  # Green for product terms
                else:
                    text_color = (220, 220, 220)  # Standard white
                
                draw.text((20, line_y), line, fill=text_color, font=content_font)
        
        # Robot panel
        robot_panel_x = self.width - 150
        robot_panel_y = 80
        robot_panel_width = 140
        robot_panel_height = 160
        
        draw.rectangle([robot_panel_x, robot_panel_y, 
                       robot_panel_x + robot_panel_width, robot_panel_y + robot_panel_height], 
                      fill=(8, 12, 18), outline=self.robot_color, width=2)
        
        # Panel header
        draw.rectangle([robot_panel_x, robot_panel_y, 
                       robot_panel_x + robot_panel_width, robot_panel_y + 25], fill=self.robot_color)
        draw.text((robot_panel_x + 25, robot_panel_y + 6), "AI TUTOR", fill=(255, 255, 255), font=small_font)
        
        # Robot avatar
        robot = self.create_robot_face(speaking=speaking)
        robot_rgb = Image.new('RGB', robot.size, (8, 12, 18))
        robot_rgb.paste(robot, mask=robot.split()[-1])
        frame.paste(robot_rgb, (robot_panel_x + 10, robot_panel_y + 30))
        
        # Progress bar
        if progress > 0:
            bar_width = self.width - 40
            bar_height = 6
            bar_x = 20
            bar_y = self.height - 40
            
            # Background
            draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], fill=(40, 40, 50))
            
            # Progress
            progress_width = int(bar_width * progress)
            if progress_width > 0:
                draw.rectangle([bar_x, bar_y, bar_x + progress_width, bar_y + bar_height], 
                              fill=self.robot_color)
            
            # Progress text
            progress_text = f"PROGRESS: {progress*100:.1f}%"
            draw.text((bar_x, bar_y - 20), progress_text, fill=(150, 200, 255), font=small_font)
        
        return frame
    
    def generate_enhanced_robotic_voice(self, text, filename):
        """Generate enhanced robotic voice with conversational tone"""
        print(f"🤖 Generating enhanced robotic voice: {filename.name}")
        
        try:
            # Make text more conversational and robotic
            conversational_text = self.make_conversational(text)
            
            # Choose voice based on content
            if any(term in text.lower() for term in ['security', 'warning', 'important']):
                voice = 'Daniel'  # Authoritative
                rate = '160'
            elif any(term in text.lower() for term in ['welcome', 'congratulations']):
                voice = 'Samantha'  # Friendly
                rate = '175'
            else:
                voice = 'Alex'  # Neutral, robotic
                rate = '170'
            
            # Generate audio with improved settings
            cmd = [
                'say', '-v', voice, '-r', rate,
                '-o', str(filename), conversational_text
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0 and filename.exists():
                print(f"   ✅ Enhanced robotic voice generated")
                return True
            else:
                print(f"   ❌ Voice generation failed: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"   ❌ Error generating voice: {e}")
            return False
    
    def make_conversational(self, text):
        """Make text more conversational and robotic"""
        # Robotic conversational replacements
        replacements = {
            'Welcome to C-Cube': 'Greetings. Welcome to C-Cube',
            'Let me': 'I will now',
            'you need to know': 'you must understand',
            'This is like': 'This is similar to',
            "Don't be one of them!": 'Avoid this common error.',
            'Congratulations!': 'Operation successful.',
            'Your journey starts now!': 'Your cryptocurrency management is now active.',
        }
        
        result_text = text
        for old, new in replacements.items():
            result_text = result_text.replace(old, new)
        
        # Add slight pauses for robotic feel
        result_text = result_text.replace('. ', '... ')
        result_text = result_text.replace('security', 'security protocols')
        
        return result_text
    
    def create_tutorial_sections(self):
        """Create tutorial sections with enhanced conversational content"""
        sections = [
            {
                "title": "Welcome to C-Cube Cold Wallet",
                "content": "Greetings. Welcome to C-Cube, your secure cold wallet solution. I am your AI crypto tutor. C-Cube provides true cold storage, multi-chain support, intuitive interface, military-grade security, and operates as a native desktop application.",
                "duration": 10
            },
            {
                "title": "Getting Started - First Launch", 
                "content": "Upon first launch, you will see a security acknowledgment. This protects you. Click 'I Understand and Accept the Risks' to proceed. The welcome screen shows two options: 'Setup New Wallet' for new users, or 'Access Existing Wallet' for importing.",
                "duration": 12
            },
            {
                "title": "Creating Your First Wallet",
                "content": "Select between Single Network Wallet for beginners, or Multi-Chain Wallet for advanced users. I recommend starting with Ethereum. Set a strong password to encrypt your private keys. The system will generate your wallet address, private key, and recovery phrase.",
                "duration": 14
            },
            {
                "title": "The Recovery Phrase Security",
                "content": "Critical: Your recovery phrase is the master key to your assets. Write it on paper. Store in a fireproof safe. Create multiple copies. Never digitize this information. Never share with anyone. Never photograph it. Millions lost due to poor security protocols. Do not become a statistic.",
                "duration": 16
            },
            {
                "title": "Understanding Security Features",
                "content": "C-Cube uses four-layer security. Cold storage keeps you offline by default. Password encryption protects private keys. Transaction signing requires your approval. Network verification prevents malicious connections. Monitor security indicators throughout the interface.",
                "duration": 14
            },
            {
                "title": "Managing Multiple Wallets",
                "content": "Advanced users may need multiple wallets. Recommended setup: Primary wallet for storage, Trading wallet for active use, Privacy wallet for anonymous transactions. Create additional wallets through the interface and switch using the dropdown menu.",
                "duration": 12
            },
            {
                "title": "Network Selection Support",
                "content": "C-Cube supports five major networks. Ethereum offers maximum security with higher fees. Polygon provides fast processing with lower costs. Binance Smart Chain offers high speed with minimal fees. Arbitrum and Optimism provide scaling solutions. Switch networks using the selector.",
                "duration": 14
            },
            {
                "title": "Sending Your First Transaction",
                "content": "Before sending: verify sufficient balance including gas fees, confirm recipient address accuracy, select correct network, acknowledge irreversibility. Fill transaction form, review all details, sign cryptographically, then broadcast. Always test with small amounts first.",
                "duration": 14
            },
            {
                "title": "Understanding Gas Fees",
                "content": "Gas fees are blockchain transaction costs. Variables include network congestion, transaction complexity, and speed preferences. Optimization strategies: use Layer 2 networks, batch operations, transact during low-traffic periods. Always verify addresses to prevent loss.",
                "duration": 12
            },
            {
                "title": "Token Management",
                "content": "Tokens are programmable assets on blockchain platforms. Add tokens through the integrated database, custom contract address, or automatic discovery. Always verify token legitimacy using official sources and blockchain explorers before interaction.",
                "duration": 12
            },
            {
                "title": "Transaction History",
                "content": "The system maintains comprehensive logs including sends, receives, token transfers, and smart contract interactions. Use this data for taxes, budgeting, and security monitoring. Regularly audit for unauthorized activity and export records.",
                "duration": 12
            },
            {
                "title": "Advanced Features",
                "content": "Power users can access advanced features: multi-network management, custom gas configuration, transaction data manipulation, and smart contract interaction. These enable DeFi engagement and custom blockchain operations for experienced users.",
                "duration": 12
            },
            {
                "title": "Security Best Practices",
                "content": "Implement comprehensive security. Physical security with strong authentication. Digital security with updated systems. Operational security through address verification. Social engineering protection via verification. Use unique passwords and password managers.",
                "duration": 14
            },
            {
                "title": "Troubleshooting Common Issues",
                "content": "Common issues include wallet access problems, balance display errors, transaction delays, and network connectivity failures. Solutions: use recovery phrase for access, verify correct network for balances, practice patience during congestion. Your assets remain secure on blockchain.",
                "duration": 14
            },
            {
                "title": "Your C-Cube Journey Begins",
                "content": "Operation successful. You now have comprehensive knowledge for secure C-Cube management. Remember: prioritize security, learn incrementally, stay updated. You are now part of the financial revolution. Every expert started as a beginner. Welcome to the future of finance.",
                "duration": 14
            }
        ]
        
        return sections
    
    def create_enhanced_robotic_tutorial_video(self):
        """Generate tutorial video with enhanced robotic voice"""
        print("\n🤖 Generating Enhanced Robotic C-Cube Tutorial Video...")
        
        sections = self.create_tutorial_sections()
        total_sections = len(sections)
        total_duration = sum(section['duration'] for section in sections)
        
        print(f"📊 Duration: {total_duration/60:.1f} minutes ({total_sections} sections)")
        print("🎵 Voice: Enhanced robotic with conversational elements")
        
        all_frames = []
        audio_files = []
        
        current_progress = 0
        
        for i, section in enumerate(sections):
            print(f"\n🤖 Section {i+1}/{total_sections}: {section['title']}")
            
            # Generate enhanced robotic audio
            audio_file = self.output_dir / f"enhanced_section_{i:02d}.aiff"
            generated_audio = self.generate_enhanced_robotic_voice(section['content'], audio_file)
            if generated_audio:
                audio_files.append(str(audio_file))
            
            # Calculate progress
            section_start_progress = current_progress / total_duration
            section_end_progress = (current_progress + section['duration']) / total_duration
            
            # Generate frames
            frames_in_section = int(section['duration'] * self.fps)
            
            for frame_num in range(frames_in_section):
                frame_progress = frame_num / frames_in_section
                overall_progress = section_start_progress + (section_end_progress - section_start_progress) * frame_progress
                
                # Speaking animation pattern
                speaking_cycle = 30
                cycle_pos = frame_num % speaking_cycle
                speaking = cycle_pos < 20  # Speaking 2/3 of time
                
                frame = self.create_tutorial_frame(
                    title=section['title'],
                    content=section['content'],
                    section_num=i+1,
                    total_sections=total_sections,
                    speaking=speaking,
                    progress=overall_progress
                )
                
                all_frames.append(frame)
            
            current_progress += section['duration']
            print(f"   ✅ Section {i+1} completed: {frames_in_section} frames")
        
        # Save frames efficiently
        print(f"\n💾 Saving {len(all_frames)} frames...")
        frames_dir = self.output_dir / "enhanced_frames"
        frames_dir.mkdir(exist_ok=True)
        
        for i, frame in enumerate(all_frames):
            if i % 200 == 0:
                print(f"   Saved {i}/{len(all_frames)} frames")
            frame_path = frames_dir / f"frame_{i:05d}.png"
            frame.save(frame_path, "PNG", optimize=True)
        
        print("✅ All frames saved!")
        
        # Create final video
        if audio_files:
            # Create audio concatenation list
            audio_list_file = self.output_dir / "enhanced_audio_list.txt"
            with open(audio_list_file, 'w') as f:
                for audio_file in audio_files:
                    f.write(f"file '{Path(audio_file).absolute()}'\n")
            
            output_video = self.output_dir / "CCube_Tutorial_Enhanced_Robotic.mp4"
            
            print("\n🎬 Rendering final video...")
            
            video_cmd = [
                'ffmpeg', '-y',
                '-framerate', str(self.fps),
                '-i', str(frames_dir / 'frame_%05d.png'),
                '-f', 'concat', '-safe', '0', '-i', str(audio_list_file),
                '-c:v', 'libx264', '-preset', 'medium', '-crf', '23',
                '-pix_fmt', 'yuv420p',
                '-c:a', 'aac', '-b:a', '192k',
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
                
                file_size_mb = output_video.stat().st_size / (1024 * 1024)
                
                print(f"\n🎉 ENHANCED ROBOTIC TUTORIAL COMPLETE!")
                print("=" * 50)
                print(f"📁 File: {output_video}")
                print(f"📊 Size: {file_size_mb:.1f} MB")
                print(f"⏱️  Duration: {total_duration/60:.1f} minutes")
                print(f"🤖 Voice: Enhanced robotic with conversational AI")
                print("=" * 50)
                
                return output_video
            else:
                print(f"❌ Video creation failed: {result.stderr}")
                return None
        
        return None

def main():
    """Generate enhanced robotic tutorial"""
    print("🤖 C-CUBE ENHANCED ROBOTIC TUTORIAL GENERATOR")
    print("🚀 Creating modern conversational AI crypto education")
    print("=" * 50)
    
    generator = CCubeRoboticTutorialGenerator()
    result = generator.create_enhanced_robotic_tutorial_video()
    
    if result:
        print(f"\n🎉 Opening your enhanced robotic tutorial...")
        os.system(f"open '{result}'")
    else:
        print("\n❌ Failed to create tutorial video")

if __name__ == "__main__":
    main()