#!/usr/bin/env python3
"""
C-Cube Simple Tutorial Video Generator
Creates a tutorial video using only built-in macOS tools
"""

import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import time

class CCubeSimpleTutorialGenerator:
    """Generate C-Cube tutorial video using simple tools"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        # Simple video settings
        self.width = 1280
        self.height = 720
        self.fps = 15  # Lower FPS for simplicity
        self.robot_color = (0, 204, 51)
        
        print("🎥 C-Cube Simple Tutorial Video Generator")
        print(f"📁 Output: {self.output_dir}")
        print(f"🎬 Resolution: {self.width}x{self.height} @ {self.fps}fps")
    
    def create_robot_face(self, speaking=False):
        """Create simple robot face"""
        size = (120, 120)
        img = Image.new('RGBA', size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        center_x, center_y = size[0] // 2, size[1] // 2
        
        # Head
        head_rect = [20, 20, 100, 100]
        draw.rounded_rectangle(head_rect, radius=10, outline=self.robot_color, width=2, fill=(10, 10, 15))
        
        # Eyes
        eye_color = (0, 255, 51) if speaking else (0, 180, 51)
        draw.ellipse([35, 35, 45, 45], fill=eye_color)
        draw.ellipse([75, 35, 85, 45], fill=eye_color)
        
        # Mouth
        if speaking:
            draw.ellipse([45, 65, 75, 75], fill=self.robot_color)
        else:
            draw.rectangle([45, 68, 75, 72], fill=self.robot_color)
        
        return img
    
    def create_simple_frame(self, title, content, section_num, total_sections, speaking=False, progress=0.0):
        """Create simple tutorial frame"""
        frame = Image.new('RGB', (self.width, self.height), (5, 5, 10))
        draw = ImageDraw.Draw(frame)
        
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
            content_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
            small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
        except:
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        # Header
        draw.rectangle([0, 0, self.width, 60], fill=(0, 0, 0))
        draw.rectangle([0, 58, self.width, 60], fill=self.robot_color)
        
        # Logo and info
        draw.text((20, 20), "C-CUBE TUTORIAL", fill=self.robot_color, font=title_font)
        draw.text((self.width - 200, 20), f"Section {section_num}/{total_sections}", fill=(200, 200, 200), font=small_font)
        
        # Title
        title_y = 80
        # Split long titles
        if len(title) > 50:
            title_words = title.split()
            mid = len(title_words) // 2
            title_line1 = ' '.join(title_words[:mid])
            title_line2 = ' '.join(title_words[mid:])
            draw.text((20, title_y), title_line1, fill=self.robot_color, font=title_font)
            draw.text((20, title_y + 35), title_line2, fill=self.robot_color, font=title_font)
            content_y = title_y + 80
        else:
            draw.text((20, title_y), title, fill=self.robot_color, font=title_font)
            content_y = title_y + 50
        
        # Content
        content_width = self.width - 180
        words = content.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            # Simple width estimation
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
        
        # Display content lines
        max_lines = (self.height - content_y - 80) // 25
        for i, line in enumerate(lines[:max_lines]):
            if line.strip():
                draw.text((20, content_y + i * 25), line, fill=(220, 220, 220), font=content_font)
        
        # Robot
        robot = self.create_robot_face(speaking=speaking)
        robot_x = self.width - 140
        robot_y = 100
        
        # Robot panel
        draw.rectangle([robot_x - 10, robot_y - 10, robot_x + 130, robot_y + 130], 
                      outline=self.robot_color, width=2)
        
        robot_rgb = Image.new('RGB', robot.size, (15, 15, 20))
        robot_rgb.paste(robot, mask=robot.split()[-1])
        frame.paste(robot_rgb, (robot_x, robot_y))
        
        # Status
        status = "SPEAKING" if speaking else "READY"
        status_color = (255, 100, 100) if speaking else (100, 200, 100)
        draw.text((robot_x + 10, robot_y + 130), status, fill=status_color, font=small_font)
        
        # Progress bar
        if progress > 0:
            bar_width = self.width - 40
            bar_height = 6
            bar_x = 20
            bar_y = self.height - 40
            
            draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], fill=(30, 30, 35))
            
            progress_width = int(bar_width * progress)
            if progress_width > 0:
                draw.rectangle([bar_x, bar_y, bar_x + progress_width, bar_y + bar_height], fill=self.robot_color)
            
            draw.text((bar_x, bar_y - 20), f"Progress: {progress*100:.0f}%", fill=(150, 150, 150), font=small_font)
        
        return frame
    
    def generate_voice_audio(self, text, filename):
        """Generate voice using macOS say command"""
        print(f"🎤 Generating voice: {filename.name}")
        
        try:
            # Use AIFF format which macOS handles better
            aiff_file = str(filename).replace('.wav', '.aiff')
            cmd = ['say', '-v', 'Alex', '-r', '160', '-o', aiff_file, text]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0 and os.path.exists(aiff_file):
                print(f"   ✅ Voice generated successfully")
                return aiff_file
            else:
                print(f"   ❌ Failed: {result.stderr}")
                return None
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return None
    
    def create_tutorial_sections(self):
        """Create tutorial sections"""
        sections = [
            {
                "title": "Welcome to C-Cube Cold Wallet",
                "content": "Welcome to C-Cube, your secure cold wallet companion. I'm your crypto tutor. C-Cube offers true cold storage, multi-chain support, user-friendly interface, advanced security, and runs as a desktop application.",
                "duration": 10
            },
            {
                "title": "Getting Started - First Launch", 
                "content": "When you first open C-Cube, you'll see a security prompt. Click 'I Understand and Accept the Risks' to continue. Choose 'Setup New Wallet' for beginners or 'Access Existing Wallet' to import.",
                "duration": 10
            },
            {
                "title": "Creating Your First Wallet",
                "content": "Choose Single Network Wallet for beginners or Multi-Chain Wallet for advanced users. Set up password protection. You'll receive your wallet address, private key, and recovery phrase.",
                "duration": 10
            },
            {
                "title": "The Sacred Recovery Phrase",
                "content": "Your recovery phrase is the master key. Write it on paper, store in a fireproof safe, make multiple copies, never store digitally. Never share with anyone or take photos. This is critical for your security.",
                "duration": 12
            },
            {
                "title": "Understanding Security Features",
                "content": "C-Cube has four security layers: cold storage design, password encryption, transaction signing, and network verification. Your wallet operates offline by default for maximum security.",
                "duration": 10
            },
            {
                "title": "Managing Multiple Wallets",
                "content": "Create multiple wallets for different purposes: main wallet for savings, trading wallet for active trading, privacy wallet for anonymous transactions. Switch easily using the dropdown.",
                "duration": 10
            },
            {
                "title": "Network Selection and Multi-Chain Support",
                "content": "C-Cube supports Ethereum, Polygon, Binance Smart Chain, Arbitrum, and Optimism. Each network has different fees and speeds. Switch networks easily with the network selector.",
                "duration": 12
            },
            {
                "title": "Sending Your First Transaction",
                "content": "Before sending, verify balance, double-check recipient address, confirm correct network. Fill out transaction form, review details, sign transaction, then broadcast. Start with small test amounts.",
                "duration": 12
            },
            {
                "title": "Understanding Gas Fees",
                "content": "Gas fees are transaction costs. Factors include network congestion and complexity. Save money using Layer 2 networks, batching transactions, and sending during off-peak hours. Always verify addresses.",
                "duration": 10
            },
            {
                "title": "Token Management",
                "content": "Add tokens from database, custom addition, or auto-discovery. Always verify token legitimacy using official sources and block explorers. Manage your token portfolio efficiently.",
                "duration": 10
            },
            {
                "title": "Transaction History",
                "content": "Your history records all transactions. Use for tax purposes, budgeting, and security. Regularly review for unauthorized activity. Export records for your documentation needs.",
                "duration": 8
            },
            {
                "title": "Advanced Features",
                "content": "Advanced users can customize gas fees, interact with smart contracts, manage multiple networks, and configure custom settings for enhanced functionality.",
                "duration": 8
            },
            {
                "title": "Security Best Practices",
                "content": "Follow security hierarchy: physical security, digital security, operational security, social engineering protection. Use strong passwords, be skeptical of unsolicited contact.",
                "duration": 10
            },
            {
                "title": "Troubleshooting",
                "content": "Common issues: wallet access, missing balances, stuck transactions. For access problems, use recovery phrase. For missing balances, check correct network. Your funds are always safe on blockchain.",
                "duration": 10
            },
            {
                "title": "Your C-Cube Journey Begins",
                "content": "Congratulations! You now know how to safely use C-Cube. Remember: security first, start small, stay informed. You're participating in the financial revolution. Your journey starts now!",
                "duration": 8
            }
        ]
        
        return sections
    
    def create_simple_tutorial_video(self):
        """Generate simple tutorial video"""
        print("\n🚀 Generating Simple C-Cube Tutorial Video...")
        
        sections = self.create_tutorial_sections()
        total_sections = len(sections)
        total_duration = sum(section['duration'] for section in sections)
        
        print(f"📊 Total duration: {total_duration/60:.1f} minutes")
        print(f"🎬 Total sections: {total_sections}")
        
        all_frames = []
        audio_files = []
        
        current_progress = 0
        
        for i, section in enumerate(sections):
            print(f"\n📹 Creating Section {i+1}/{total_sections}: {section['title']}")
            
            # Generate audio
            audio_file = self.output_dir / f"section_{i:02d}.aiff"
            generated_audio = self.generate_voice_audio(section['content'], audio_file)
            if generated_audio:
                audio_files.append(generated_audio)
            
            # Calculate progress
            section_start_progress = current_progress / total_duration
            section_end_progress = (current_progress + section['duration']) / total_duration
            
            # Generate frames
            frames_in_section = int(section['duration'] * self.fps)
            
            for frame_num in range(frames_in_section):
                frame_progress = frame_num / frames_in_section
                overall_progress = section_start_progress + (section_end_progress - section_start_progress) * frame_progress
                
                speaking = (frame_num % 30) < 20  # Speaking pattern
                
                frame = self.create_simple_frame(
                    title=section['title'],
                    content=section['content'],
                    section_num=i+1,
                    total_sections=total_sections,
                    speaking=speaking,
                    progress=overall_progress
                )
                
                all_frames.append(frame)
            
            current_progress += section['duration']
            print(f"   ✅ Section {i+1} completed: {len(all_frames)} total frames")
        
        # Save frames
        print(f"\n💾 Saving {len(all_frames)} frames...")
        frames_dir = self.output_dir / "frames"
        frames_dir.mkdir(exist_ok=True)
        
        for i, frame in enumerate(all_frames):
            if i % 50 == 0:
                print(f"   Saved {i}/{len(all_frames)} frames")
            frame_path = frames_dir / f"frame_{i:05d}.png"
            frame.save(frame_path, "PNG")
        
        print("✅ All frames saved!")
        
        # Create instructions for manual video creation
        instructions_file = self.output_dir / "video_creation_instructions.txt"
        with open(instructions_file, 'w') as f:
            f.write("C-CUBE TUTORIAL VIDEO CREATION INSTRUCTIONS\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Frames saved to: {frames_dir}\n")
            f.write(f"Total frames: {len(all_frames)}\n")
            f.write(f"Frame rate: {self.fps} fps\n")
            f.write(f"Duration: {total_duration} seconds\n\n")
            
            f.write("AUDIO FILES:\n")
            for i, audio_file in enumerate(audio_files):
                f.write(f"Section {i+1}: {audio_file}\n")
            
            f.write("\nTO CREATE VIDEO:\n")
            f.write("1. Install FFmpeg: brew install ffmpeg\n")
            f.write("2. Run this command:\n\n")
            
            # Prepare audio concat list
            audio_list_content = ""
            for audio_file in audio_files:
                audio_list_content += f"file '{Path(audio_file).absolute()}'\n"
            
            audio_list_file = self.output_dir / "audio_list.txt"
            with open(audio_list_file, 'w') as af:
                af.write(audio_list_content)
            
            f.write(f"ffmpeg -y -framerate {self.fps} ")
            f.write(f"-i {frames_dir}/frame_%05d.png ")
            f.write(f"-f concat -safe 0 -i {audio_list_file} ")
            f.write("-c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p ")
            f.write("-c:a aac -b:a 192k -shortest ")
            f.write("CCube_Tutorial_Complete.mp4\n\n")
            
            f.write("OR use any video editing software that supports image sequences.\n")
        
        # Also create a simple slideshow
        print("\n🎥 Creating simple slideshow...")
        slideshow_frames = []
        
        for i, section in enumerate(sections):
            # Create a single frame per section that lasts longer
            frame = self.create_simple_frame(
                title=section['title'],
                content=section['content'],
                section_num=i+1,
                total_sections=total_sections,
                speaking=True,
                progress=(i+1)/total_sections
            )
            
            # Save this as a slideshow frame
            slideshow_frame_path = self.output_dir / f"slide_{i+1:02d}_{section['title'][:30].replace(' ', '_').replace('/', '_')}.png"
            frame.save(slideshow_frame_path, "PNG")
            slideshow_frames.append(slideshow_frame_path)
        
        print(f"\n🎉 TUTORIAL CONTENT CREATED!")
        print("=" * 50)
        print(f"📁 Output directory: {self.output_dir}")
        print(f"🎬 Video frames: {frames_dir} ({len(all_frames)} frames)")
        print(f"🖼️  Slideshow: {len(slideshow_frames)} slides created")
        print(f"🎵 Audio files: {len(audio_files)} voice tracks")
        print(f"📋 Instructions: {instructions_file}")
        print("=" * 50)
        print("✨ Ready for video compilation!")
        
        return instructions_file

def main():
    """Main function"""
    generator = CCubeSimpleTutorialGenerator()
    result = generator.create_simple_tutorial_video()
    
    if result:
        print(f"\n📖 Opening instructions...")
        os.system(f"open '{result}'")
        print(f"📁 Opening output folder...")
        os.system(f"open '{result.parent}'")
    else:
        print("❌ Failed to create tutorial content")

if __name__ == "__main__":
    main()