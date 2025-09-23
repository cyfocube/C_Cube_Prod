#!/usr/bin/env python3
"""
C-Cube Multi-Page Screenshot Capturer
Takes screenshots of different pages/routes in your running React app
"""

import time
import subprocess
from pathlib import Path

class CCubeMultiPageCapturer:
    """Capture multiple pages of your running app"""
    
    def __init__(self):
        self.output_dir = Path("complete_app_screenshots")
        self.output_dir.mkdir(exist_ok=True)
        
        self.base_url = "http://localhost:3000"
        
        print("📸 C-Cube Multi-Page Screenshot Capturer")
        print(f"📁 Output: {self.output_dir}")
        print(f"🌐 Base URL: {self.base_url}")
        print("✨ Capturing ALL pages of your running app")
    
    def take_chrome_screenshot(self, url, filename, description):
        """Take screenshot with Chrome"""
        try:
            screenshot_path = self.output_dir / filename
            
            cmd = [
                '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                '--headless',
                '--disable-gpu',
                '--window-size=1200,800',
                '--screenshot=' + str(screenshot_path),
                url
            ]
            
            print(f"📸 Capturing: {description}")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0 and screenshot_path.exists():
                print(f"✅ Saved: {filename}")
                return True
            else:
                print(f"❌ Failed: {description}")
                return False
                
        except Exception as e:
            print(f"❌ Error capturing {description}: {e}")
            return False
    
    def capture_all_pages(self):
        """Capture screenshots of all app pages"""
        print("\n📸 Capturing All C-Cube App Pages...")
        print("=" * 60)
        
        # Define all routes/pages to capture
        pages_to_capture = [
            (self.base_url, "01_home_page.png", "Home/Welcome Page"),
            (f"{self.base_url}/", "02_root_page.png", "Root Page"),
            (f"{self.base_url}/setup", "03_setup_page.png", "Setup Wallet Page"),
            (f"{self.base_url}/wallet", "04_wallet_page.png", "Main Wallet Page"),
            (f"{self.base_url}/cold-wallet", "05_cold_wallet_page.png", "Cold Wallet Page"),
            (f"{self.base_url}/resources", "06_resources_page.png", "Resources Page"),
            (f"{self.base_url}/broadcast", "07_broadcast_page.png", "Broadcast Page"),
        ]
        
        successful_captures = 0
        
        for url, filename, description in pages_to_capture:
            if self.take_chrome_screenshot(url, filename, description):
                successful_captures += 1
            time.sleep(1)  # Brief pause between captures
        
        print(f"\n📊 Successfully captured {successful_captures}/{len(pages_to_capture)} pages")
        
        if successful_captures > 0:
            print(f"📁 All screenshots saved in: {self.output_dir.absolute()}")
            
            # Open the directory
            subprocess.run(['open', str(self.output_dir)])
            return self.output_dir
        else:
            print("❌ No pages were successfully captured")
            return None

def main():
    """Capture all pages of running C-Cube app"""
    print("📸 C-CUBE MULTI-PAGE SCREENSHOT CAPTURER")
    print("🚀 Capturing ALL pages of your running React app")
    print("=" * 60)
    
    capturer = CCubeMultiPageCapturer()
    result = capturer.capture_all_pages()
    
    if result:
        print(f"\n🎉 SUCCESS! Multi-page screenshots captured!")
        print("📱 These show ALL your actual C-Cube app pages")
        print("🎯 Now we can see your complete UI!")
    else:
        print("\n❌ Could not capture app pages")
        print("💡 Make sure your app is running at http://localhost:3000")

if __name__ == "__main__":
    main()