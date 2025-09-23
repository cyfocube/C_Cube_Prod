#!/usr/bin/env python3
"""
C-Cube Simple Screenshot Capturer
Takes real screenshots of your running React app using requests and headless browser
"""

import time
import subprocess
from pathlib import Path

class CCubeSimpleScreenshotCapturer:
    """Simple screenshot capturer for your running app"""
    
    def __init__(self):
        self.output_dir = Path("actual_app_screenshots")
        self.output_dir.mkdir(exist_ok=True)
        
        self.app_url = "http://localhost:3000"
        
        print("📸 C-Cube Simple Screenshot Capturer")
        print(f"📁 Output: {self.output_dir}")
        print(f"🌐 App URL: {self.app_url}")
        print("✨ Taking screenshots of your REAL running app")
    
    def take_screenshot_with_chrome(self):
        """Use Chrome headless to take screenshot"""
        try:
            screenshot_path = self.output_dir / "app_screenshot_real.png"
            
            # Use Chrome in headless mode to take screenshot
            cmd = [
                '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                '--headless',
                '--disable-gpu',
                '--window-size=1200,800',
                '--screenshot=' + str(screenshot_path),
                self.app_url
            ]
            
            print("📸 Taking screenshot with Chrome...")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0 and screenshot_path.exists():
                print(f"✅ Screenshot saved: {screenshot_path}")
                return screenshot_path
            else:
                print(f"❌ Chrome screenshot failed: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"❌ Chrome screenshot error: {e}")
            return None
    
    def take_screenshot_with_webkit2png(self):
        """Try using webkit2png if available"""
        try:
            screenshot_path = self.output_dir / "app_webkit_screenshot.png"
            
            cmd = [
                'webkit2png',
                '--width=1200',
                '--height=800',
                '--fullsize',
                '--output=' + str(self.output_dir),
                '--filename=app_webkit_screenshot',
                self.app_url
            ]
            
            print("📸 Taking screenshot with webkit2png...")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print(f"✅ Webkit screenshot saved: {screenshot_path}")
                return screenshot_path
            else:
                print(f"⚠️ webkit2png not available or failed")
                return None
                
        except Exception as e:
            print(f"⚠️ webkit2png error: {e}")
            return None
    
    def take_screenshot_with_curlchrome(self):
        """Use curl to check if app is running, then screenshot"""
        try:
            # First check if app is responding
            print("🔍 Checking if app is running...")
            result = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', self.app_url], 
                                   capture_output=True, text=True, timeout=10)
            
            if result.stdout.strip() == '200':
                print("✅ App is responding!")
                
                # Try to take screenshot using screencapture after opening in browser
                print("🌐 Opening app in browser...")
                subprocess.run(['open', self.app_url], check=True)
                
                print("⏱️ Waiting 5 seconds for app to load...")
                time.sleep(5)
                
                # Take screenshot of entire screen
                screenshot_path = self.output_dir / "fullscreen_with_app.png"
                result = subprocess.run(['screencapture', str(screenshot_path)], check=True)
                
                print(f"✅ Full screen screenshot saved: {screenshot_path}")
                print("💡 This includes your browser with the app open")
                return screenshot_path
            else:
                print(f"❌ App not responding. HTTP code: {result.stdout}")
                return None
                
        except Exception as e:
            print(f"❌ Screenshot error: {e}")
            return None
    
    def capture_app(self):
        """Try multiple methods to capture your app"""
        print("\n📸 Capturing Your Running C-Cube App...")
        print("=" * 60)
        
        # Try different methods
        methods = [
            ("Chrome Headless", self.take_screenshot_with_chrome),
            ("webkit2png", self.take_screenshot_with_webkit2png),
            ("Screen Capture", self.take_screenshot_with_curlchrome),
        ]
        
        successful_screenshots = []
        
        for method_name, method_func in methods:
            print(f"\n🔄 Trying: {method_name}")
            try:
                result = method_func()
                if result:
                    successful_screenshots.append((method_name, result))
                    print(f"✅ {method_name} successful!")
                else:
                    print(f"❌ {method_name} failed")
            except Exception as e:
                print(f"❌ {method_name} error: {e}")
        
        print(f"\n📊 Results: {len(successful_screenshots)} successful screenshots")
        
        if successful_screenshots:
            print(f"📁 Screenshots saved in: {self.output_dir.absolute()}")
            
            for method_name, file_path in successful_screenshots:
                print(f"  📸 {method_name}: {file_path.name}")
            
            # Open the directory
            subprocess.run(['open', str(self.output_dir)])
            return self.output_dir
        else:
            print("❌ No screenshots were successful")
            return None

def main():
    """Capture screenshots of running C-Cube app"""
    print("📸 C-CUBE SIMPLE SCREENSHOT CAPTURER")
    print("🚀 Capturing your REAL running React app")
    print("=" * 60)
    
    capturer = CCubeSimpleScreenshotCapturer()
    result = capturer.capture_app()
    
    if result:
        print(f"\n🎉 SUCCESS! Screenshots captured!")
        print("📱 These show your ACTUAL running C-Cube app")
        print("🎯 Finally we can see what your UI really looks like!")
    else:
        print("\n❌ Could not capture screenshots")
        print("💡 Make sure your app is running at http://localhost:3000")

if __name__ == "__main__":
    main()