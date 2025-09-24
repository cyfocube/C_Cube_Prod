#!/usr/bin/env python3
"""
C-Cube Learning Guide PDF Generator
Converts the comprehensive markdown guide into a professional PDF learning document
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Install required packages if not available
def install_requirements():
    try:
        import markdown
        import pdfkit
        from markdown.extensions import toc
        print("✅ All required packages are available")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Installing required packages...")
        os.system("pip install markdown pdfkit markdown-extensions")
        try:
            import markdown
            import pdfkit
            return True
        except ImportError:
            print("❌ Failed to install packages. Please install manually:")
            print("pip install markdown pdfkit markdown-extensions")
            return False

def read_markdown_file(file_path):
    """Read the markdown content from file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"✅ Successfully read markdown file: {file_path}")
        return content
    except FileNotFoundError:
        print(f"❌ Markdown file not found: {file_path}")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None

def create_html_template():
    """Create HTML template with professional styling for learning document"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>C-Cube Cold Wallet: Complete User Education Guide</title>
    <style>
        /* Professional Learning Document Styling */
        @page {
            size: A4;
            margin: 1in;
            @top-left {
                content: "C-Cube Learning Guide";
                font-size: 10px;
                color: #666;
            }
            @top-right {
                content: counter(page);
                font-size: 10px;
                color: #666;
            }
        }
        
        body {
            font-family: 'Segoe UI', 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
        }
        
        /* Title Page Styling */
        .title-page {
            text-align: center;
            padding: 100px 0;
            page-break-after: always;
            border-bottom: 3px solid #667eea;
        }
        
        .title-page h1 {
            font-size: 2.5em;
            color: #667eea;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        .title-page h2 {
            font-size: 1.5em;
            color: #666;
            margin-bottom: 50px;
            font-weight: 300;
        }
        
        .title-page .version-info {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin: 30px auto;
            max-width: 400px;
            border-left: 4px solid #667eea;
        }
        
        /* Headers */
        h1 {
            color: #667eea;
            font-size: 2em;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
            margin-top: 40px;
            page-break-before: always;
        }
        
        h2 {
            color: #555;
            font-size: 1.5em;
            margin-top: 30px;
            border-left: 4px solid #667eea;
            padding-left: 15px;
        }
        
        h3 {
            color: #666;
            font-size: 1.3em;
            margin-top: 25px;
        }
        
        h4 {
            color: #777;
            font-size: 1.1em;
            margin-top: 20px;
        }
        
        /* Table of Contents */
        .toc {
            background: #f8f9fa;
            padding: 30px;
            border-radius: 8px;
            margin: 30px 0;
            page-break-after: always;
        }
        
        .toc h2 {
            color: #667eea;
            border: none;
            margin-top: 0;
            padding-left: 0;
        }
        
        .toc ul {
            list-style: none;
            padding-left: 0;
        }
        
        .toc li {
            padding: 8px 0;
            border-bottom: 1px dotted #ddd;
        }
        
        .toc a {
            text-decoration: none;
            color: #555;
            font-weight: 500;
        }
        
        /* Content Styling */
        p {
            margin-bottom: 15px;
            text-align: justify;
        }
        
        /* Lists */
        ul, ol {
            margin: 15px 0;
            padding-left: 25px;
        }
        
        li {
            margin-bottom: 8px;
        }
        
        /* Emphasis boxes */
        .highlight-box {
            background: #f0f7ff;
            border: 1px solid #667eea;
            border-radius: 6px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .warning-box {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-left: 4px solid #f39c12;
            border-radius: 6px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .success-box {
            background: #d4edda;
            border: 1px solid #c3e6cb;
            border-left: 4px solid #28a745;
            border-radius: 6px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .danger-box {
            background: #f8d7da;
            border: 1px solid #f5c6cb;
            border-left: 4px solid #dc3545;
            border-radius: 6px;
            padding: 20px;
            margin: 20px 0;
        }
        
        /* Code and technical content */
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9em;
        }
        
        pre {
            background: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 6px;
            padding: 15px;
            overflow-x: auto;
            margin: 15px 0;
        }
        
        /* Step-by-step instructions */
        .step-list {
            counter-reset: step-counter;
        }
        
        .step-list li {
            counter-increment: step-counter;
            position: relative;
            padding-left: 40px;
            margin-bottom: 15px;
        }
        
        .step-list li::before {
            content: counter(step-counter);
            position: absolute;
            left: 0;
            top: 0;
            background: #667eea;
            color: white;
            width: 25px;
            height: 25px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: bold;
        }
        
        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        
        th {
            background: #667eea;
            color: white;
            font-weight: 600;
        }
        
        tr:nth-child(even) {
            background: #f9f9f9;
        }
        
        /* Links */
        a {
            color: #667eea;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        /* Blockquotes */
        blockquote {
            border-left: 4px solid #667eea;
            margin: 20px 0;
            padding: 10px 20px;
            background: #f8f9fa;
            font-style: italic;
        }
        
        /* Icons and emojis */
        .icon {
            font-style: normal;
            font-size: 1.2em;
            margin-right: 8px;
        }
        
        /* Footer */
        .document-footer {
            text-align: center;
            padding: 30px 0;
            border-top: 1px solid #ddd;
            margin-top: 50px;
            color: #666;
            font-size: 0.9em;
        }
        
        /* Page breaks */
        .page-break {
            page-break-before: always;
        }
        
        /* Print optimizations */
        @media print {
            body {
                font-size: 12px;
                line-height: 1.4;
            }
            
            h1 {
                font-size: 1.8em;
            }
            
            h2 {
                font-size: 1.4em;
            }
            
            .no-print {
                display: none;
            }
        }
    </style>
</head>
<body>
    <!-- Title Page -->
    <div class="title-page">
        <h1>C-Cube Cold Wallet</h1>
        <h2>Complete User Education Guide</h2>
        <div class="version-info">
            <p><strong>Your Journey to Secure Cryptocurrency Management</strong></p>
            <p>Version 1.0 • Generated: {date}</p>
            <p>Educational Learning Document</p>
        </div>
    </div>
    
    <!-- Main Content -->
    <div class="content">
        {content}
    </div>
    
    <!-- Document Footer -->
    <div class="document-footer">
        <p>© 2025 C-Cube. This educational guide is designed to help users safely navigate cryptocurrency management.</p>
        <p>For the latest updates and support, visit the official C-Cube documentation.</p>
    </div>
</body>
</html>
"""

