#!/usr/bin/env python3
"""
ElevenLabs Setup and Configuration Helper
Helps set up ElevenLabs API key and test voice generation
"""

import os
import requests
import json
from pathlib import Path

def setup_elevenlabs():
    """Interactive setup for ElevenLabs API"""
    print("🎵 ElevenLabs AI Voice Setup")
    print("=" * 40)
    
    # Check if API key already exists
    existing_key = os.getenv('ELEVENLABS_API_KEY')
    if existing_key:
        print(f"✅ API key already configured: {existing_key[:8]}...")
        use_existing = input("Use existing key? (y/n): ").lower().strip()
        if use_existing == 'y':
            return existing_key
    
    print("\n📝 To get your free ElevenLabs API key:")
    print("1. Visit: https://elevenlabs.io")
    print("2. Sign up for a free account")
    print("3. Go to Profile -> API Keys")
    print("4. Copy your API key")
    print("\n💰 Free tier includes 10,000 characters per month")
    
    api_key = input("\n🔑 Enter your ElevenLabs API key (or press Enter to skip): ").strip()
    
    if api_key:
        # Test the API key
        print("\n🧪 Testing API key...")
        if test_api_key(api_key):
            print("✅ API key is valid!")
            
            # Offer to save it permanently
            save_key = input("Save API key to environment? (y/n): ").lower().strip()
            if save_key == 'y':
                save_api_key_to_env(api_key)
            
            return api_key
        else:
            print("❌ API key test failed. Please check your key.")
            return None
    else:
        print("⚠️  Skipping ElevenLabs setup. Will use system TTS.")
        return None

def test_api_key(api_key):
    """Test if the API key is valid"""
    try:
        url = "https://api.elevenlabs.io/v1/voices"
        headers = {"xi-api-key": api_key}
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            voices = response.json().get('voices', [])
            print(f"   Found {len(voices)} available voices")
            return True
        else:
            print(f"   API error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   Connection error: {e}")
        return False

def save_api_key_to_env(api_key):
    """Save API key to shell profile"""
    home = Path.home()
    
    # Try different shell profiles
    profiles = ['.zshrc', '.bash_profile', '.bashrc']
    
    for profile in profiles:
        profile_path = home / profile
        if profile_path.exists() or profile == '.zshrc':  # Default to zsh on macOS
            try:
                with open(profile_path, 'a') as f:
                    f.write(f"\n# ElevenLabs API Key\nexport ELEVENLABS_API_KEY='{api_key}'\n")
                
                print(f"✅ API key saved to {profile_path}")
                print("   Restart your terminal or run: source ~/.zshrc")
                return True
            except Exception as e:
                print(f"   Error saving to {profile_path}: {e}")
    
    print("⚠️  Could not save API key automatically.")
    print(f"   Manually add this line to your shell profile:")
    print(f"   export ELEVENLABS_API_KEY='{api_key}'")
    return False

def list_available_voices(api_key):
    """List available ElevenLabs voices"""
    if not api_key:
        print("❌ No API key provided")
        return
    
    try:
        url = "https://api.elevenlabs.io/v1/voices"
        headers = {"xi-api-key": api_key}
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            voices = response.json().get('voices', [])
            
            print(f"\n🎵 Available ElevenLabs Voices ({len(voices)}):")
            print("-" * 50)
            
            for voice in voices[:10]:  # Show first 10
                name = voice.get('name', 'Unknown')
                voice_id = voice.get('voice_id', 'Unknown')
                labels = voice.get('labels', {})
                gender = labels.get('gender', 'Unknown')
                accent = labels.get('accent', 'Unknown')
                
                print(f"🎤 {name}")
                print(f"   ID: {voice_id}")
                print(f"   Gender: {gender}, Accent: {accent}")
                print()
        else:
            print(f"❌ Failed to fetch voices: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error fetching voices: {e}")

def test_voice_generation(api_key):
    """Test voice generation with a sample"""
    if not api_key:
        print("❌ No API key for testing")
        return
    
    print("\n🧪 Testing voice generation...")
    
    try:
        url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"  # Adam voice
        
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": api_key
        }
        
        data = {
            "text": "Hello, this is a test of ElevenLabs AI voice generation for C-Cube cryptocurrency tutorials.",
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.8,
                "similarity_boost": 0.7
            }
        }
        
        response = requests.post(url, json=data, headers=headers, timeout=30)
        
        if response.status_code == 200:
            test_file = Path("elevenlabs_test.mp3")
            with open(test_file, 'wb') as f:
                f.write(response.content)
            
            print("✅ Test audio generated successfully!")
            print(f"   Saved as: {test_file}")
            
            # Try to play it
            try:
                os.system(f"open '{test_file}'")
                print("🔊 Playing test audio...")
            except:
                print("   You can manually play the test file")
            
            return True
        else:
            error = response.json().get('detail', {})
            print(f"❌ Generation failed: {error}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🤖 C-Cube ElevenLabs Voice Setup")
    print("🚀 Professional AI voice for cryptocurrency education")
    print("=" * 55)
    
    # Setup API key
    api_key = setup_elevenlabs()
    
    if api_key:
        print("\n🎵 ElevenLabs Features:")
        print("✅ Ultra-realistic AI voices")
        print("✅ Professional quality audio")
        print("✅ Multiple voice personalities") 
        print("✅ Robotic processing effects")
        print("✅ Conversational tone optimization")
        
        # Show available voices
        show_voices = input("\n👀 Show available voices? (y/n): ").lower().strip()
        if show_voices == 'y':
            list_available_voices(api_key)
        
        # Test voice generation
        test_gen = input("\n🧪 Test voice generation? (y/n): ").lower().strip()
        if test_gen == 'y':
            test_voice_generation(api_key)
        
        print("\n🎬 Ready to generate professional C-Cube tutorial!")
        print("   Run: python ccube_elevenlabs_generator.py")
    else:
        print("\n🔄 No ElevenLabs API key configured.")
        print("   The generator will use enhanced system TTS as fallback.")
        print("   Run: python ccube_enhanced_robotic_generator.py")
    
    print("\n✨ Setup complete!")

if __name__ == "__main__":
    main()