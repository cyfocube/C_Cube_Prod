#!/usr/bin/env python3
"""
C-Cube Interactive Screenshot Capturer
Uses macOS screencapture to take real screenshots while you navigate your app
"""

import time
import subprocess
from pathlib import Path

class CCubeInteractiveCapturer:
    """Interactive screenshot capturer for your running app"""
    
    def __init__(self):
        self.output_dir = Path("interactive_app_screenshots")
        self.output_dir.mkdir(exist_ok=True)
        
        self.app_url = "http://localhost:3000"
        
        print("📸 C-Cube Interactive Screenshot Capturer")
        print(f"📁 Output: {self.output_dir}")
        print(f"🌐 App URL: {self.app_url}")
        print("✨ Taking screenshots while YOU navigate your app")
    
    def open_app_in_browser(self):
        """Open your app in the default browser"""
        try:
            print("🌐 Opening your C-Cube app in browser...")
            subprocess.run(['open', self.app_url], check=True)
            print("✅ App opened in browser")
            return True
        except Exception as e:
            print(f"❌ Failed to open browser: {e}")
            return False
    
    def take_manual_screenshot(self, filename, description):
        """Take a screenshot using macOS screencapture"""
        try:
            screenshot_path = self.output_dir / filename
            
            print(f"\n📸 Ready to capture: {description}")
            print("🎯 Instructions:")
            print("1. Make sure your browser with the C-Cube app is visible")
            print("2. Navigate to the screen you want to capture")
            print("3. Press ENTER when ready")
            print("4. You'll have 3 seconds, then click on your browser window")
            
            input("Press ENTER when ready...")
            
            print("📸 Taking screenshot in 3 seconds...")
            print("👆 Get ready to click on your browser window!")
            
            # Use screencapture with window selection
            subprocess.run([
                'screencapture', 
                '-T', '3',      # 3 second delay
                '-w',           # Interactive window selection
                str(screenshot_path)
            ], check=True)
            
            if screenshot_path.exists():
                print(f"✅ Screenshot saved: {filename}")
                return True
            else:
                print(f"❌ Screenshot failed: {filename}")
                return False
                
        except Exception as e:
            print(f"❌ Screenshot error: {e}")
            return False
    
    def take_automatic_screenshot(self, filename, description):
        """Take automatic full-screen screenshot"""
        try:
            screenshot_path = self.output_dir / filename
            
            print(f"\n📸 Taking automatic screenshot: {description}")
            print("🎯 Make sure your app is visible on screen")
            print("⏱️ Taking screenshot in 2 seconds...")
            
            time.sleep(2)
            
            # Automatic full screen capture
            subprocess.run([
                'screencapture', 
                str(screenshot_path)
            ], check=True)
            
            if screenshot_path.exists():
                print(f"✅ Full screen screenshot saved: {filename}")
                return True
            else:
                print(f"❌ Screenshot failed: {filename}")
                return False
                
        except Exception as e:
            print(f"❌ Screenshot error: {e}")
            return False
    
    def capture_app_interactively(self):
        """Guide user through capturing their app screens"""
        print("\n📸 Interactive C-Cube App Screenshot Session")
        print("=" * 60)
        
        # Open the app
        if not self.open_app_in_browser():
            return None
        
        print("\n⏱️ Waiting 5 seconds for app to load...")
        time.sleep(5)
        
        # Define screens to capture
        screens_to_capture = [
            ("01_welcome_screen.png", "Welcome/Home Screen"),
            ("02_setup_screen.png", "Setup Wallet Screen"),
            ("03_main_wallet.png", "Main Wallet Interface"),
            ("04_current_view.png", "Any Other Screen You Want"),
        ]
        
        successful_captures = 0
        
        print("\n🎮 INTERACTIVE SCREENSHOT SESSION")
        print("📱 Navigate your app and we'll capture each screen")
        print("-" * 50)
        
        for filename, description in screens_to_capture:
            print(f"\n🎯 Next: {description}")
            choice = input("Choose capture method: (w)indow selection, (f)ull screen, or (s)kip: ").lower()
            
            if choice == 'w':
                if self.take_manual_screenshot(filename, description):
                    successful_captures += 1
            elif choice == 'f':
                if self.take_automatic_screenshot(filename, description):
                    successful_captures += 1
            elif choice == 's':
                print(f"⏭️ Skipped: {description}")
            else:
                print("❓ Invalid choice, skipping...")
            
            time.sleep(1)
        
        print(f"\n📊 Session complete: {successful_captures} screenshots captured")
        
        if successful_captures > 0:
            print(f"📁 Screenshots saved in: {self.output_dir.absolute()}")
            
            # Open the directory
            subprocess.run(['open', str(self.output_dir)])
            return self.output_dir
        else:
            print("❌ No screenshots were captured")
            return None

def main():
    """Interactive screenshot capture session"""
    print("📸 C-CUBE INTERACTIVE SCREENSHOT CAPTURER")
    print("🚀 You navigate, I capture your REAL app screens")
    print("=" * 60)
    
    capturer = CCubeInteractiveCapturer()
    result = capturer.capture_app_interactively()
    
    if result:
        print(f"\n🎉 SUCCESS! Interactive screenshots captured!")
        print("📱 These show your REAL C-Cube app as you see it")
        print("🎯 Finally we have authentic UI screenshots!")
    else:
        print("\n❌ No screenshots captured")
        print("💡 Make sure your app is running and visible in browser")

if __name__ == "__main__":
    main()