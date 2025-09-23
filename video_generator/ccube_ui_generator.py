#!/usr/bin/env python3
"""
C-Cube UI Mockup Generator
Creates realistic UI mockups for each section of the tutorial guide
Based on the actual C-Cube wallet code structure and styling
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json

class CCubeUIGenerator:
    """Generate C-Cube wallet UI mockups for tutorial sections"""
    
    def __init__(self):
        self.output_dir = Path("ui_mockups")
        self.output_dir.mkdir(exist_ok=True)
        
        # C-Cube theme colors (from GlobalStyle.js)
        self.colors = {
            'primary': (0, 204, 51),      # Matrix green
            'secondary': (11, 42, 2),     # Dark green
            'success': (46, 204, 64),     # Bright green
            'danger': (255, 7, 58),       # Digital red
            'warning': (255, 153, 0),     # Alert amber
            'info': (0, 204, 255),        # Cyber blue
            'background': (12, 12, 12),   # Near black
            'cardBackground': (20, 20, 20), # Dark slate
            'text': (0, 204, 51),         # Matrix green text
            'mutedText': (78, 154, 6),    # Muted green
            'border': (0, 255, 65),       # Bright green borders
            'highlight': (0, 255, 65, 85), # Semi-transparent green
            'accent': (255, 7, 58),       # Red accent
            'overlay': (0, 255, 65, 13),  # Subtle green overlay
        }
        
        # Screen dimensions
        self.width = 1200
        self.height = 800
        
        print("🎨 C-Cube UI Mockup Generator")
        print(f"📁 Output: {self.output_dir}")
        print(f"🖥️  Resolution: {self.width}x{self.height}")
        print("🎨 Style: Cyber/Matrix theme with green terminal aesthetics")
    
    def create_background_with_grid(self):
        """Create the signature C-Cube background with cyber grid"""
        bg = Image.new('RGB', (self.width, self.height), self.colors['background'])
        draw = ImageDraw.Draw(bg)
        
        # Grid pattern
        grid_spacing = 20
        grid_color = (0, 255, 65, 8)  # Very subtle green
        
        # Vertical lines
        for x in range(0, self.width, grid_spacing):
            draw.line([(x, 0), (x, self.height)], fill=self.colors['primary'], width=1)
            
        # Horizontal lines  
        for y in range(0, self.height, grid_spacing):
            draw.line([(0, y), (self.width, y)], fill=self.colors['primary'], width=1)
        
        # Add subtle noise/static effect
        for i in range(500):
            x = hash(str(i * 7)) % self.width
            y = hash(str(i * 11)) % self.height
            alpha = hash(str(i * 13)) % 30 + 10
            noise_color = (0, 255, 65, alpha)
            draw.point((x, y), fill=self.colors['primary'])
        
        return bg
    
    def get_fonts(self):
        """Get appropriate fonts for the cyber theme"""
        try:
            # Try to load Share Tech Mono (C-Cube's actual font)
            title_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 28)
            subtitle_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 20)
            body_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 16)
            small_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 14)
            code_font = ImageFont.truetype("/System/Library/Fonts/Courier.ttc", 12)
        except:
            # Fallback to default fonts
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
            code_font = ImageFont.load_default()
        
        return {
            'title': title_font,
            'subtitle': subtitle_font,
            'body': body_font,
            'small': small_font,
            'code': code_font
        }
    
    def draw_terminal_frame(self, draw, x, y, width, height, title="C-CUBE TERMINAL v1.3.37"):
        """Draw the signature C-Cube terminal frame"""
        # Main frame border
        draw.rectangle([x, y, x + width, y + height], 
                      outline=self.colors['primary'], width=2)
        
        # Terminal header background
        header_height = 30
        draw.rectangle([x + 2, y + 2, x + width - 2, y + header_height], 
                      fill=(0, 40, 10))
        
        # Terminal title
        fonts = self.get_fonts()
        title_bbox = draw.textbbox((0, 0), title, font=fonts['small'])
        title_width = title_bbox[2] - title_bbox[0]
        draw.text((x + 10, y + 8), title, fill=self.colors['primary'], font=fonts['small'])
        
        # Terminal buttons (classic red, yellow, green)
        button_y = y + 8
        button_size = 12
        button_x_start = x + width - 60
        
        # Close button (red)
        draw.ellipse([button_x_start, button_y, button_x_start + button_size, button_y + button_size], 
                    fill=self.colors['danger'])
        
        # Minimize button (yellow)
        draw.ellipse([button_x_start + 20, button_y, button_x_start + 20 + button_size, button_y + button_size], 
                    fill=self.colors['warning'])
        
        # Maximize button (green)
        draw.ellipse([button_x_start + 40, button_y, button_x_start + 40 + button_size, button_y + button_size], 
                    fill=self.colors['success'])
        
        # Return content area coordinates
        return (x + 10, y + header_height + 10, width - 20, height - header_height - 20)
    
    def draw_card(self, draw, x, y, width, height, title=None):
        """Draw a C-Cube style card with cyber styling"""
        # Card background with slight transparency effect
        draw.rectangle([x, y, x + width, y + height], 
                      fill=self.colors['cardBackground'], 
                      outline=self.colors['primary'], width=1)
        
        # Add subtle inner glow
        inner_glow_color = (0, 255, 65, 20)
        draw.rectangle([x + 1, y + 1, x + width - 1, y + height - 1], 
                      outline=self.colors['primary'], width=1)
        
        # Security indicator (top right)
        fonts = self.get_fonts()
        security_text = "SECURE"
        sec_bbox = draw.textbbox((0, 0), security_text, font=fonts['small'])
        sec_width = sec_bbox[2] - sec_bbox[0]
        
        sec_x = x + width - sec_width - 15
        sec_y = y + 8
        draw.rectangle([sec_x - 5, sec_y - 2, sec_x + sec_width + 5, sec_y + 12], 
                      outline=self.colors['primary'], width=1)
        draw.text((sec_x, sec_y), security_text, fill=self.colors['primary'], font=fonts['small'])
        
        # Title if provided
        title_y = y + 15
        if title:
            draw.text((x + 15, title_y), title, fill=self.colors['primary'], font=fonts['subtitle'])
            title_y += 35
        
        return (x + 15, title_y, width - 30, height - (title_y - y) - 15)
    
    def draw_button(self, draw, x, y, width, height, text, style='primary'):
        """Draw a C-Cube style button"""
        fonts = self.get_fonts()
        
        # Button colors based on style
        if style == 'primary':
            bg_color = self.colors['primary']
            text_color = (0, 0, 0)
        elif style == 'secondary':
            bg_color = self.colors['secondary'] 
            text_color = self.colors['text']
        elif style == 'danger':
            bg_color = self.colors['danger']
            text_color = (255, 255, 255)
        else:
            bg_color = self.colors['cardBackground']
            text_color = self.colors['text']
        
        # Draw button background
        draw.rectangle([x, y, x + width, y + height], 
                      fill=bg_color, outline=self.colors['border'], width=1)
        
        # Button text (centered)
        text_bbox = draw.textbbox((0, 0), text, font=fonts['body'])
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        text_x = x + (width - text_width) // 2
        text_y = y + (height - text_height) // 2
        
        draw.text((text_x, text_y), text, fill=text_color, font=fonts['body'])
    
    def draw_input_field(self, draw, x, y, width, height, placeholder="", value=""):
        """Draw a C-Cube style input field"""
        fonts = self.get_fonts()
        
        # Input background
        draw.rectangle([x, y, x + width, y + height], 
                      fill=self.colors['background'], 
                      outline=self.colors['border'], width=1)
        
        # Input text
        display_text = value if value else placeholder
        text_color = self.colors['text'] if value else self.colors['mutedText']
        
        draw.text((x + 10, y + 8), display_text, fill=text_color, font=fonts['body'])
        
        # Cursor if there's a value
        if value:
            cursor_x = x + 10 + len(value) * 8
            draw.line([(cursor_x, y + 5), (cursor_x, y + height - 5)], 
                     fill=self.colors['primary'], width=2)
    
    def create_welcome_screen(self):
        """Create the Welcome Screen UI mockup"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Main container (centered)
        container_width = 600
        container_height = 400
        container_x = (self.width - container_width) // 2
        container_y = (self.height - container_height) // 2
        
        # Welcome card
        card_x, card_y, card_width, card_height = self.draw_card(
            draw, container_x, container_y, container_width, container_height
        )
        
        # C-Cube logo/title
        title = "Welcome to C-Cube"
        title_bbox = draw.textbbox((0, 0), title, font=fonts['title'])
        title_width = title_bbox[2] - title_bbox[0]
        title_x = card_x + (card_width - title_width) // 2
        
        draw.text((title_x, card_y), title, fill=self.colors['primary'], font=fonts['title'])
        
        # Subtitle
        subtitle = "Your secure offline cryptocurrency wallet solution."
        subtitle2 = "Get started by creating a new wallet or recovering an existing one."
        
        draw.text((card_x, card_y + 50), subtitle, fill=self.colors['text'], font=fonts['body'])
        draw.text((card_x, card_y + 75), subtitle2, fill=self.colors['text'], font=fonts['body'])
        
        # Buttons
        button_width = 300
        button_height = 50
        button_x = card_x + (card_width - button_width) // 2
        
        # Create New Wallet button
        self.draw_button(draw, button_x, card_y + 150, button_width, button_height, 
                        "➕ Create New Wallet", 'primary')
        
        # Recover Wallet button
        self.draw_button(draw, button_x, card_y + 220, button_width, button_height, 
                        "🔑 Recover Existing Wallet", 'secondary')
        
        # Save image
        img.save(self.output_dir / "01_welcome_screen.png", "PNG")
        print("✅ Created: Welcome Screen")
    
    def create_security_prompt(self):
        """Create the Security Acknowledgment prompt"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Overlay background
        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 200))
        img.paste(overlay, (0, 0), overlay)
        
        # Prompt container
        prompt_width = 700
        prompt_height = 500
        prompt_x = (self.width - prompt_width) // 2
        prompt_y = (self.height - prompt_height) // 2
        
        # Prompt card
        card_x, card_y, card_width, card_height = self.draw_card(
            draw, prompt_x, prompt_y, prompt_width, prompt_height, 
            "⚠️ SECURITY ACKNOWLEDGMENT"
        )
        
        # Warning content
        warning_texts = [
            "IMPORTANT: Cryptocurrency transactions are irreversible.",
            "",
            "By using this wallet, you acknowledge that:",
            "• You are responsible for securing your private keys",
            "• Lost recovery phrases cannot be recovered",
            "• C-Cube cannot access or recover your funds",
            "• You understand the risks of cryptocurrency",
            "",
            "Only proceed if you understand these risks."
        ]
        
        y_offset = card_y
        for text in warning_texts:
            if text.startswith("•"):
                draw.text((card_x + 20, y_offset), text, fill=self.colors['warning'], font=fonts['body'])
            elif text == "":
                pass  # Skip empty lines
            else:
                color = self.colors['danger'] if 'IMPORTANT' in text else self.colors['text']
                draw.text((card_x, y_offset), text, fill=color, font=fonts['body'])
            y_offset += 25
        
        # Checkbox
        checkbox_y = y_offset + 20
        draw.rectangle([card_x, checkbox_y, card_x + 15, checkbox_y + 15], 
                      outline=self.colors['primary'], width=2)
        draw.text((card_x + 25, checkbox_y), "I understand and accept the risks", 
                 fill=self.colors['text'], font=fonts['body'])
        
        # Continue button
        self.draw_button(draw, card_x + card_width - 200, card_y + card_height - 60, 
                        180, 40, "Continue", 'primary')
        
        img.save(self.output_dir / "02_security_prompt.png", "PNG")
        print("✅ Created: Security Acknowledgment")
    
    def create_wallet_setup(self):
        """Create the Wallet Setup screen"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Terminal frame
        frame_x, frame_y, frame_width, frame_height = self.draw_terminal_frame(
            draw, 50, 50, self.width - 100, self.height - 100
        )
        
        # Setup title
        draw.text((frame_x, frame_y), "Wallet Setup", fill=self.colors['primary'], font=fonts['title'])
        
        # Tab selector
        tab_y = frame_y + 50
        tab_width = 150
        tab_height = 40
        
        # Single Network tab (active)
        self.draw_button(draw, frame_x, tab_y, tab_width, tab_height, 
                        "Single Network", 'primary')
        
        # Multi-Chain tab (inactive)
        self.draw_button(draw, frame_x + tab_width + 10, tab_y, tab_width, tab_height, 
                        "Multi-Chain", 'secondary')
        
        # Network selection
        network_y = tab_y + 70
        draw.text((frame_x, network_y), "Select Network:", fill=self.colors['text'], font=fonts['body'])
        
        # Network dropdown (showing Ethereum selected)
        dropdown_y = network_y + 30
        self.draw_input_field(draw, frame_x, dropdown_y, 300, 40, value="Ethereum Mainnet")
        
        # Dropdown arrow
        draw.polygon([(frame_x + 270, dropdown_y + 15), 
                     (frame_x + 280, dropdown_y + 25), 
                     (frame_x + 260, dropdown_y + 25)], 
                    fill=self.colors['primary'])
        
        # Password section
        password_y = dropdown_y + 80
        draw.text((frame_x, password_y), "Password Protection (Recommended):", 
                 fill=self.colors['text'], font=fonts['body'])
        
        # Password checkbox (checked)
        checkbox_y = password_y + 30
        draw.rectangle([frame_x, checkbox_y, frame_x + 15, checkbox_y + 15], 
                      fill=self.colors['primary'], outline=self.colors['primary'], width=2)
        draw.text((frame_x + 7, checkbox_y + 3), "✓", fill=(0, 0, 0), font=fonts['small'])
        draw.text((frame_x + 25, checkbox_y), "Enable password protection", 
                 fill=self.colors['text'], font=fonts['body'])
        
        # Password input fields
        pass_input_y = checkbox_y + 40
        draw.text((frame_x, pass_input_y), "Password:", fill=self.colors['text'], font=fonts['body'])
        self.draw_input_field(draw, frame_x, pass_input_y + 25, 300, 40, value="••••••••••")
        
        confirm_y = pass_input_y + 80
        draw.text((frame_x, confirm_y), "Confirm Password:", fill=self.colors['text'], font=fonts['body'])
        self.draw_input_field(draw, frame_x, confirm_y + 25, 300, 40, value="••••••••••")
        
        # Create Wallet button
        create_btn_y = confirm_y + 80
        self.draw_button(draw, frame_x, create_btn_y, 200, 50, "Create Wallet", 'primary')
        
        img.save(self.output_dir / "03_wallet_setup.png", "PNG")
        print("✅ Created: Wallet Setup")
    
    def create_wallet_created(self):
        """Create the Wallet Created/Recovery Phrase screen"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Terminal frame
        frame_x, frame_y, frame_width, frame_height = self.draw_terminal_frame(
            draw, 50, 50, self.width - 100, self.height - 100
        )
        
        # Success title
        draw.text((frame_x, frame_y), "🎉 Wallet Created Successfully!", 
                 fill=self.colors['success'], font=fonts['title'])
        
        # Wallet info section
        info_y = frame_y + 50
        
        # Wallet address
        draw.text((frame_x, info_y), "Wallet Address:", fill=self.colors['text'], font=fonts['body'])
        address = "0x742d35cc6934c0532925a3b8d04e3bc07d9dd123"
        draw.text((frame_x, info_y + 25), address, fill=self.colors['primary'], font=fonts['code'])
        
        # Recovery phrase section
        phrase_y = info_y + 80
        draw.text((frame_x, phrase_y), "🔑 RECOVERY PHRASE (WRITE THIS DOWN!):", 
                 fill=self.colors['danger'], font=fonts['subtitle'])
        
        # Recovery phrase grid
        words = [
            "abandon", "ability", "able", "about", "above", "absent",
            "absorb", "abstract", "absurd", "abuse", "access", "accident"
        ]
        
        phrase_start_y = phrase_y + 40
        phrase_card_x, phrase_card_y, phrase_card_width, phrase_card_height = self.draw_card(
            draw, frame_x, phrase_start_y, frame_width - 100, 150
        )
        
        # Draw words in a grid
        words_per_row = 4
        word_width = phrase_card_width // words_per_row
        
        for i, word in enumerate(words):
            row = i // words_per_row
            col = i % words_per_row
            word_x = phrase_card_x + col * word_width
            word_y = phrase_card_y + row * 30
            
            # Word number
            draw.text((word_x, word_y), f"{i+1}.", fill=self.colors['mutedText'], font=fonts['small'])
            # Word
            draw.text((word_x + 25, word_y), word, fill=self.colors['text'], font=fonts['body'])
        
        # Security warning
        warning_y = phrase_start_y + 180
        warning_texts = [
            "⚠️ CRITICAL SECURITY INSTRUCTIONS:",
            "• Write this phrase on paper and store it safely",
            "• NEVER share it with anyone or store it digitally", 
            "• This phrase can recover your entire wallet",
            "• Lost phrases cannot be recovered - your funds will be lost forever"
        ]
        
        for i, text in enumerate(warning_texts):
            color = self.colors['danger'] if 'CRITICAL' in text else self.colors['warning']
            draw.text((frame_x, warning_y + i * 25), text, fill=color, font=fonts['body'])
        
        # Continue button
        continue_y = warning_y + 150
        self.draw_button(draw, frame_x, continue_y, 300, 50, 
                        "I have written down my recovery phrase", 'primary')
        
        img.save(self.output_dir / "04_wallet_created_recovery.png", "PNG")
        print("✅ Created: Wallet Created/Recovery Phrase")
    
    def create_main_wallet_interface(self):
        """Create the main wallet interface"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Terminal frame
        frame_x, frame_y, frame_width, frame_height = self.draw_terminal_frame(
            draw, 20, 20, self.width - 40, self.height - 40
        )
        
        # Header with network selector
        header_y = frame_y
        
        # Network selector
        draw.text((frame_x, header_y), "Network:", fill=self.colors['text'], font=fonts['body'])
        self.draw_input_field(draw, frame_x + 80, header_y - 5, 200, 30, value="Ethereum Mainnet")
        
        # Wallet address (right side)
        address_text = "Address: 0x742d...d123"
        draw.text((frame_x + frame_width - 250, header_y), address_text, 
                 fill=self.colors['mutedText'], font=fonts['small'])
        
        # Balance section
        balance_y = header_y + 50
        balance_card_x, balance_card_y, balance_card_width, balance_card_height = self.draw_card(
            draw, frame_x, balance_y, frame_width // 2 - 10, 150, "💰 Wallet Balance"
        )
        
        # ETH Balance
        draw.text((balance_card_x, balance_card_y), "ETH Balance:", 
                 fill=self.colors['text'], font=fonts['body'])
        draw.text((balance_card_x, balance_card_y + 25), "2.456789 ETH", 
                 fill=self.colors['primary'], font=fonts['subtitle'])
        draw.text((balance_card_x, balance_card_y + 50), "≈ $4,123.45 USD", 
                 fill=self.colors['mutedText'], font=fonts['body'])
        
        # QR Code placeholder (right side)
        qr_card_x, qr_card_y, qr_card_width, qr_card_height = self.draw_card(
            draw, frame_x + frame_width // 2 + 10, balance_y, frame_width // 2 - 10, 150, 
            "📱 Receive Address"
        )
        
        # QR code placeholder
        qr_size = 100
        qr_x = qr_card_x + (qr_card_width - qr_size) // 2
        qr_y = qr_card_y + 10
        
        # Simple QR code simulation
        for i in range(0, qr_size, 10):
            for j in range(0, qr_size, 10):
                if (i + j) % 20 == 0:
                    draw.rectangle([qr_x + i, qr_y + j, qr_x + i + 8, qr_y + j + 8], 
                                  fill=self.colors['text'])
        
        # Send Transaction section
        send_y = balance_y + 170
        send_card_x, send_card_y, send_card_width, send_card_height = self.draw_card(
            draw, frame_x, send_y, frame_width, 200, "💸 Send Transaction"
        )
        
        # Send form fields
        form_y = send_card_y
        
        # Recipient address
        draw.text((send_card_x, form_y), "Recipient Address:", 
                 fill=self.colors['text'], font=fonts['body'])
        self.draw_input_field(draw, send_card_x, form_y + 25, 400, 35, 
                             placeholder="0x...")
        
        # Amount
        draw.text((send_card_x + 450, form_y), "Amount (ETH):", 
                 fill=self.colors['text'], font=fonts['body'])
        self.draw_input_field(draw, send_card_x + 450, form_y + 25, 150, 35)
        
        # Gas fee
        gas_y = form_y + 80
        draw.text((send_card_x, gas_y), "Gas Fee:", fill=self.colors['text'], font=fonts['body'])
        draw.text((send_card_x + 80, gas_y), "0.001 ETH (~$2.50)", 
                 fill=self.colors['warning'], font=fonts['body'])
        
        # Send button
        self.draw_button(draw, send_card_x + send_card_width - 150, gas_y + 30, 
                        120, 40, "Send", 'primary')
        
        # Transaction history section
        history_y = send_y + 220
        if history_y + 100 < frame_y + frame_height:
            history_card_x, history_card_y, history_card_width, history_card_height = self.draw_card(
                draw, frame_x, history_y, frame_width, 120, "📊 Recent Transactions"
            )
            
            # Transaction entries
            transactions = [
                ("Received", "0.5 ETH", "2 hours ago", self.colors['success']),
                ("Sent", "-0.1 ETH", "1 day ago", self.colors['danger']),
                ("Received", "1.0 ETH", "3 days ago", self.colors['success'])
            ]
            
            for i, (tx_type, amount, time, color) in enumerate(transactions):
                tx_y = history_card_y + i * 25
                draw.text((history_card_x, tx_y), tx_type, fill=self.colors['text'], font=fonts['body'])
                draw.text((history_card_x + 100, tx_y), amount, fill=color, font=fonts['body'])
                draw.text((history_card_x + 200, tx_y), time, fill=self.colors['mutedText'], font=fonts['small'])
        
        img.save(self.output_dir / "05_main_wallet_interface.png", "PNG")
        print("✅ Created: Main Wallet Interface")
    
    def create_network_selector(self):
        """Create the Network Selection interface"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Terminal frame
        frame_x, frame_y, frame_width, frame_height = self.draw_terminal_frame(
            draw, 50, 50, self.width - 100, self.height - 100
        )
        
        # Title
        draw.text((frame_x, frame_y), "🌐 Network Selection", 
                 fill=self.colors['primary'], font=fonts['title'])
        
        # Network cards
        networks = [
            {
                'name': 'Ethereum Mainnet',
                'symbol': 'ETH',
                'features': 'Maximum security, Higher fees',
                'selected': True
            },
            {
                'name': 'Polygon',
                'symbol': 'MATIC', 
                'features': 'Fast & cheap transactions',
                'selected': False
            },
            {
                'name': 'Binance Smart Chain',
                'symbol': 'BNB',
                'features': 'High speed, Low fees',
                'selected': False
            },
            {
                'name': 'Arbitrum',
                'symbol': 'ARB',
                'features': 'Layer 2 scaling solution',
                'selected': False
            }
        ]
        
        card_width = (frame_width - 30) // 2
        card_height = 120
        
        for i, network in enumerate(networks):
            row = i // 2
            col = i % 2
            
            card_x = frame_x + col * (card_width + 10)
            card_y = frame_y + 60 + row * (card_height + 20)
            
            # Network card
            border_color = self.colors['primary'] if network['selected'] else self.colors['border']
            bg_color = self.colors['highlight'] if network['selected'] else self.colors['cardBackground']
            
            draw.rectangle([card_x, card_y, card_x + card_width, card_y + card_height],
                          fill=bg_color, outline=border_color, width=2)
            
            # Selection indicator
            if network['selected']:
                draw.text((card_x + 10, card_y + 10), "✓ SELECTED", 
                         fill=self.colors['success'], font=fonts['small'])
            
            # Network name
            draw.text((card_x + 15, card_y + 30), network['name'], 
                     fill=self.colors['text'], font=fonts['subtitle'])
            
            # Symbol
            draw.text((card_x + 15, card_y + 55), f"Symbol: {network['symbol']}", 
                     fill=self.colors['mutedText'], font=fonts['body'])
            
            # Features
            draw.text((card_x + 15, card_y + 80), network['features'], 
                     fill=self.colors['info'], font=fonts['small'])
        
        # Switch Network button
        switch_y = frame_y + 350
        self.draw_button(draw, frame_x, switch_y, 200, 50, "Switch Network", 'primary')
        
        img.save(self.output_dir / "06_network_selection.png", "PNG")
        print("✅ Created: Network Selection")
    
    def create_transaction_confirmation(self):
        """Create the Transaction Confirmation screen"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Semi-transparent overlay
        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 150))
        img.paste(overlay, (0, 0), overlay)
        
        # Confirmation modal
        modal_width = 600
        modal_height = 500
        modal_x = (self.width - modal_width) // 2
        modal_y = (self.height - modal_height) // 2
        
        # Modal card
        card_x, card_y, card_width, card_height = self.draw_card(
            draw, modal_x, modal_y, modal_width, modal_height, 
            "🔒 Confirm Transaction"
        )
        
        # Transaction details
        details = [
            ("From:", "0x742d35cc6934c0532925a3b8d04e3bc07d9dd123"),
            ("To:", "0x8ba1f109551bD432803012645Hac136c72f87721"),
            ("Amount:", "0.5 ETH"),
            ("Gas Fee:", "0.001 ETH (~$2.50)"),
            ("Total Cost:", "0.501 ETH (~$1,252.50)"),
            ("Network:", "Ethereum Mainnet")
        ]
        
        detail_y = card_y
        for label, value in details:
            draw.text((card_x, detail_y), label, fill=self.colors['text'], font=fonts['body'])
            
            # Truncate long addresses
            display_value = value
            if value.startswith('0x') and len(value) > 20:
                display_value = f"{value[:10]}...{value[-8:]}"
            
            color = self.colors['primary'] if 'ETH' in value else self.colors['mutedText']
            draw.text((card_x + 120, detail_y), display_value, fill=color, font=fonts['body'])
            detail_y += 30
        
        # Warning message
        warning_y = detail_y + 20
        warning_text = "⚠️ This transaction cannot be reversed once confirmed"
        draw.text((card_x, warning_y), warning_text, fill=self.colors['warning'], font=fonts['body'])
        
        # Password confirmation
        password_y = warning_y + 50
        draw.text((card_x, password_y), "Enter wallet password to confirm:", 
                 fill=self.colors['text'], font=fonts['body'])
        self.draw_input_field(draw, card_x, password_y + 25, 300, 40, value="••••••••••")
        
        # Buttons
        button_y = password_y + 100
        self.draw_button(draw, card_x, button_y, 120, 50, "Cancel", 'secondary')
        self.draw_button(draw, card_x + card_width - 140, button_y, 120, 50, 
                        "Confirm", 'primary')
        
        img.save(self.output_dir / "07_transaction_confirmation.png", "PNG")
        print("✅ Created: Transaction Confirmation")
    
    def create_token_management(self):
        """Create the Token Management interface"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Terminal frame
        frame_x, frame_y, frame_width, frame_height = self.draw_terminal_frame(
            draw, 30, 30, self.width - 60, self.height - 60
        )
        
        # Title
        draw.text((frame_x, frame_y), "🪙 Token Management", 
                 fill=self.colors['primary'], font=fonts['title'])
        
        # Add Token section
        add_token_y = frame_y + 50
        add_card_x, add_card_y, add_card_width, add_card_height = self.draw_card(
            draw, frame_x, add_token_y, frame_width, 120, "➕ Add Token"
        )
        
        # Token contract address input
        draw.text((add_card_x, add_card_y), "Token Contract Address:", 
                 fill=self.colors['text'], font=fonts['body'])
        self.draw_input_field(draw, add_card_x, add_card_y + 25, 400, 35,
                             placeholder="0x...")
        
        # Add button
        self.draw_button(draw, add_card_x + 420, add_card_y + 25, 100, 35, "Add", 'primary')
        
        # Token list
        token_list_y = add_token_y + 140
        list_card_x, list_card_y, list_card_width, list_card_height = self.draw_card(
            draw, frame_x, token_list_y, frame_width, 350, "💎 Your Tokens"
        )
        
        # Token entries
        tokens = [
            {
                'name': 'Ethereum',
                'symbol': 'ETH',
                'balance': '2.456789',
                'value': '$4,123.45',
                'native': True
            },
            {
                'name': 'USD Coin',
                'symbol': 'USDC', 
                'balance': '1,500.00',
                'value': '$1,500.00',
                'native': False
            },
            {
                'name': 'Chainlink',
                'symbol': 'LINK',
                'balance': '150.25',
                'value': '$2,253.75',
                'native': False
            },
            {
                'name': 'Uniswap',
                'symbol': 'UNI',
                'balance': '75.50',
                'value': '$453.00',
                'native': False
            }
        ]
        
        # Table headers
        header_y = list_card_y
        draw.text((list_card_x, header_y), "Token", fill=self.colors['primary'], font=fonts['body'])
        draw.text((list_card_x + 200, header_y), "Balance", fill=self.colors['primary'], font=fonts['body'])
        draw.text((list_card_x + 350, header_y), "Value", fill=self.colors['primary'], font=fonts['body'])
        draw.text((list_card_x + 450, header_y), "Actions", fill=self.colors['primary'], font=fonts['body'])
        
        # Separator line
        draw.line([(list_card_x, header_y + 20), (list_card_x + list_card_width - 20, header_y + 20)],
                 fill=self.colors['border'], width=1)
        
        # Token rows
        for i, token in enumerate(tokens):
            row_y = header_y + 40 + i * 50
            
            # Token icon placeholder (colored circle)
            icon_color = self.colors['primary'] if token['native'] else self.colors['info']
            draw.ellipse([list_card_x, row_y, list_card_x + 20, row_y + 20], fill=icon_color)
            
            # Token name and symbol
            draw.text((list_card_x + 30, row_y), token['name'], 
                     fill=self.colors['text'], font=fonts['body'])
            draw.text((list_card_x + 30, row_y + 20), token['symbol'], 
                     fill=self.colors['mutedText'], font=fonts['small'])
            
            # Balance
            draw.text((list_card_x + 200, row_y), token['balance'], 
                     fill=self.colors['text'], font=fonts['body'])
            
            # Value
            draw.text((list_card_x + 350, row_y), token['value'], 
                     fill=self.colors['success'], font=fonts['body'])
            
            # Actions (only for non-native tokens)
            if not token['native']:
                self.draw_button(draw, list_card_x + 450, row_y + 5, 60, 25, "Send", 'primary')
                self.draw_button(draw, list_card_x + 520, row_y + 5, 60, 25, "Hide", 'secondary')
        
        img.save(self.output_dir / "08_token_management.png", "PNG")
        print("✅ Created: Token Management")
    
    def create_transaction_history(self):
        """Create the Transaction History interface"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Terminal frame
        frame_x, frame_y, frame_width, frame_height = self.draw_terminal_frame(
            draw, 30, 30, self.width - 60, self.height - 60
        )
        
        # Title and filters
        draw.text((frame_x, frame_y), "📊 Transaction History", 
                 fill=self.colors['primary'], font=fonts['title'])
        
        # Filter section
        filter_y = frame_y + 50
        draw.text((frame_x, filter_y), "Filter:", fill=self.colors['text'], font=fonts['body'])
        
        # Filter buttons
        filter_buttons = ["All", "Sent", "Received", "Failed"]
        for i, btn_text in enumerate(filter_buttons):
            btn_x = frame_x + 60 + i * 80
            style = 'primary' if btn_text == 'All' else 'secondary'
            self.draw_button(draw, btn_x, filter_y - 5, 70, 30, btn_text, style)
        
        # Transaction list
        list_y = filter_y + 50
        list_card_x, list_card_y, list_card_width, list_card_height = self.draw_card(
            draw, frame_x, list_y, frame_width, 500, "Recent Transactions"
        )
        
        # Table headers
        headers = ["Type", "Amount", "To/From", "Status", "Time", "Hash"]
        header_widths = [80, 120, 200, 80, 120, 150]
        header_x = list_card_x
        
        for i, header in enumerate(headers):
            draw.text((header_x, list_card_y), header, fill=self.colors['primary'], font=fonts['body'])
            header_x += header_widths[i]
        
        # Separator line
        draw.line([(list_card_x, list_card_y + 20), 
                  (list_card_x + list_card_width - 20, list_card_y + 20)],
                 fill=self.colors['border'], width=1)
        
        # Transaction entries
        transactions = [
            {
                'type': 'Sent',
                'amount': '-0.5 ETH',
                'address': '0x8ba1...7721',
                'status': 'Confirmed',
                'time': '2 hours ago',
                'hash': '0xabc123...def456',
                'color': self.colors['danger']
            },
            {
                'type': 'Received', 
                'amount': '+1.0 ETH',
                'address': '0x123abc...789def',
                'status': 'Confirmed',
                'time': '1 day ago',
                'hash': '0x789def...123abc',
                'color': self.colors['success']
            },
            {
                'type': 'Sent',
                'amount': '-0.1 ETH',
                'address': '0x456def...012ghi',
                'status': 'Pending',
                'time': '3 days ago',
                'hash': '0x012ghi...456def',
                'color': self.colors['warning']
            },
            {
                'type': 'Received',
                'amount': '+2.5 ETH',
                'address': '0xfed321...987cba',
                'status': 'Confirmed',
                'time': '1 week ago',
                'hash': '0x987cba...fed321',
                'color': self.colors['success']
            }
        ]
        
        for i, tx in enumerate(transactions):
            row_y = list_card_y + 40 + i * 40
            col_x = list_card_x
            
            # Type
            draw.text((col_x, row_y), tx['type'], fill=self.colors['text'], font=fonts['body'])
            col_x += header_widths[0]
            
            # Amount
            draw.text((col_x, row_y), tx['amount'], fill=tx['color'], font=fonts['body'])
            col_x += header_widths[1]
            
            # Address
            draw.text((col_x, row_y), tx['address'], fill=self.colors['mutedText'], font=fonts['small'])
            col_x += header_widths[2]
            
            # Status
            status_color = self.colors['success'] if tx['status'] == 'Confirmed' else self.colors['warning']
            draw.text((col_x, row_y), tx['status'], fill=status_color, font=fonts['body'])
            col_x += header_widths[3]
            
            # Time
            draw.text((col_x, row_y), tx['time'], fill=self.colors['mutedText'], font=fonts['small'])
            col_x += header_widths[4]
            
            # Hash (clickable)
            draw.text((col_x, row_y), tx['hash'], fill=self.colors['info'], font=fonts['small'])
        
        # Export button
        export_y = list_y + 520
        self.draw_button(draw, frame_x, export_y, 150, 40, "Export CSV", 'primary')
        
        img.save(self.output_dir / "09_transaction_history.png", "PNG")
        print("✅ Created: Transaction History")
    
    def create_settings_security(self):
        """Create the Settings/Security interface"""
        img = self.create_background_with_grid()
        draw = ImageDraw.Draw(img)
        fonts = self.get_fonts()
        
        # Terminal frame
        frame_x, frame_y, frame_width, frame_height = self.draw_terminal_frame(
            draw, 40, 40, self.width - 80, self.height - 80
        )
        
        # Title
        draw.text((frame_x, frame_y), "🔒 Security Settings", 
                 fill=self.colors['primary'], font=fonts['title'])
        
        # Security sections
        sections = [
            {
                'title': 'Password Protection',
                'items': [
                    ('Password Lock Enabled', True, 'Your wallet is password protected'),
                    ('Auto-lock Timer', False, '5 minutes of inactivity'),
                    ('Require Password for Transactions', True, 'Extra security for sends')
                ]
            },
            {
                'title': 'Backup & Recovery',
                'items': [
                    ('Recovery Phrase Backed Up', True, 'Phrase safely stored offline'),
                    ('Wallet Backup Created', False, 'Create encrypted backup file'),
                    ('Backup Verification', False, 'Test recovery process')
                ]
            },
            {
                'title': 'Network Security',
                'items': [
                    ('Cold Storage Mode', True, 'Offline by default'),
                    ('Transaction Signing', True, 'Manual approval required'),
                    ('Network Verification', True, 'Prevent malicious connections')
                ]
            }
        ]
        
        current_y = frame_y + 50
        
        for section in sections:
            # Section card
            section_height = 140
            section_card_x, section_card_y, section_card_width, section_card_height = self.draw_card(
                draw, frame_x, current_y, frame_width, section_height, 
                f"🛡️ {section['title']}"
            )
            
            # Security items
            item_y = section_card_y
            for item_name, enabled, description in section['items']:
                # Checkbox
                checkbox_color = self.colors['success'] if enabled else self.colors['cardBackground']
                draw.rectangle([section_card_x, item_y, section_card_x + 15, item_y + 15],
                              fill=checkbox_color, outline=self.colors['primary'], width=1)
                
                if enabled:
                    draw.text((section_card_x + 4, item_y + 2), "✓", 
                             fill=(0, 0, 0), font=fonts['small'])
                
                # Item name
                draw.text((section_card_x + 25, item_y), item_name, 
                         fill=self.colors['text'], font=fonts['body'])
                
                # Description
                draw.text((section_card_x + 25, item_y + 20), description, 
                         fill=self.colors['mutedText'], font=fonts['small'])
                
                item_y += 45
            
            current_y += section_height + 20
        
        # Change Password button
        self.draw_button(draw, frame_x, current_y, 180, 40, "Change Password", 'primary')
        
        # Backup Wallet button
        self.draw_button(draw, frame_x + 200, current_y, 180, 40, "Backup Wallet", 'secondary')
        
        img.save(self.output_dir / "10_security_settings.png", "PNG")
        print("✅ Created: Security Settings")
    
    def create_all_ui_mockups(self):
        """Generate all UI mockups for the tutorial sections"""
        print("\n🎨 Generating C-Cube UI Mockups for Tutorial Guide...")
        print("=" * 60)
        
        # Create all UI screens
        self.create_welcome_screen()
        self.create_security_prompt()
        self.create_wallet_setup()
        self.create_wallet_created()
        self.create_main_wallet_interface()
        self.create_network_selector()
        self.create_transaction_confirmation()
        self.create_token_management()
        self.create_transaction_history()
        self.create_settings_security()
        
        print("\n✅ All UI mockups generated successfully!")
        print(f"📁 Location: {self.output_dir.absolute()}")
        print("\n🎨 Generated UI Mockups:")
        print("1. Welcome Screen - Initial app launch")
        print("2. Security Prompt - Risk acknowledgment")
        print("3. Wallet Setup - Create new wallet")
        print("4. Wallet Created - Recovery phrase display")
        print("5. Main Interface - Primary wallet screen")
        print("6. Network Selection - Multi-chain support")
        print("7. Transaction Confirmation - Send verification")
        print("8. Token Management - ERC-20 tokens")
        print("9. Transaction History - Activity log")
        print("10. Security Settings - Protection options")
        
        return self.output_dir

def main():
    """Generate C-Cube UI mockups"""
    print("🎨 C-CUBE UI MOCKUP GENERATOR")
    print("🚀 Creating realistic interface mockups for tutorial guide")
    print("=" * 60)
    
    generator = CCubeUIGenerator()
    output_dir = generator.create_all_ui_mockups()
    
    print(f"\n🎉 SUCCESS! All UI mockups created in: {output_dir}")
    print("📱 These mockups show the actual C-Cube interface for each tutorial section")
    print("🎨 Styled with authentic cyber/Matrix theme and green terminal aesthetics")
    
    # Open output directory
    import subprocess
    subprocess.run(['open', str(output_dir)])

if __name__ == "__main__":
    main()