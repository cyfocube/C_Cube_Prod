#!/usr/bin/env python3
"""
C-Cube Screenshot Helper
Simple helper to guide you through taking screenshots manually
"""

import subprocess
import time
from pathlib import Path

def create_screenshot_folder():
    """Create folder for screenshots"""
    folder = Path("real_app_screenshots")
    folder.mkdir(exist_ok=True)
    return folder

def open_app_and_guide():
    """Open app and guide through screenshot process"""
    print("📸 C-CUBE SCREENSHOT HELPER")
    print("🚀 Let's get your REAL app screenshots")
    print("=" * 60)
    
    # Create folder
    screenshot_folder = create_screenshot_folder()
    
    print(f"📁 Screenshot folder created: {screenshot_folder.absolute()}")
    
    # Open the app
    print("\n1️⃣ Opening your C-Cube app...")
    try:
        subprocess.run(['open', 'http://localhost:3000'], check=True)
        print("✅ App opened in browser")
    except:
        print("❌ Please open http://localhost:3000 manually")
    
    print("\n2️⃣ SIMPLE SCREENSHOT INSTRUCTIONS:")
    print("=" * 40)
    print("🎯 To take a screenshot:")
    print("   1. Press Cmd + Shift + 4")
    print("   2. Press SPACEBAR (cursor becomes camera)")
    print("   3. Click on your browser window")
    print("   4. Screenshot will be saved to Desktop")
    print("   5. Move it to the screenshots folder")
    print()
    
    screenshots_needed = [
        "01_welcome_screen.png - Main welcome/home page",
        "02_setup_screen.png - Wallet setup/creation page", 
        "03_main_wallet.png - Main wallet interface",
        "04_resources.png - Resources or other important screens"
    ]
    
    print("📱 Screenshots needed:")
    for i, screenshot in enumerate(screenshots_needed, 1):
        print(f"   {i}. {screenshot}")
    
    print(f"\n📁 Save all screenshots to: {screenshot_folder.absolute()}")
    print("\n🎯 When done, press ENTER...")
    input()
    
    # Open the screenshot folder
    print("📁 Opening screenshot folder...")
    subprocess.run(['open', str(screenshot_folder)])
    
    print("\n✅ Screenshot session complete!")
    print("📱 Your real app screenshots are now saved")
    print("🎯 These show your ACTUAL C-Cube UI!")

if __name__ == "__main__":
    open_app_and_guide()