#!/usr/bin/env python3
"""
C-Cube macOS Screenshot Capturer
Uses macOS built-in screenshot tools to capture your running React app
"""

import os
import time
import subprocess
from pathlib import Path

class CCubeMacOSScreenshotCapturer:
    """Capture real screenshots using macOS tools"""
    
    def __init__(self):
        self.output_dir = Path("real_app_screenshots")
        self.output_dir.mkdir(exist_ok=True)
        
        self.app_url = "http://localhost:3000"
        
        print("📸 C-Cube macOS Screenshot Capturer")
        print(f"📁 Output: {self.output_dir}")
        print(f"🌐 App URL: {self.app_url}")
        print("✨ Using macOS screencapture to get REAL UI")
    
    def open_browser_to_app(self):
        """Open browser to your React app"""
        try:
            # Open in default browser
            subprocess.run(['open', self.app_url], check=True)
            print(f"✅ Opened {self.app_url} in browser")
            time.sleep(3)  # Wait for page to load
            return True
        except Exception as e:
            print(f"❌ Failed to open browser: {e}")
            return False
    
    def take_screenshot(self, filename, description):
        """Take a screenshot using macOS screencapture"""
        try:
            screenshot_path = self.output_dir / filename
            
            # Use macOS screencapture command
            # -w flag captures a specific window (user will need to select)
            # -T 5 gives 5 second delay
            subprocess.run([
                'screencapture', 
                '-T', '5',  # 5 second delay
                '-w',       # Interactive window selection
                str(screenshot_path)
            ], check=True)
            
            print(f"✅ Captured: {description}")
            return True
        except Exception as e:
            print(f"❌ Failed to capture {description}: {e}")
            return False
    
    def take_automatic_screenshot(self, filename, description):
        """Take automatic screenshot of entire screen"""
        try:
            screenshot_path = self.output_dir / filename
            
            # Automatic screenshot of main display
            subprocess.run([
                'screencapture', 
                '-T', '2',  # 2 second delay
                str(screenshot_path)
            ], check=True)
            
            print(f"✅ Captured: {description}")
            return True
        except Exception as e:
            print(f"❌ Failed to capture {description}: {e}")
            return False
    
    def capture_app_screens(self):
        """Guide user through capturing app screens"""
        print("\n📸 Capturing Real C-Cube App Screenshots...")
        print("=" * 60)
        
        # Open the app in browser
        if not self.open_browser_to_app():
            return None
        
        print("\n🎯 INSTRUCTIONS:")
        print("1. Make sure your C-Cube app is visible in the browser")
        print("2. When prompted, click on the browser window to select it")
        print("3. Screenshots will be taken automatically")
        print("\nPress Enter when ready...")
        input()
        
        # Take screenshots
        screenshots = [
            ("01_welcome_screen_real.png", "Welcome Screen"),
            ("02_current_view_real.png", "Current App View"),
        ]
        
        for filename, description in screenshots:
            print(f"\n📸 Taking screenshot: {description}")
            print("Click on your browser window in the next 5 seconds...")
            self.take_screenshot(filename, description)
            time.sleep(2)
        
        print(f"\n✅ Screenshots saved to: {self.output_dir.absolute()}")
        return self.output_dir

def main():
    """Capture real screenshots of C-Cube app"""
    print("📸 C-CUBE macOS SCREENSHOT CAPTURER")
    print("🚀 Taking actual screenshots of your running React app")
    print("=" * 60)
    
    capturer = CCubeMacOSScreenshotCapturer()
    output_dir = capturer.capture_app_screens()
    
    if output_dir:
        print(f"\n🎉 SUCCESS! Real screenshots captured in: {output_dir}")
        print("📱 These are ACTUAL screenshots of your running React app")
        
        # Open output directory
        subprocess.run(['open', str(output_dir)])
    else:
        print("❌ Screenshot capture failed")

if __name__ == "__main__":
    main()