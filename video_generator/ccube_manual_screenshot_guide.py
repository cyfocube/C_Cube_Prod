#!/usr/bin/env python3
"""
C-Cube Manual Screenshot Guide
Since automated tools are capturing blocked pages, let's do this manually
"""

import subprocess
from pathlib import Path

class CCubeManualScreenshotGuide:
    """Guide user through manual screenshot process"""
    
    def __init__(self):
        self.output_dir = Path("manual_app_screenshots")
        self.output_dir.mkdir(exist_ok=True)
        
        self.app_url = "http://localhost:3000"
        
        print("📸 C-Cube Manual Screenshot Guide")
        print(f"📁 Output: {self.output_dir}")
        print(f"🌐 App URL: {self.app_url}")
        print("✨ Let's capture your REAL app screens manually")
    
    def guide_manual_process(self):
        """Guide user through manual screenshot process"""
        print("\n📸 Manual Screenshot Process")
        print("=" * 60)
        
        print("🎯 Since automated tools are capturing blocked pages,")
        print("   let's do this manually to get your REAL UI")
        print()
        
        # Open the app
        print("1️⃣ Opening your C-Cube app in browser...")
        try:
            subprocess.run(['open', self.app_url], check=True)
            print("✅ App should now be open in your browser")
        except:
            print(f"❌ Please manually open: {self.app_url}")
        
        print("\n2️⃣ Now let's take screenshots manually:")
        print("   I'll guide you through each screen")
        print()
        
        # Define screens we need
        screens_needed = [
            {
                'name': 'Welcome Screen',
                'filename': '01_welcome_screen_manual.png',
                'instructions': [
                    "Navigate to the main/welcome page of your app",
                    "Make sure the full interface is visible",
                    "This should show welcome message and main buttons"
                ]
            },
            {
                'name': 'Setup Wallet Screen', 
                'filename': '02_setup_manual.png',
                'instructions': [
                    "Click 'Create New Wallet' or navigate to setup",
                    "Show the wallet setup/creation interface",
                    "This should show network selection, password fields, etc."
                ]
            },
            {
                'name': 'Main Wallet Interface',
                'filename': '03_wallet_main_manual.png', 
                'instructions': [
                    "Navigate to the main wallet interface",
                    "Show balance, send/receive options",
                    "This should be the primary wallet screen"
                ]
            },
            {
                'name': 'Resources/Settings Screen',
                'filename': '04_resources_manual.png',
                'instructions': [
                    "Navigate to resources or settings",
                    "Show any additional features/options",
                    "Any other important screens"
                ]
            }
        ]
        
        print("🎯 FOR EACH SCREEN:")
        print("   • Navigate to the screen in your browser")
        print("   • Press Cmd+Shift+4, then Spacebar")
        print("   • Click on your browser window")
        print("   • Save to the screenshots folder")
        print()
        
        for i, screen in enumerate(screens_needed, 1):
            print(f"\n{i}️⃣ {screen['name']}:")
            print(f"   📄 Save as: {screen['filename']}")
            print("   🎯 Instructions:")
            for instruction in screen['instructions']:
                print(f"      • {instruction}")
            print(f"   📁 Save to: {self.output_dir.absolute()}")
            
            input("\n   Press ENTER when you've taken this screenshot...")
            print("   ✅ Screenshot noted!")
        
        print("\n🎉 Manual Screenshot Session Complete!")
        print(f"📁 Check your screenshots in: {self.output_dir.absolute()}")
        
        # Open the directory
        subprocess.run(['open', str(self.output_dir)])
        
        return self.output_dir

def main():
    """Guide manual screenshot process"""
    print("📸 C-CUBE MANUAL SCREENSHOT GUIDE")
    print("🚀 Let's capture your REAL app screens manually")
    print("=" * 60)
    
    print("💡 Why manual screenshots?")
    print("   Automated tools are capturing 'blocked page' instead of your app")
    print("   Manual screenshots will show your REAL UI exactly as you see it")
    print()
    
    guide = CCubeManualScreenshotGuide()
    result = guide.guide_manual_process()
    
    print(f"\n🎯 Next Steps:")
    print("1. Check the screenshots you saved")
    print("2. These will show your REAL C-Cube UI")
    print("3. Now I can create accurate tutorial materials!")

if __name__ == "__main__":
    main()