#!/usr/bin/env python3
"""
Advanced background removal for LetterC2.png
"""

from PIL import Image
import os

def remove_background_advanced(input_path, output_path):
    """
    More aggressive background removal
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert to RGBA
        img = img.convert("RGBA")
        
        # Get image data
        data = img.getdata()
        
        # Create new data with transparent background
        new_data = []
        for item in data:
            r, g, b, a = item
            
            # More aggressive: remove lighter colors and grays
            # Calculate brightness
            brightness = (r + g + b) / 3
            
            # If pixel is light (bright) or close to gray, make transparent
            if brightness > 150 or (abs(r-g) < 30 and abs(g-b) < 30 and abs(r-b) < 30 and brightness > 100):
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(item)  # Keep original
        
        # Update image data
        img.putdata(new_data)
        
        # Save with transparency
        img.save(output_path, "PNG")
        print(f"Advanced background removed! Saved as: {output_path}")
        
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    input_file = "Images/LetterC2.png"
    output_file = "Images/LetterC2_transparent.png"
    
    if os.path.exists(input_file):
        remove_background_advanced(input_file, output_file)
    else:
        print(f"Input file {input_file} not found!")