def process_markdown_content(content):
    """Process markdown content and add special formatting"""
    import re
    
    # Convert markdown emphasis to HTML classes
    content = re.sub(r'\*\*(✅[^*]+)\*\*', r'<span class="success-box">\1</span>', content)
    content = re.sub(r'\*\*(❌[^*]+)\*\*', r'<span class="danger-box">\1</span>', content)
    content = re.sub(r'\*\*(⚠️[^*]+)\*\*', r'<span class="warning-box">\1</span>', content)
    
    # Convert step-by-step lists
    content = re.sub(r'(\*\*Step \d+[^*]*\*\*)', r'<div class="highlight-box">\1</div>', content)
    
    # Enhance important sections
    content = content.replace('**Real Talk**:', '<div class="warning-box"><strong>⚠️ Real Talk:</strong>')
    content = content.replace('**The Golden Rule**:', '<div class="highlight-box"><strong>🎯 The Golden Rule:</strong>')
    content = content.replace('**Pro Tip**:', '<div class="success-box"><strong>💡 Pro Tip:</strong>')
    
    return content

def convert_to_pdf(content, output_path):
    """Convert HTML content to PDF"""
    try:
        import pdfkit
        
        # PDF options for better formatting
        options = {
            'page-size': 'A4',
            'margin-top': '1in',
            'margin-right': '0.8in',
            'margin-bottom': '1in',
            'margin-left': '0.8in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None,
            'print-media-type': None,
            'disable-smart-shrinking': None,
        }
        
        # Generate PDF
        pdfkit.from_string(content, output_path, options=options)
        print(f"✅ PDF generated successfully: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        print("Note: You may need to install wkhtmltopdf:")
        print("- macOS: brew install wkhtmltopdf")
        print("- Windows: Download from https://wkhtmltopdf.org/downloads.html")
        print("- Linux: sudo apt-get install wkhtmltopdf")
        return False

def main():
    """Main function to generate the PDF learning guide"""
    print("🚀 C-Cube Learning Guide PDF Generator")
    print("=" * 50)
    
    # Check and install requirements
    if not install_requirements():
        return
    
    import markdown
    from markdown.extensions import toc
    
    # Set up paths
    current_dir = Path(__file__).parent
    markdown_file = current_dir.parent / "C-Cube_Wallet_Complete_Tutorial_Guide.md"
    output_file = current_dir / "C-Cube_Learning_Guide.pdf"
    
    # Create output directory if it doesn't exist
    current_dir.mkdir(exist_ok=True)
    
    print(f"📖 Reading markdown file: {markdown_file}")
    
    # Read markdown content
    markdown_content = read_markdown_file(markdown_file)
    if not markdown_content:
        return
    
    print("🔄 Processing markdown content...")
    
    # Process the content
    processed_content = process_markdown_content(markdown_content)
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=[
        'toc',
        'tables', 
        'fenced_code',
        'codehilite',
        'extra'
    ])
    
    html_content = md.convert(processed_content)
    
    # Create complete HTML document
    html_template = create_html_template()
    complete_html = html_template.format(
        content=html_content,
        date=datetime.now().strftime("%B %d, %Y")
    )
    
    print("📄 Converting to PDF...")
    
    # Convert to PDF
    if convert_to_pdf(complete_html, str(output_file)):
        print(f"🎉 Success! PDF learning guide created: {output_file}")
        print(f"📁 File size: {output_file.stat().st_size / 1024 / 1024:.2f} MB")
        
        # Also save HTML version for review
        html_file = current_dir / "C-Cube_Learning_Guide.html"
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(complete_html)
        print(f"📝 HTML version also saved: {html_file}")
        
    else:
        print("❌ PDF generation failed. Please check the requirements.")

if __name__ == "__main__":
    main()