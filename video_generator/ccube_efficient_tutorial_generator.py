#!/usr/bin/env python3
"""
C-Cube Efficient Tutorial Video Generator
Creates a comprehensive tutorial video with optimized memory usage
"""

import os
import subprocess
import tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import time

class CCubeEfficientTutorialGenerator:
    """Generate C-Cube tutorial video with memory optimization"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        # Optimized video settings
        self.width = 1280  # 720p for efficiency
        self.height = 720
        self.fps = 24  # Lower FPS for smaller file
        self.robot_color = (0, 204, 51)
        
        print("🎥 C-Cube Efficient Tutorial Video Generator")
        print(f"📁 Output: {self.output_dir}")
        print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
    
    def create_robot_face(self, speaking=False, frame_size=(160, 160)):
        """Create efficient robot face"""
        img = Image.new('RGBA', frame_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        center_x, center_y = frame_size[0] // 2, frame_size[1] // 2
        head_size = frame_size[0] - 30
        
        # Simple head
        head_rect = [
            center_x - head_size//2, center_y - head_size//2,
            center_x + head_size//2, center_y + head_size//2
        ]
        draw.rounded_rectangle(head_rect, radius=15, outline=self.robot_color, width=3, fill=(10, 10, 15))
        
        # Eyes
        eye_size = head_size // 8
        eye_y = center_y - head_size // 4
        left_eye_x = center_x - head_size // 4
        right_eye_x = center_x + head_size // 4
        
        eye_color = (0, 255, 51) if speaking else (0, 180, 51)
        
        draw.ellipse([
            left_eye_x - eye_size, eye_y - eye_size//2,
            left_eye_x + eye_size, eye_y + eye_size//2
        ], fill=eye_color)
        
        draw.ellipse([
            right_eye_x - eye_size, eye_y - eye_size//2,
            right_eye_x + eye_size, eye_y + eye_size//2
        ], fill=eye_color)
        
        # Mouth
        mouth_y = center_y + head_size // 4
        mouth_width = head_size // 3
        
        if speaking:
            mouth_height = 8
            draw.ellipse([
                center_x - mouth_width//2, mouth_y - mouth_height//2,
                center_x + mouth_width//2, mouth_y + mouth_height//2
            ], fill=self.robot_color)
        else:
            draw.rounded_rectangle([
                center_x - mouth_width//2, mouth_y - 2,
                center_x + mouth_width//2, mouth_y + 2
            ], radius=2, fill=self.robot_color)
        
        return img
    
    def create_tutorial_frame(self, title, content, section_num, total_sections, speaking=False, progress=0.0):
        """Create efficient tutorial frame"""
        frame = Image.new('RGB', (self.width, self.height), (5, 5, 10))
        draw = ImageDraw.Draw(frame)
        
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
            content_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
            small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
        except:
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        # Header
        header_height = 80
        draw.rectangle([0, 0, self.width, header_height], fill=(0, 0, 0))
        draw.rectangle([0, header_height-2, self.width, header_height], fill=self.robot_color)
        
        # Logo
        draw.text((30, 25), "C-CUBE TUTORIAL", fill=self.robot_color, font=title_font)
        
        # Section info
        section_text = f"Section {section_num}/{total_sections}"
        draw.text((self.width - 200, 25), section_text, fill=(200, 200, 200), font=small_font)
        
        status_text = "🔴 SPEAKING" if speaking else "⚪ READY"
        draw.text((self.width - 200, 45), status_text, fill=(255, 100, 100) if speaking else (100, 200, 100), font=small_font)
        
        # Title
        title_y = header_height + 30
        wrapped_title = self.wrap_text(title, title_font, self.width - 250)
        for i, line in enumerate(wrapped_title[:2]):
            draw.text((30, title_y + i * 40), line, fill=self.robot_color, font=title_font)
        
        # Content
        content_y = title_y + len(wrapped_title) * 40 + 20
        content_width = self.width - 220
        wrapped_content = self.wrap_text(content, content_font, content_width)
        
        line_height = 28
        max_lines = (self.height - content_y - 100) // line_height
        
        for i, line in enumerate(wrapped_content[:max_lines]):
            if line.strip():
                line_y = content_y + i * line_height
                alpha = 255 if i < max_lines - 3 else max(80, 255 - (i - (max_lines - 3)) * 50)
                draw.text((30, line_y), line, fill=(alpha, alpha, alpha), font=content_font)
        
        # Robot
        robot = self.create_robot_face(speaking=speaking)
        robot_x = self.width - 180
        robot_y = 120
        
        # Robot panel
        draw.rounded_rectangle([
            robot_x - 10, robot_y - 10,
            robot_x + 170, robot_y + 170
        ], radius=10, fill=(15, 15, 20), outline=self.robot_color, width=2)
        
        robot_rgb = Image.new('RGB', robot.size, (15, 15, 20))
        robot_rgb.paste(robot, mask=robot.split()[-1])
        frame.paste(robot_rgb, (robot_x, robot_y))
        
        # Progress bar
        if progress > 0:
            bar_width = self.width - 60
            bar_height = 6
            bar_x = 30
            bar_y = self.height - 50
            
            draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], 
                                 radius=3, fill=(30, 30, 35))
            
            progress_width = int(bar_width * progress)
            if progress_width > 0:
                draw.rounded_rectangle([bar_x, bar_y, bar_x + progress_width, bar_y + bar_height], 
                                     radius=3, fill=self.robot_color)
            
            progress_text = f"{progress*100:.0f}% Complete"
            draw.text((bar_x, bar_y + 15), progress_text, fill=(150, 150, 150), font=small_font)
        
        return frame
    
    def wrap_text(self, text, font, max_width):
        """Wrap text efficiently"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            try:
                bbox = font.getbbox(test_line)
                width = bbox[2] - bbox[0]
            except:
                width = len(test_line) * 10  # Fallback
            
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
    
    def generate_simple_audio(self, text, filename):
        """Generate simple TTS audio"""
        print(f"🎤 Generating voice: {filename}")
        
        try:
            cmd = ['say', '-v', 'Alex', '-r', '170', '-o', str(filename), text]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print(f"   ✅ Voice generated")
                return True
            else:
                print(f"   ❌ Failed: {result.stderr}")
                return False
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return False
    
    def create_tutorial_sections(self):
        """Create concise tutorial sections"""
        sections = [
            {
                "title": "Welcome to C-Cube Cold Wallet",
                "content": "Welcome to C-Cube, your secure cold wallet companion. I'm your crypto tutor, here to guide you safely through cryptocurrency management. C-Cube offers true cold storage, multi-chain support, user-friendly interface, advanced security, and runs as a desktop application on all platforms.",
                "duration": 12
            },
            {
                "title": "Getting Started - First Launch",
                "content": "When you first open C-Cube, you'll see a security prompt about cryptocurrency risks. Click 'I Understand and Accept the Risks' to continue. You'll then see the welcome screen with two options: 'Setup New Wallet' for beginners, or 'Access Existing Wallet' to import an existing wallet.",
                "duration": 14
            },
            {
                "title": "Creating Your First Wallet",
                "content": "Let's create your first wallet! Choose between Single Network Wallet for beginners or Multi-Chain Wallet for advanced users. I recommend starting with Ethereum. Set up password protection to encrypt your private key. Once created, you'll see your wallet address, private key, and recovery phrase.",
                "duration": 16
            },
            {
                "title": "The Sacred Recovery Phrase", 
                "content": "Your recovery phrase is the master key to your cryptocurrency. Write it down on paper immediately, store it in a fireproof safe, make multiple copies, and never store it digitally. Never share it with anyone, don't take photos, and don't store it in the cloud. People have lost millions by not securing their recovery phrase properly.",
                "duration": 18
            },
            {
                "title": "Understanding Security Features",
                "content": "C-Cube has four security layers. Cold storage keeps your wallet offline by default. Password encryption protects your private key. Transaction signing requires manual approval for every transaction. Network verification prevents connection to malicious networks. Look for security indicators in the interface.",
                "duration": 16
            },
            {
                "title": "Managing Multiple Wallets",
                "content": "As you grow, you'll want multiple wallets for different purposes. Main wallet for savings, trading wallet for active trading, privacy wallet for anonymous transactions. Create additional wallets easily and switch between them using the dropdown navigation.",
                "duration": 14
            },
            {
                "title": "Network Selection and Multi-Chain Support",
                "content": "C-Cube supports multiple blockchain networks. Ethereum for security, Polygon for lower fees, Binance Smart Chain for speed, Arbitrum and Optimism for scaling. Each network has different balances, tokens, fees, and speeds. Switch networks easily with the network selector.",
                "duration": 16
            },
            {
                "title": "Sending Your First Transaction",
                "content": "Before sending, verify your balance includes gas fees, double-check recipient address, confirm correct network, and have your password ready. Fill out the transaction form, review details carefully, sign the transaction, then broadcast to the network. Always start with small test amounts.",
                "duration": 16
            },
            {
                "title": "Understanding Gas Fees",
                "content": "Gas fees are like postage for blockchain transactions. Factors affecting fees include network congestion, transaction complexity, and speed preference. Save money by using Layer 2 networks, batching transactions, and sending during off-peak hours. Always verify recipient addresses carefully.",
                "duration": 14
            },
            {
                "title": "Token Management",
                "content": "Tokens are digital assets that run on blockchains. Add tokens from the database, through custom addition using contract addresses, or via auto-discovery. Always verify token legitimacy by checking contract addresses against official sources and using block explorers.",
                "duration": 14
            },
            {
                "title": "Transaction History and Monitoring",
                "content": "Your transaction history records all activity including sends, receives, token transfers, and smart contract interactions. Use it for tax purposes, budgeting, and security monitoring. Regularly review for unauthorized transactions and export for record keeping.",
                "duration": 14
            },
            {
                "title": "Advanced Features",
                "content": "Advanced features include multi-network wallet management, custom gas fee settings, transaction data fields, and smart contract interactions. You can perform direct contract calls, interact with DeFi protocols, and configure custom RPC endpoints for enhanced functionality.",
                "duration": 14
            },
            {
                "title": "Security Best Practices",
                "content": "Follow the security hierarchy: physical security with strong passwords, digital security with updated software, operational security by verifying addresses, and social engineering protection. Use strong unique passwords, password managers, and be skeptical of unsolicited contact.",
                "duration": 16
            },
            {
                "title": "Troubleshooting Common Issues",
                "content": "Common issues include wallet access problems, missing balances, stuck transactions, and network connection issues. For wallet access, use recovery phrase. For missing balances, check correct network. For stuck transactions, be patient during congestion. Your funds are always safe on the blockchain.",
                "duration": 16
            },
            {
                "title": "Your C-Cube Journey Begins",
                "content": "Congratulations! You now know how to safely manage cryptocurrency with C-Cube. Remember: security first, start small, and stay informed. You're participating in a financial revolution. Every expert was once a beginner. Welcome to the future of finance. Your C-Cube journey starts now!",
                "duration": 16
            }
        ]
        
        return sections
    
    def create_efficient_tutorial_video(self):
        """Generate tutorial video with memory optimization"""
        print("\n🚀 Generating Efficient C-Cube Tutorial Video...")
        
        sections = self.create_tutorial_sections()
        total_sections = len(sections)
        total_duration = sum(section['duration'] for section in sections)
        
        print(f"📊 Total duration: {total_duration/60:.1f} minutes")
        print(f"🎬 Total sections: {total_sections}")
        
        # Process in batches to manage memory
        batch_size = 3  # Process 3 sections at a time
        video_parts = []
        
        for batch_start in range(0, total_sections, batch_size):
            batch_end = min(batch_start + batch_size, total_sections)
            batch_sections = sections[batch_start:batch_end]
            
            print(f"\n📹 Processing batch {batch_start//batch_size + 1}: sections {batch_start+1}-{batch_end}")
            
            # Create temporary video for this batch
            batch_video = self.create_batch_video(batch_sections, batch_start, total_sections, total_duration)
            if batch_video:
                video_parts.append(batch_video)
        
        # Combine all batch videos
        if video_parts:
            final_video = self.combine_video_parts(video_parts)
            
            # Clean up batch videos
            for part in video_parts:
                if part.exists():
                    part.unlink()
            
            return final_video
        
        return None
    
    def create_batch_video(self, sections, start_index, total_sections, total_duration):
        """Create video for a batch of sections"""
        batch_frames = []
        batch_audio_files = []
        
        current_progress_base = sum(sections[i]['duration'] for i in range(start_index)) / total_duration
        
        for i, section in enumerate(sections):
            print(f"   📝 Section {start_index + i + 1}: {section['title']}")
            
            # Generate audio
            audio_file = self.output_dir / f"batch_audio_{start_index + i:02d}.wav"
            self.generate_simple_audio(section['content'], audio_file)
            if audio_file.exists():
                batch_audio_files.append(audio_file)
            
            # Generate frames
            frames_in_section = int(section['duration'] * self.fps)
            section_progress_base = current_progress_base + sum(sections[j]['duration'] for j in range(i)) / total_duration
            
            for frame_num in range(frames_in_section):
                frame_progress = frame_num / frames_in_section
                overall_progress = section_progress_base + (section['duration'] / total_duration) * frame_progress
                
                speaking = (frame_num % 48) < 32  # Speaking pattern
                
                frame = self.create_tutorial_frame(
                    title=section['title'],
                    content=section['content'],
                    section_num=start_index + i + 1,
                    total_sections=total_sections,
                    speaking=speaking,
                    progress=overall_progress
                )
                
                batch_frames.append(frame)
        
        # Save batch frames
        temp_dir = Path(f"temp_batch_{start_index}")
        temp_dir.mkdir(exist_ok=True)
        
        for i, frame in enumerate(batch_frames):
            frame_path = temp_dir / f"frame_{i:05d}.png"
            frame.save(frame_path, "PNG")
        
        # Combine batch audio
        batch_audio = self.output_dir / f"batch_audio_{start_index}.wav"
        if batch_audio_files:
            audio_list = self.output_dir / f"batch_audio_list_{start_index}.txt"
            with open(audio_list, 'w') as f:
                for audio_file in batch_audio_files:
                    f.write(f"file '{audio_file.absolute()}'\n")
            
            cmd = [
                'ffmpeg', '-y', '-f', 'concat', '-safe', '0',
                '-i', str(audio_list), '-c', 'copy', str(batch_audio)
            ]
            subprocess.run(cmd, capture_output=True)
            audio_list.unlink()
        
        # Create batch video
        batch_video = self.output_dir / f"batch_video_{start_index}.mp4"
        
        cmd = [
            'ffmpeg', '-y',
            '-framerate', str(self.fps),
            '-i', str(temp_dir / 'frame_%05d.png'),
            '-i', str(batch_audio) if batch_audio.exists() else '/dev/null',
            '-c:v', 'libx264', '-preset', 'fast', '-crf', '23',
            '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k',
            '-shortest', str(batch_video)
        ]
        
        result = subprocess.run(cmd, capture_output=True)
        
        # Clean up
        for frame_file in temp_dir.glob("*.png"):
            frame_file.unlink()
        temp_dir.rmdir()
        
        for audio_file in batch_audio_files:
            if audio_file.exists():
                audio_file.unlink()
        if batch_audio.exists():
            batch_audio.unlink()
        
        if result.returncode == 0:
            print(f"   ✅ Batch video created: {batch_video}")
            return batch_video
        else:
            print(f"   ❌ Batch video failed: {result.stderr}")
            return None
    
    def combine_video_parts(self, video_parts):
        """Combine video parts into final video"""
        print("\n🎬 Combining video parts...")
        
        # Create list file for concatenation
        parts_list = self.output_dir / "video_parts.txt"
        with open(parts_list, 'w') as f:
            for part in video_parts:
                f.write(f"file '{part.absolute()}'\n")
        
        final_video = self.output_dir / "CCube_Complete_Tutorial.mp4"
        
        cmd = [
            'ffmpeg', '-y', '-f', 'concat', '-safe', '0',
            '-i', str(parts_list), '-c', 'copy', str(final_video)
        ]
        
        result = subprocess.run(cmd, capture_output=True)
        parts_list.unlink()
        
        if result.returncode == 0:
            file_size_mb = final_video.stat().st_size / (1024 * 1024)
            print(f"\n🎉 TUTORIAL VIDEO COMPLETE!")
            print(f"📁 Location: {final_video}")
            print(f"📊 File Size: {file_size_mb:.1f} MB")
            print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
            return final_video
        else:
            print(f"❌ Final video creation failed: {result.stderr}")
            return None

def main():
    """Main function"""
    generator = CCubeEfficientTutorialGenerator()
    result = generator.create_efficient_tutorial_video()
    
    if result:
        print(f"\n🎬 Opening your C-Cube tutorial video...")
        os.system(f"open '{result}'")
    else:
        print("❌ Failed to create tutorial video")

if __name__ == "__main__":
    main()