#!/usr/bin/env python3
"""
C-Cube Complete Tutorial Video Generator
Creates a single comprehensive video using the full tutorial guide
"""

import os
import subprocess
import glob
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import time

class CompleteTutorialGenerator:
    """Generate a complete C-Cube tutorial video"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        # Video settings
        self.width = 1920  # 1080p resolution
        self.height = 1080
        self.fps = 30
        self.robot_color = (0, 204, 51)  # C-Cube green
        
        print("🎥 C-Cube Complete Tutorial Video Generator")
        print(f"📁 Output: {self.output_dir}")
        print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
    
    def create_modern_robot_face(self, speaking=False, frame_size=(200, 200)):
        """Create modern animated robot face"""
        img = Image.new('RGBA', frame_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Robot head (rounded rectangle for modern look)
        margin = 15
        head_size = frame_size[0] - margin * 2
        center_x, center_y = frame_size[0] // 2, frame_size[1] // 2
        
        # Head outline with rounded corners
        head_rect = [
            center_x - head_size//2, center_y - head_size//2,
            center_x + head_size//2, center_y + head_size//2
        ]
        
        # Draw head background
        draw.rounded_rectangle(head_rect, radius=20, outline=self.robot_color, width=4, fill=(15, 15, 15))
        
        # Modern LED-style eyes
        eye_size = head_size // 8
        eye_y = center_y - head_size // 4
        left_eye_x = center_x - head_size // 4
        right_eye_x = center_x + head_size // 4
        
        # Animated eyes (brighter when speaking)
        eye_brightness = 255 if speaking else 180
        eye_color = (0, eye_brightness, 51)
        
        # Left eye
        draw.rounded_rectangle([
            left_eye_x - eye_size, eye_y - eye_size//2,
            left_eye_x + eye_size, eye_y + eye_size//2
        ], radius=eye_size//2, fill=eye_color)
        
        # Right eye
        draw.rounded_rectangle([
            right_eye_x - eye_size, eye_y - eye_size//2,
            right_eye_x + eye_size, eye_y + eye_size//2
        ], radius=eye_size//2, fill=eye_color)
        
        # Modern mouth with speaking animation
        mouth_y = center_y + head_size // 4
        mouth_width = head_size // 2
        
        if speaking:
            # Animated speaking mouth (oval)
            mouth_height = head_size // 8
            draw.ellipse([
                center_x - mouth_width//2, mouth_y - mouth_height//2,
                center_x + mouth_width//2, mouth_y + mouth_height//2
            ], fill=self.robot_color)
            
            # Add sound wave indicators
            for i in range(3):
                wave_x = center_x + mouth_width//2 + 10 + (i * 8)
                wave_size = 3 + i * 2
                draw.ellipse([
                    wave_x - wave_size, mouth_y - wave_size,
                    wave_x + wave_size, mouth_y + wave_size
                ], outline=self.robot_color, width=2)
        else:
            # Closed mouth (line)
            mouth_height = 3
            draw.rounded_rectangle([
                center_x - mouth_width//2, mouth_y - mouth_height//2,
                center_x + mouth_width//2, mouth_y + mouth_height//2
            ], radius=mouth_height//2, fill=self.robot_color)
        
        # Add modern antenna/indicator
        antenna_x = center_x
        antenna_y = center_y - head_size//2 - 5
        antenna_size = 4
        antenna_color = (0, 255, 51) if speaking else (0, 180, 51)
        
        draw.ellipse([
            antenna_x - antenna_size, antenna_y - antenna_size,
            antenna_x + antenna_size, antenna_y + antenna_size
        ], fill=antenna_color)
        
        return img
    
    def create_tutorial_frame(self, title, content, section_number, total_sections, robot_speaking=False, progress=0.0):
        """Create a modern tutorial frame"""
        # Create background with gradient effect
        frame = Image.new('RGB', (self.width, self.height), (5, 5, 10))
        draw = ImageDraw.Draw(frame)
        
        # Add subtle grid pattern
        grid_spacing = 50
        grid_color = (15, 15, 20)
        for x in range(0, self.width, grid_spacing):
            draw.line([(x, 0), (x, self.height)], fill=grid_color, width=1)
        for y in range(0, self.height, grid_spacing):
            draw.line([(0, y), (self.width, y)], fill=grid_color, width=1)
        
        # Load fonts
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
            content_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
            section_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        except:
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
            section_font = ImageFont.load_default()
        
        # Header section with C-Cube branding
        header_height = 120
        draw.rectangle([0, 0, self.width, header_height], fill=(0, 0, 0))
        draw.rectangle([0, header_height-3, self.width, header_height], fill=self.robot_color)
        
        # C-Cube logo area
        logo_text = "C-CUBE"
        logo_bbox = draw.textbbox((0, 0), logo_text, font=title_font)
        logo_width = logo_bbox[2] - logo_bbox[0]
        draw.text((50, 30), logo_text, fill=self.robot_color, font=title_font)
        
        # Section indicator
        section_text = f"Section {section_number}/{total_sections}"
        section_bbox = draw.textbbox((0, 0), section_text, font=section_font)
        section_width = section_bbox[2] - section_bbox[0]
        draw.text((self.width - section_width - 50, 35), section_text, fill=(200, 200, 200), font=section_font)
        
        # Tutorial status
        status_text = "LIVE TUTORIAL" if robot_speaking else "TUTORIAL"
        status_color = (255, 100, 100) if robot_speaking else (100, 100, 100)
        draw.text((self.width - section_width - 50, 65), status_text, fill=status_color, font=section_font)
        
        # Main title
        title_y = header_height + 40
        # Wrap title if too long
        if len(title) > 60:
            title_lines = self.wrap_text(title, title_font, self.width - 400)
            for i, line in enumerate(title_lines[:2]):  # Max 2 lines for title
                draw.text((50, title_y + i * 55), line, fill=self.robot_color, font=title_font)
            content_start_y = title_y + len(title_lines) * 55 + 30
        else:
            draw.text((50, title_y), title, fill=self.robot_color, font=title_font)
            content_start_y = title_y + 70
        
        # Main content area
        content_area_width = self.width - 350  # Leave space for robot
        wrapped_content = self.wrap_text(content, content_font, content_area_width)
        
        line_height = 35
        max_lines = (self.height - content_start_y - 150) // line_height  # Leave space for progress bar
        
        for i, line in enumerate(wrapped_content[:max_lines]):
            line_y = content_start_y + i * line_height
            # Fade out text near bottom
            alpha = 255 if i < max_lines - 3 else max(50, 255 - (i - (max_lines - 3)) * 70)
            text_color = (alpha, alpha, alpha)
            draw.text((50, line_y), line, fill=text_color, font=content_font)
        
        # Add robot to the right side
        robot = self.create_modern_robot_face(speaking=robot_speaking, frame_size=(200, 200))
        robot_x = self.width - 250
        robot_y = 200
        
        # Robot background panel
        panel_margin = 20
        draw.rounded_rectangle([
            robot_x - panel_margin, robot_y - panel_margin,
            robot_x + 200 + panel_margin, robot_y + 200 + panel_margin
        ], radius=15, fill=(20, 20, 25), outline=self.robot_color, width=2)
        
        # Convert robot to RGB and paste
        robot_rgb = Image.new('RGB', robot.size, (20, 20, 25))
        robot_rgb.paste(robot, mask=robot.split()[-1])
        frame.paste(robot_rgb, (robot_x, robot_y))
        
        # Robot status text
        robot_status = "SPEAKING..." if robot_speaking else "LISTENING"
        robot_status_color = self.robot_color if robot_speaking else (100, 100, 100)
        status_bbox = draw.textbbox((0, 0), robot_status, font=section_font)
        status_width = status_bbox[2] - status_bbox[0]
        draw.text((robot_x + 100 - status_width//2, robot_y + 220), robot_status, fill=robot_status_color, font=section_font)
        
        # Progress bar
        if progress > 0:
            bar_width = self.width - 100
            bar_height = 8
            bar_x = 50
            bar_y = self.height - 80
            
            # Background
            draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], 
                                 radius=bar_height//2, fill=(30, 30, 35))
            
            # Progress
            progress_width = int(bar_width * progress)
            if progress_width > 0:
                draw.rounded_rectangle([bar_x, bar_y, bar_x + progress_width, bar_y + bar_height], 
                                     radius=bar_height//2, fill=self.robot_color)
            
            # Progress text
            progress_text = f"{progress*100:.1f}% Complete"
            progress_bbox = draw.textbbox((0, 0), progress_text, font=section_font)
            progress_text_width = progress_bbox[2] - progress_bbox[0]
            draw.text((bar_x + bar_width - progress_text_width, bar_y + 15), progress_text, 
                     fill=(150, 150, 150), font=section_font)
        
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
                    lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def generate_modern_voice_audio(self, text, filename):
        """Generate modern robot voice using macOS built-in TTS"""
        print(f"🎤 Generating modern robot voice: {filename}")
        
        try:
            # Use macOS 'say' command with different voices for variety
            voices = ['Alex', 'Daniel', 'Fred', 'Victoria', 'Samantha']
            voice = voices[hash(text) % len(voices)]  # Consistent voice per text
            
            # Generate with robot-like effects
            cmd = [
                'say', '-v', voice, '-r', '180',  # Slightly faster rate
                '-o', str(filename), text
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"   ✅ Voice generated successfully")
                return True
            else:
                print(f"   ❌ Voice generation failed: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"   ❌ Error generating voice: {e}")
            return False
    
    def create_tutorial_sections(self):
        """Create comprehensive tutorial sections from the complete guide"""
        sections = [
            {
                "title": "Welcome to C-Cube Cold Wallet",
                "content": "Hey there! Welcome to C-Cube, your new secure cold wallet companion. I'm here to guide you through everything you need to know about managing your cryptocurrency safely and efficiently. Think of me as your personal crypto tutor. C-Cube is different from other wallets because it offers true cold storage, multi-chain support, user-friendly interface, advanced security, and runs as a native desktop application.",
                "duration": 15
            },
            {
                "title": "Getting Started - Your First Launch",
                "content": "When you first open C-Cube, you'll see a security prompt. This isn't scary, it's protective! You'll see a warning about cryptocurrency risks - this ensures you understand the responsibility. Click 'I Understand and Accept the Risks' to continue. Next, you'll see our beautiful welcome screen with two main options: 'Setup New Wallet' for newcomers, or 'Access Existing Wallet' if you're importing an existing wallet.",
                "duration": 18
            },
            {
                "title": "Creating Your First Wallet",
                "content": "Let's create your first wallet! This is like opening your first bank account, but way cooler because you're in complete control. You can choose between a Single Network Wallet for beginners, or a Multi-Chain Wallet for advanced users. I recommend starting with Ethereum. You'll set up password protection to encrypt your private key. Once created, C-Cube shows you three critical pieces: your wallet address, private key, and recovery phrase.",
                "duration": 20
            },
            {
                "title": "The Sacred Recovery Phrase",
                "content": "Your recovery phrase is the master key to your cryptocurrency. Write it down on paper immediately, store it in a fireproof safe, make multiple copies in different locations, and never store it digitally. Never share it with anyone, don't store it on your computer or phone, don't take photos, don't email it, and don't store it in the cloud. People have lost millions by not properly securing their recovery phrase. Don't be one of them!",
                "duration": 18
            },
            {
                "title": "Understanding Security Features",
                "content": "C-Cube has multiple security layers. Layer 1 is cold storage design - your wallet operates offline by default. Layer 2 is password encryption for your private key. Layer 3 is transaction signing - every transaction must be manually signed by you. Layer 4 is network verification to prevent connection to malicious networks. Look for visual security indicators: lock icons for encrypted elements, warning symbols for security considerations, green indicators for secure operations, and red alerts for potential issues.",
                "duration": 22
            },
            {
                "title": "Managing Multiple Wallets",
                "content": "As you grow in crypto, you'll want multiple wallets for different purposes. Think of wallets like different pockets: Main Wallet for primary savings, Trading Wallet for active trading, Privacy Wallet for anonymous transactions, and Network-Specific Wallets for each blockchain. C-Cube makes switching between wallets easy with the dropdown navigation. Use descriptive names and organize them properly for better management.",
                "duration": 20
            },
            {
                "title": "Network Selection and Multi-Chain Support",
                "content": "C-Cube supports multiple blockchain networks. Think of them like different countries with their own currencies. Ethereum is the original smart contract platform with highest security but higher fees. Polygon is Ethereum's faster, cheaper cousin. Binance Smart Chain offers high speed and low cost. Arbitrum and Optimism are Ethereum Layer 2 scaling solutions. Each network has different balances, tokens, transaction fees, and speeds.",
                "duration": 25
            },
            {
                "title": "Sending Your First Transaction",
                "content": "Now for the exciting part - actually using your cryptocurrency! Before sending, verify you have enough balance including gas fees, double-check the recipient address, confirm you're on the correct network, understand the transaction is irreversible, and have your wallet password ready. Fill out the transaction form with recipient address, amount, and any transaction data. Review details carefully, sign the transaction, then broadcast to the network.",
                "duration": 25
            },
            {
                "title": "Understanding Gas Fees",
                "content": "Gas fees are like postage stamps for the blockchain. You pay miners or validators to process your transaction. Factors affecting gas fees include network congestion, transaction complexity, and speed preference. Tips for managing gas fees: check current network fees before sending, consider Layer 2 networks for lower fees, batch multiple transactions when possible, and send during off-peak hours for lower costs.",
                "duration": 18
            },
            {
                "title": "Token Management",
                "content": "Tokens are like apps on your phone - they run on blockchain platforms and give you additional functionality. Common standards include ERC-20 for Ethereum and BEP-20 for Binance Smart Chain. You can add tokens from the token database, through custom addition using contract addresses, or via auto-discovery. Always verify token legitimacy by checking contract addresses against official sources and cross-referencing with official websites.",
                "duration": 22
            },
            {
                "title": "Transaction History and Monitoring",
                "content": "Your transaction history is like your crypto bank statement. It records every transaction you send or receive, token transfers, smart contract interactions, and even failed transactions. Use it for tax purposes, budgeting, and security monitoring. Regularly review your history for unauthorized transactions and keep records for tax calculations. You can explore detailed information using block explorers like Etherscan for Ethereum.",
                "duration": 20
            },
            {
                "title": "Advanced Features",
                "content": "Ready to level up? C-Cube offers advanced features like multi-network wallet management, custom gas fee settings, transaction data fields, and smart contract interactions. You can perform direct contract calls, interact with DeFi protocols, and manage NFTs. Advanced users can view raw transactions, configure custom RPC endpoints, and integrate with external tools for enhanced functionality.",
                "duration": 20
            },
            {
                "title": "Security Best Practices",
                "content": "Security isn't just a feature, it's a mindset. Follow the security hierarchy: physical security with strong computer passwords and secure recovery phrase storage, digital security with unique passwords and updated software, operational security by verifying addresses and using test transactions, and social engineering protection by being skeptical of unsolicited contact and never sharing private keys.",
                "duration": 22
            },
            {
                "title": "Troubleshooting Common Issues",
                "content": "Even experienced users encounter issues. Common problems include wallet access issues, balance and display problems, stuck or failed transactions, network connection issues, and interface problems. For wallet access issues, use your recovery phrase to restore. For missing balances, check you're on the correct network. For stuck transactions, be patient during network congestion. Always contact support with specific error messages if issues persist.",
                "duration": 20
            },
            {
                "title": "Your C-Cube Journey Begins",
                "content": "Congratulations! You now have comprehensive knowledge to safely manage your cryptocurrency with C-Cube. Remember the golden rules: security first with strong passwords and secure backups, start small with test transactions, and stay informed about blockchain developments. You're not just managing digital assets - you're participating in a financial revolution. Every expert was once a beginner. Welcome to the future of finance. Welcome to C-Cube. Your journey starts now!",
                "duration": 25
            }
        ]
        
        return sections
    
    def create_complete_tutorial_video(self):
        """Generate the complete tutorial video"""
        print("\n🚀 Generating Complete C-Cube Tutorial Video...")
        
        sections = self.create_tutorial_sections()
        total_sections = len(sections)
        all_frames = []
        all_audio_files = []
        
        # Create frames and audio for each section
        current_progress = 0
        total_duration = sum(section['duration'] for section in sections)
        
        for i, section in enumerate(sections):
            print(f"\n📹 Creating Section {i+1}/{total_sections}: {section['title']}")
            
            # Generate audio first
            audio_file = self.output_dir / f"complete_section_{i:02d}.wav"
            self.generate_modern_voice_audio(section['content'], audio_file)
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
                
                # Speaking animation (robot speaks for 70% of the time)
                speaking = (frame_num % 60) < 42  # Speaking pattern
                
                frame = self.create_tutorial_frame(
                    title=section['title'],
                    content=section['content'],
                    section_number=i+1,
                    total_sections=total_sections,
                    robot_speaking=speaking,
                    progress=overall_progress
                )
                
                all_frames.append(frame)
            
            current_progress += section['duration']
            print(f"   ✅ Section {i+1} completed: {len(all_frames)} total frames")
        
        # Create final video
        print(f"\n🎬 Creating final video with {len(all_frames)} frames...")
        
        # Save frames temporarily
        temp_dir = Path("temp_complete_frames")
        temp_dir.mkdir(exist_ok=True)
        
        print("   💾 Saving frames...")
        for i, frame in enumerate(all_frames):
            if i % 100 == 0:  # Progress indicator
                print(f"      Saved {i}/{len(all_frames)} frames")
            frame_path = temp_dir / f"frame_{i:06d}.png"
            frame.save(frame_path, "PNG")
        
        # Combine all audio files
        print("   🎵 Combining audio tracks...")
        combined_audio = self.output_dir / "complete_tutorial_audio.wav"
        
        if all_audio_files:
            # Use FFmpeg to concatenate audio files
            audio_list_file = self.output_dir / "audio_files.txt"
            with open(audio_list_file, 'w') as f:
                for audio_file in all_audio_files:
                    f.write(f"file '{audio_file.absolute()}'\n")
            
            concat_cmd = [
                'ffmpeg', '-y', '-f', 'concat', '-safe', '0',
                '-i', str(audio_list_file),
                '-c', 'copy', str(combined_audio)
            ]
            
            subprocess.run(concat_cmd, capture_output=True)
            audio_list_file.unlink()  # Clean up
        
        # Create final video with audio
        output_video = self.output_dir / "CCube_Complete_Tutorial_Master.mp4"
        
        print("   🎥 Rendering final video...")
        video_cmd = [
            'ffmpeg', '-y',
            '-framerate', str(self.fps),
            '-i', str(temp_dir / 'frame_%06d.png'),
            '-i', str(combined_audio) if combined_audio.exists() else '/dev/null',
            '-c:v', 'libx264',
            '-preset', 'medium',
            '-crf', '23',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-r', str(self.fps),
            '-shortest',
            str(output_video)
        ]
        
        result = subprocess.run(video_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Clean up temporary files
            print("   🧹 Cleaning up temporary files...")
            for frame_file in temp_dir.glob("*.png"):
                frame_file.unlink()
            temp_dir.rmdir()
            
            # Clean up individual audio files
            for audio_file in all_audio_files:
                audio_file.unlink()
            if combined_audio.exists():
                combined_audio.unlink()
            
            # Get final video stats
            file_size_mb = output_video.stat().st_size / (1024 * 1024)
            duration_minutes = total_duration / 60
            
            print(f"\n🎉 COMPLETE TUTORIAL VIDEO CREATED!")
            print(f"📁 Location: {output_video}")
            print(f"📊 File Size: {file_size_mb:.1f} MB")
            print(f"⏱️  Duration: {duration_minutes:.1f} minutes")
            print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
            print(f"🎵 Audio: Modern robot voice with synchronized speech")
            print(f"🤖 Features: Animated robot, progress tracking, modern UI")
            
            return output_video
        else:
            print(f"❌ Video creation failed: {result.stderr}")
            return None

def main():
    """Main function"""
    generator = CompleteTutorialGenerator()
    result = generator.create_complete_tutorial_video()
    
    if result:
        print(f"\n🎬 Opening your complete C-Cube tutorial video...")
        os.system(f"open '{result}'")
    else:
        print("❌ Failed to create complete tutorial video")

if __name__ == "__main__":
    main()
