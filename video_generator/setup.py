#!/usr/bin/env python3
"""
Setup script for C-Cube Video Generator
Installs all required packages and dependencies
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python {version.major}.{version.minor} is not supported")
        print("📋 Please install Python 3.8 or higher")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_packages():
    """Install required Python packages"""
    print("📦 Installing Python packages...")
    
    # Basic packages that should install easily
    basic_packages = [
        "pillow>=10.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "requests>=2.31.0"
    ]
    
    # Video processing packages
    video_packages = [
        "moviepy>=1.0.3",
        "opencv-python>=4.8.0",
        "imageio>=2.31.0"
    ]
    
    # Audio packages
    audio_packages = [
        "pyttsx3>=2.90",
        "gtts>=2.4.0",
        "pydub>=0.25.1"
    ]
    
    # Screen capture packages
    screen_packages = [
        "pyautogui>=0.9.54",
        "mss>=9.0.1"
    ]
    
    all_package_groups = [
        ("Basic packages", basic_packages),
        ("Video processing packages", video_packages),
        ("Audio packages", audio_packages),
        ("Screen capture packages", screen_packages)
    ]
    
    failed_packages = []
    
    for group_name, packages in all_package_groups:
        print(f"\n🔨 Installing {group_name}...")
        for package in packages:
            command = f"{sys.executable} -m pip install {package}"
            if not run_command(command, f"Installing {package}"):
                failed_packages.append(package)
    
    if failed_packages:
        print(f"\n⚠️  Some packages failed to install: {failed_packages}")
        print("📋 You can try installing them manually:")
        for package in failed_packages:
            print(f"   pip install {package}")
        return False
    
    print("\n✅ All packages installed successfully!")
    return True

def setup_directories():
    """Create necessary directories"""
    directories = ["output", "temp", "assets"]
    
    for dir_name in directories:
        dir_path = Path(dir_name)
        dir_path.mkdir(exist_ok=True)
        print(f"📁 Created directory: {dir_path}")

def test_installation():
    """Test if all packages can be imported"""
    print("\n🧪 Testing package imports...")
    
    test_imports = [
        ("PIL", "Pillow"),
        ("numpy", "NumPy"),
        ("matplotlib", "Matplotlib"),
        ("cv2", "OpenCV"),
        ("moviepy.editor", "MoviePy"),
        ("pyttsx3", "pyttsx3"),
        ("gtts", "gTTS"),
        ("pyautogui", "PyAutoGUI"),
        ("mss", "MSS")
    ]
    
    failed_imports = []
    
    for module, name in test_imports:
        try:
            __import__(module)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"❌ {name} import failed: {e}")
            failed_imports.append(name)
    
    if failed_imports:
        print(f"\n⚠️  Some imports failed: {failed_imports}")
        print("📋 Video generation may have limited functionality")
        return False
    
    print("\n🎉 All packages imported successfully!")
    return True

def create_demo_script():
    """Create a simple demo script to test functionality"""
    demo_script = '''#!/usr/bin/env python3
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
'''
    
    with open("demo_test.py", "w") as f:
        f.write(demo_script)
    
    print("✅ Demo script created: demo_test.py")

def main():
    """Main setup function"""
    print("🤖 C-Cube Video Generator Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Create directories
    setup_directories()
    
    # Install packages
    if not install_packages():
        print("\n⚠️  Some packages failed to install, but continuing...")
    
    # Test installation
    test_installation()
    
    # Create demo script
    create_demo_script()
    
    print("\n🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Run: python demo_test.py (to test basic functionality)")
    print("2. Run: python ccube_video_generator.py (to generate tutorial video)")
    print("3. Make sure your C-Cube app is running at http://localhost:3000")
    
    return True

if __name__ == "__main__":
    main()
