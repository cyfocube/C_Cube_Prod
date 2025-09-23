#!/usr/bin/env python3
"""
C-Cube Real Screenshot Capturer
Takes actual screenshots of your running React app
Uses Selenium WebDriver to capture the real UI
"""

import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CCubeRealScreenshotCapturer:
    """Capture real screenshots of your running C-Cube app"""
    
    def __init__(self):
        self.output_dir = Path("real_ui_screenshots")
        self.output_dir.mkdir(exist_ok=True)
        
        self.app_url = "http://localhost:3000"
        
        print("📸 C-Cube Real Screenshot Capturer")
        print(f"📁 Output: {self.output_dir}")
        print(f"🌐 App URL: {self.app_url}")
        print("✨ Capturing REAL UI from your running React app")
    
    def setup_driver(self):
        """Setup Chrome WebDriver for screenshots"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--window-size=1200,800")  # Set window size
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        chrome_options.add_argument("--hide-scrollbars")
        
        try:
            # Try to create Chrome driver
            driver = webdriver.Chrome(options=chrome_options)
            print("✅ Chrome WebDriver initialized")
            return driver
        except Exception as e:
            print(f"❌ Chrome WebDriver failed: {e}")
            print("💡 Please install ChromeDriver or use a different browser")
            return None
    
    def capture_screenshot(self, driver, filename, description):
        """Capture a screenshot and save it"""
        try:
            # Wait a moment for page to load
            time.sleep(2)
            
            # Take screenshot
            screenshot_path = self.output_dir / filename
            driver.save_screenshot(str(screenshot_path))
            
            print(f"✅ Captured: {description}")
            return True
        except Exception as e:
            print(f"❌ Failed to capture {description}: {e}")
            return False
    
    def capture_welcome_screen(self, driver):
        """Capture the welcome screen"""
        driver.get(self.app_url)
        
        # Wait for the page to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except:
            pass
        
        self.capture_screenshot(driver, "01_welcome_screen_real.png", "Real Welcome Screen")
    
    def capture_security_prompt(self, driver):
        """Capture security prompt if it appears"""
        # Security prompt might appear automatically or need to be triggered
        # We'll wait a moment and capture if it's there
        time.sleep(1)
        self.capture_screenshot(driver, "02_security_prompt_real.png", "Real Security Prompt")
    
    def capture_setup_screen(self, driver):
        """Navigate to setup and capture"""
        try:
            # Look for setup/create wallet button and click it
            create_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create') or contains(text(), 'Setup')]")
            create_button.click()
            
            time.sleep(2)  # Wait for navigation
            self.capture_screenshot(driver, "03_setup_wallet_real.png", "Real Setup Wallet")
        except Exception as e:
            print(f"⚠️  Could not navigate to setup: {e}")
    
    def capture_main_wallet(self, driver):
        """Navigate to main wallet interface"""
        try:
            # Try to navigate to the main wallet view
            driver.get(f"{self.app_url}/wallet")
            time.sleep(2)
            self.capture_screenshot(driver, "04_main_wallet_real.png", "Real Main Wallet")
        except Exception as e:
            print(f"⚠️  Could not navigate to main wallet: {e}")
    
    def capture_all_screens(self):
        """Capture all app screens"""
        print("\n📸 Capturing Real C-Cube App Screenshots...")
        print("=" * 60)
        
        driver = self.setup_driver()
        if not driver:
            print("❌ Cannot proceed without WebDriver")
            return None
        
        try:
            # Capture all screens
            self.capture_welcome_screen(driver)
            self.capture_security_prompt(driver)
            self.capture_setup_screen(driver)
            self.capture_main_wallet(driver)
            
            print(f"\n✅ Real screenshots saved to: {self.output_dir.absolute()}")
            return self.output_dir
            
        finally:
            driver.quit()
            print("🔒 WebDriver closed")

def install_selenium():
    """Install selenium if not available"""
    try:
        import selenium
        return True
    except ImportError:
        print("📦 Installing selenium...")
        import subprocess
        subprocess.check_call(["pip", "install", "selenium"])
        return True

def main():
    """Capture real screenshots of C-Cube app"""
    print("📸 C-CUBE REAL SCREENSHOT CAPTURER")
    print("🚀 Taking actual screenshots of your running React app")
    print("=" * 60)
    
    # Install selenium if needed
    if not install_selenium():
        print("❌ Failed to install selenium")
        return
    
    capturer = CCubeRealScreenshotCapturer()
    output_dir = capturer.capture_all_screens()
    
    if output_dir:
        print(f"\n🎉 SUCCESS! Real screenshots captured in: {output_dir}")
        print("📱 These are ACTUAL screenshots of your running React app")
        
        # Open output directory
        import subprocess
        subprocess.run(['open', str(output_dir)])
    else:
        print("❌ Screenshot capture failed")

if __name__ == "__main__":
    main()