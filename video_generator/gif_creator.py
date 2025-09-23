#!/usr/bin/env python3
"""
Create animated GIF from robot tutorial frames
"""

import glob
from pathlib import Path
from PIL import Image

def create_animated_gif(frames_pattern, output_file, duration=500):
    """Create animated GIF from frames"""
    
    # Get frame files
    frame_files = sorted(glob.glob(frames_pattern))
    if not frame_files:
        print(f"No frames found: {frames_pattern}")
        return False
    
    print(f"Creating animated GIF from {len(frame_files)} frames")
    
    # Load images
    images = []
    for frame_file in frame_files:
        img = Image.open(frame_file)
        # Resize for smaller file size
        img = img.resize((640, 360), Image.Resampling.LANCZOS)
        images.append(img)
    
    # Save as animated GIF
    images[0].save(
        output_file,
        save_all=True,
        append_images=images[1:],
        duration=duration,  # Duration per frame in milliseconds
        loop=0  # Infinite loop
    )
    
    print(f"✅ Animated GIF created: {output_file}")
    return True

def create_tutorial_gifs():
    """Create GIFs for all tutorial sections"""
    output_dir = Path("output")
    
    sections = [
        ("section_00_Welcome_to_C-Cube_Cold_Wallet", "Welcome"),
        ("section_01_Getting_Started_-_Security_First", "Security"),
        ("section_02_Creating_Your_First_Wallet", "Creating_Wallet"),
        ("section_03_Understanding_Networks", "Networks"),
        ("section_04_Sending_Your_First_Transaction", "Transactions")
    ]
    
    for section_prefix, short_name in sections:
        print(f"\n🎬 Creating GIF for: {short_name}")
        
        frames_pattern = str(output_dir / f"{section_prefix}_frame_*.png")
        output_gif = output_dir / f"{short_name}_tutorial.gif"
        
        create_animated_gif(frames_pattern, str(output_gif), duration=800)
    
    # Create a combined preview GIF with one frame from each section
    print(f"\n🎬 Creating preview GIF...")
    
    preview_frames = []
    for section_prefix, short_name in sections:
        # Take the first frame from each section
        first_frame_pattern = str(output_dir / f"{section_prefix}_frame_0000.png")
        frame_files = glob.glob(first_frame_pattern)
        if frame_files:
            img = Image.open(frame_files[0])
            img = img.resize((320, 180), Image.Resampling.LANCZOS)  # Smaller for preview
            
            # Add section title overlay
            from PIL import ImageDraw, ImageFont
            draw = ImageDraw.Draw(img)
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 20)
            except:
                font = ImageFont.load_default()
            
            # Add background for text
            text = short_name.replace('_', ' ')
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Draw background rectangle
            padding = 10
            rect_coords = [
                10, 10,
                10 + text_width + padding * 2,
                10 + text_height + padding * 2
            ]
            draw.rectangle(rect_coords, fill=(0, 0, 0, 128))
            draw.text((10 + padding, 10 + padding), text, fill=(0, 255, 0), font=font)
            
            preview_frames.append(img)
    
    if preview_frames:
        preview_gif = output_dir / "CCube_Tutorial_Preview.gif"
        preview_frames[0].save(
            preview_gif,
            save_all=True,
            append_images=preview_frames[1:],
            duration=2000,  # 2 seconds per section
            loop=0
        )
        print(f"✅ Preview GIF created: {preview_gif}")

def main():
    """Main function"""
    print("🤖 C-Cube Animated GIF Creator")
    print("=" * 40)
    
    output_dir = Path("output")
    if not output_dir.exists():
        print("❌ No output directory found. Run the generator first.")
        return
    
    # Check for frames
    frame_files = list(output_dir.glob("*.png"))
    print(f"📊 Found {len(frame_files)} frames")
    
    if frame_files:
        create_tutorial_gifs()
        
        print(f"\n🎉 Tutorial GIFs created successfully!")
        print(f"📁 Location: {output_dir}")
        print(f"🎥 You can now view the animated tutorial GIFs!")
        
        # List created files
        gif_files = list(output_dir.glob("*.gif"))
        for gif_file in gif_files:
            size_mb = gif_file.stat().st_size / (1024 * 1024)
            print(f"   📊 {gif_file.name}: {size_mb:.1f} MB")
            
    else:
        print("❌ No frames found. Run the generator first.")

if __name__ == "__main__":
    main()
