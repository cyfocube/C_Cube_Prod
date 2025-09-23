#!/usr/bin/env python3
"""
C-Cube Safari Screenshot Capturer
Uses Safari AppleScript automation to capture real screenshots
"""

import subprocess
import time
from pathlib import Path

class CCubeSafariCapturer:
    """Use Safari and AppleScript to capture screenshots"""
    
    def __init__(self):
        self.output_dir = Path("safari_screenshots")
        self.output_dir.mkdir(exist_ok=True)
        self.app_url = "http://localhost:3000"
        
        print("📸 C-Cube Safari Screenshot Capturer")
        print(f"📁 Output: {self.output_dir}")
        print("✨ Using Safari + AppleScript automation")
    
    def capture_with_safari_automation(self):
        """Use AppleScript to control Safari and take screenshots"""
        
        # AppleScript to open Safari and navigate to app
        applescript = f'''
        tell application "Safari"
            activate
            if (count of windows) = 0 then
                make new document
            end if
            set URL of front document to "{self.app_url}"
            delay 3
        end tell
        '''
        
        try:
            print("🌐 Opening app in Safari...")
            subprocess.run(['osascript', '-e', applescript], check=True)
            print("✅ App opened in Safari")
            
            # Wait for page to load
            time.sleep(5)
            
            # Take screenshot
            screenshot_path = self.output_dir / "safari_app_screenshot.png"
            
            # Use screencapture to capture Safari window
            print("📸 Taking screenshot...")
            subprocess.run([
                'screencapture', 
                '-T', '2',
                '-w',  # Window selection
                str(screenshot_path)
            ], check=True)
            
            print(f"✅ Screenshot saved: {screenshot_path}")
            return screenshot_path
            
        except Exception as e:
            print(f"❌ Safari automation failed: {e}")
            return None
    
    def quick_screenshot_guide(self):
        """Quick guide for manual screenshots"""
        print("\n📸 Quick Screenshot Method")
        print("=" * 40)
        
        # Open app in Safari
        try:
            subprocess.run(['open', '-a', 'Safari', self.app_url], check=True)
            print("✅ Opened in Safari")
        except:
            print("❌ Please open Safari manually")
        
        print("\n🎯 QUICK STEPS:")
        print("1. Make sure Safari shows your C-Cube app")
        print("2. Press Cmd+Shift+4, then Spacebar")
        print("3. Click on Safari window")
        print("4. Screenshot saved to Desktop")
        print()
        print("Take 2-3 screenshots of different app screens")
        print(f"Move them to: {self.output_dir.absolute()}")
        
        # Open output folder
        subprocess.run(['open', str(self.output_dir)])
        
        return self.output_dir

def main():
    """Try Safari-based screenshot capture"""
    print("📸 C-CUBE SAFARI SCREENSHOT CAPTURER")
    print("🚀 Using Safari for better localhost compatibility")
    print("=" * 60)
    
    capturer = CCubeSafariCapturer()
    
    print("Choose method:")
    print("1. Automated Safari capture")
    print("2. Quick manual guide")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        result = capturer.capture_with_safari_automation()
        if result:
            print(f"🎉 Automated capture successful!")
        else:
            print("❌ Automated capture failed, try manual method")
    else:
        result = capturer.quick_screenshot_guide()
        print("📱 Manual screenshot guide ready!")
    
    if result:
        print(f"\n📁 Screenshots location: {result}")

if __name__ == "__main__":
    main()