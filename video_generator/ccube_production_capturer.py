#!/usr/bin/env python3
"""
C-Cube Production Build Screenshot Capturer
Captures screenshots from the production build served at localhost:3001
"""

import time
import subprocess
from pathlib import Path

class CCubeProductionCapturer:
    """Capture screenshots from production build"""
    
    def __init__(self):
        self.output_dir = Path("production_screenshots")
        self.output_dir.mkdir(exist_ok=True)
        
        self.app_url = "http://localhost:3001"
        
        print("📸 C-Cube Production Build Screenshot Capturer")
        print(f"📁 Output: {self.output_dir}")
        print(f"🌐 Production URL: {self.app_url}")
        print("✨ Capturing from production build")
    
    def test_app_accessibility(self):
        """Test if the production app is accessible"""
        try:
            result = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', self.app_url], 
                                   capture_output=True, text=True, timeout=10)
            
            if result.stdout.strip() == '200':
                print("✅ Production app is accessible!")
                return True
            else:
                print(f"❌ Production app returned HTTP {result.stdout}")
                return False
        except Exception as e:
            print(f"❌ Cannot access production app: {e}")
            return False
    
    def capture_with_chrome(self, url, filename, description):
        """Capture using Chrome with better settings"""
        try:
            screenshot_path = self.output_dir / filename
            
            # Chrome command with more flags to handle local apps
            cmd = [
                '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                '--headless',
                '--disable-gpu',
                '--disable-web-security',
                '--disable-features=VizDisplayCompositor',
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--window-size=1200,800',
                '--virtual-time-budget=2000',  # Wait 2 seconds for page load
                '--run-all-compositor-stages-before-draw',
                '--screenshot=' + str(screenshot_path),
                url
            ]
            
            print(f"📸 Capturing: {description}")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0 and screenshot_path.exists():
                file_size = screenshot_path.stat().st_size
                print(f"✅ Captured: {filename} ({file_size} bytes)")
                return True
            else:
                print(f"❌ Failed: {description}")
                if result.stderr:
                    print(f"   Error: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Error capturing {description}: {e}")
            return False
    
    def capture_production_screenshots(self):
        """Capture screenshots from production build"""
        print("\n📸 Capturing Production Build Screenshots...")
        print("=" * 60)
        
        # Test accessibility first
        if not self.test_app_accessibility():
            print("❌ Cannot access production app")
            return None
        
        # Wait a moment for server to be ready
        print("⏱️ Waiting for production server to be ready...")
        time.sleep(3)
        
        # Pages to capture
        pages = [
            (self.app_url, "01_production_home.png", "Production Home Page"),
            (f"{self.app_url}/", "02_production_root.png", "Production Root"),
            (f"{self.app_url}/#/", "03_production_hash_root.png", "Production Hash Root"),
        ]
        
        successful = 0
        
        for url, filename, description in pages:
            if self.capture_with_chrome(url, filename, description):
                successful += 1
            time.sleep(2)  # Wait between captures
        
        print(f"\n📊 Successfully captured {successful}/{len(pages)} screenshots")
        
        if successful > 0:
            print(f"📁 Screenshots saved in: {self.output_dir.absolute()}")
            subprocess.run(['open', str(self.output_dir)])
            return self.output_dir
        else:
            print("❌ No screenshots were successful")
            return None

def main():
    """Capture production build screenshots"""
    print("📸 C-CUBE PRODUCTION SCREENSHOT CAPTURER")
    print("🚀 Capturing from production build at localhost:3001")
    print("=" * 60)
    
    capturer = CCubeProductionCapturer()
    result = capturer.capture_production_screenshots()
    
    if result:
        print(f"\n🎉 SUCCESS! Production screenshots captured!")
        print("📱 These should show your real production app UI")
    else:
        print("\n❌ Production screenshot capture failed")

if __name__ == "__main__":
    main()