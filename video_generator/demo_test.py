#!/usr/bin/env python3
"""
Simple demo to test C-Cube video generator components
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def create_demo_frame():
    """Create a demo video frame"""
    # Create a black frame
    frame = np.zeros((720, 1280, 3), dtype=np.uint8)
    
    # Convert to PIL for text
    img = Image.fromarray(frame)
    draw = ImageDraw.Draw(img)
    
    # Add demo text
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
    except:
        font = ImageFont.load_default()
    
    text = "C-Cube Video Generator Demo"
    
    # Get text dimensions
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center text
    x = (1280 - text_width) // 2
    y = (720 - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=(0, 204, 51), font=font)
    
    return np.array(img)

def main():
    print("🎬 Running C-Cube Video Generator Demo...")
    
    # Create demo frame
    frame = create_demo_frame()
    
    # Save as image
    img = Image.fromarray(frame)
    img.save("demo_frame.png")
    print("✅ Demo frame saved as demo_frame.png")
    
    # Test matplotlib animation
    fig, ax = plt.subplots()
    ax.imshow(frame)
    ax.set_title("C-Cube Demo Frame")
    ax.axis('off')
    plt.savefig("demo_matplotlib.png")
    print("✅ Matplotlib demo saved as demo_matplotlib.png")
    
    print("🎉 Demo completed successfully!")
    print("📋 You can now run the full video generator!")

if __name__ == "__main__":
    main()
