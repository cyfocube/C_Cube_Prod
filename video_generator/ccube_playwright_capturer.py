#!/usr/bin/env python3
"""
C-Cube Playwright Screenshot Capturer
Uses Playwright to take real screenshots of your running React app
"""

import asyncio
import time
from pathlib import Path
from playwright.async_api import async_playwright

class CCubePlaywrightCapturer:
    """Capture real screenshots using Playwright"""
    
    def __init__(self):
        self.output_dir = Path("real_playwright_screenshots")
        self.output_dir.mkdir(exist_ok=True)
        
        self.app_url = "http://localhost:3000"
        
        print("📸 C-Cube Playwright Screenshot Capturer")
        print(f"📁 Output: {self.output_dir}")
        print(f"🌐 App URL: {self.app_url}")
        print("✨ Using Playwright to capture REAL running React app")
    
    async def capture_screenshots(self):
        """Capture screenshots of your running app"""
        async with async_playwright() as p:
            # Launch browser
            browser = await p.chromium.launch(headless=False)  # Visible browser
            context = await browser.new_context(
                viewport={'width': 1200, 'height': 800}
            )
            page = await context.new_page()
            
            try:
                print("🌐 Navigating to your app...")
                await page.goto(self.app_url, wait_until='networkidle')
                
                # Wait a moment for any animations
                await page.wait_for_timeout(2000)
                
                # Take screenshot of welcome screen
                welcome_path = self.output_dir / "01_welcome_screen_real.png"
                await page.screenshot(path=str(welcome_path), full_page=True)
                print(f"✅ Captured: Welcome Screen → {welcome_path}")
                
                # Try to interact with the app to get more screens
                
                # Look for "Create New Wallet" button and click it
                try:
                    create_button = page.locator('text="Create New Wallet"').first
                    if await create_button.is_visible():
                        await create_button.click()
                        await page.wait_for_timeout(2000)
                        
                        setup_path = self.output_dir / "02_setup_screen_real.png"
                        await page.screenshot(path=str(setup_path), full_page=True)
                        print(f"✅ Captured: Setup Screen → {setup_path}")
                except Exception as e:
                    print(f"⚠️ Could not navigate to setup: {e}")
                
                # Try to navigate to different routes
                routes_to_try = ['/wallet', '/setup', '/resources']
                
                for route in routes_to_try:
                    try:
                        await page.goto(f"{self.app_url}{route}", wait_until='networkidle')
                        await page.wait_for_timeout(2000)
                        
                        route_name = route.replace('/', '').replace('', 'home')
                        screenshot_path = self.output_dir / f"03_{route_name}_screen_real.png"
                        await page.screenshot(path=str(screenshot_path), full_page=True)
                        print(f"✅ Captured: {route_name.title()} Screen → {screenshot_path}")
                    except Exception as e:
                        print(f"⚠️ Could not capture {route}: {e}")
                
                # Go back to home and take final screenshot
                await page.goto(self.app_url, wait_until='networkidle')
                await page.wait_for_timeout(1000)
                
                final_path = self.output_dir / "04_final_app_state.png"
                await page.screenshot(path=str(final_path), full_page=True)
                print(f"✅ Captured: Final App State → {final_path}")
                
            finally:
                await browser.close()
                print("🔒 Browser closed")
        
        return self.output_dir
    
    def run_capture(self):
        """Run the screenshot capture"""
        return asyncio.run(self.capture_screenshots())

def main():
    """Capture real screenshots of C-Cube app"""
    print("📸 C-CUBE PLAYWRIGHT SCREENSHOT CAPTURER")
    print("🚀 Taking actual screenshots of your running React app")
    print("=" * 60)
    
    capturer = CCubePlaywrightCapturer()
    
    try:
        output_dir = capturer.run_capture()
        
        print(f"\n🎉 SUCCESS! Real screenshots captured in: {output_dir.absolute()}")
        print("📱 These are ACTUAL screenshots of your running React app")
        print("🎯 Finally showing your REAL UI!")
        
        # Open output directory
        import subprocess
        subprocess.run(['open', str(output_dir)])
        
    except Exception as e:
        print(f"❌ Screenshot capture failed: {e}")
        print("💡 Make sure your React app is running at http://localhost:3000")

if __name__ == "__main__":
    main()