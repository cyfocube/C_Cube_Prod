#!/usr/bin/env python3
"""
Script to remove background from LetterC2.png
"""

from PIL import Image
import os

def remove_background(input_path, output_path):
    """
    Remove background from an image by making white/light colors transparent
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert to RGBA if not already
        img = img.convert("RGBA")
        
        # Get image data
        data = img.getdata()
        
        # Create new data with transparent background
        new_data = []
        for item in data:
            # If pixel is close to white/light gray, make it transparent
            # Adjust these values based on the background color
            if item[0] > 200 and item[1] > 200 and item[2] > 200:  # Light colors
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(item)  # Keep original
        
        # Update image data
        img.putdata(new_data)
        
        # Save with transparency
        img.save(output_path, "PNG")
        print(f"Background removed! Saved as: {output_path}")
        
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    input_file = "Images/LetterC2.png"
    output_file = "Images/LetterC2_no_bg.png"
    
    if os.path.exists(input_file):
        remove_background(input_file, output_file)
    else:
        print(f"Input file {input_file} not found!")