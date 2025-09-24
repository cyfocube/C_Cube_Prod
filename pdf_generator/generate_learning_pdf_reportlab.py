#!/usr/bin/env python3
"""
C-Cube Learning Guide PDF Generator (Using ReportLab)
Converts the comprehensive markdown guide into a professional PDF learning document
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

def install_requirements():
    """Install required packages"""
    try:
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
        import markdown
        print("✅ All required packages are available")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Installing required packages...")
        os.system("pip install reportlab markdown")
        try:
            from reportlab.lib.pagesizes import letter, A4
            import markdown
            return True
        except ImportError:
            print("❌ Failed to install packages. Please install manually:")
            print("pip install reportlab markdown")
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

def create_styles():
    """Create custom styles for the PDF"""
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
    from reportlab.lib import colors
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.Color(0.4, 0.5, 0.9),
        alignment=TA_CENTER
    ))
    
    styles.add(ParagraphStyle(
        name='CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20,
        spaceBefore=30,
        textColor=colors.Color(0.4, 0.5, 0.9),
        borderWidth=2,
        borderColor=colors.Color(0.4, 0.5, 0.9)
    ))
    
    styles.add(ParagraphStyle(
        name='CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=15,
        spaceBefore=20,
        textColor=colors.Color(0.3, 0.3, 0.3),
        leftIndent=20
    ))
    
    styles.add(ParagraphStyle(
        name='CustomBodyText',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        leftIndent=0,
        rightIndent=0
    ))
    
    styles.add(ParagraphStyle(
        name='BulletList',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        leftIndent=20,
        bulletIndent=10
    ))
    
    styles.add(ParagraphStyle(
        name='HighlightBox',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=15,
        spaceBefore=15,
        leftIndent=20,
        rightIndent=20,
        borderWidth=1,
        borderColor=colors.Color(0.4, 0.5, 0.9),
        backColor=colors.Color(0.95, 0.97, 1.0),
        borderPadding=10
    ))
    
    styles.add(ParagraphStyle(
        name='WarningBox',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=15,
        spaceBefore=15,
        leftIndent=20,
        rightIndent=20,
        borderWidth=1,
        borderColor=colors.Color(1.0, 0.6, 0.0),
        backColor=colors.Color(1.0, 0.95, 0.8),
        borderPadding=10
    ))
    
    return styles

def process_markdown_to_elements(content, styles):
    """Convert markdown content to ReportLab elements"""
    from reportlab.platypus import Paragraph, Spacer, PageBreak
    from reportlab.lib.units import inch
    import re
    
    def format_bold_text(text):
        """Properly format bold text by replacing **text** with <b>text</b>"""
        return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    
    elements = []
    lines = content.split('\n')
    
    # Title page
    elements.append(Spacer(1, 2*inch))
    elements.append(Paragraph("C-Cube Cold Wallet", styles['CustomTitle']))
    elements.append(Paragraph("Complete User Education Guide", styles['CustomTitle']))
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("Your Journey to Secure Cryptocurrency Management", styles['CustomBodyText']))
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y')}", styles['CustomBodyText']))
    elements.append(PageBreak())
    
    current_paragraph = []
    in_list = False
    
    for line in lines:
        line = line.strip()
        
        if not line:
            if current_paragraph:
                elements.append(Paragraph(' '.join(current_paragraph), styles['CustomBodyText']))
                current_paragraph = []
            elements.append(Spacer(1, 6))
            in_list = False
            continue
        
        # Handle headers
        if line.startswith('# '):
            if current_paragraph:
                elements.append(Paragraph(' '.join(current_paragraph), styles['CustomBodyText']))
                current_paragraph = []
            elements.append(PageBreak())
            elements.append(Paragraph(line[2:], styles['CustomHeading1']))
            in_list = False
            
        elif line.startswith('## '):
            if current_paragraph:
                elements.append(Paragraph(' '.join(current_paragraph), styles['CustomBodyText']))
                current_paragraph = []
            elements.append(Paragraph(line[3:], styles['CustomHeading2']))
            in_list = False
            
        elif line.startswith('### '):
            if current_paragraph:
                elements.append(Paragraph(' '.join(current_paragraph), styles['CustomBodyText']))
                current_paragraph = []
            elements.append(Paragraph(f"<b>{line[4:]}</b>", styles['CustomBodyText']))
            in_list = False
            
        # Handle lists
        elif line.startswith('- ') or line.startswith('* '):
            if current_paragraph:
                elements.append(Paragraph(' '.join(current_paragraph), styles['CustomBodyText']))
                current_paragraph = []
            elements.append(Paragraph(f"• {line[2:]}", styles['BulletList']))
            in_list = True
            
        elif re.match(r'^\d+\. ', line):
            if current_paragraph:
                elements.append(Paragraph(' '.join(current_paragraph), styles['CustomBodyText']))
                current_paragraph = []
            number = re.match(r'^(\d+)\. (.+)', line)
            if number:
                elements.append(Paragraph(f"{number.group(1)}. {number.group(2)}", styles['BulletList']))
            in_list = True
        
        # Handle special formatting
        elif line.startswith('**✅') or line.startswith('**🔒') or line.startswith('**🌐'):
            if current_paragraph:
                elements.append(Paragraph(' '.join(current_paragraph), styles['CustomBodyText']))
                current_paragraph = []
            # Properly format bold text
            formatted_line = format_bold_text(line)
            elements.append(Paragraph(formatted_line, styles['HighlightBox']))
            in_list = False
            
        elif line.startswith('**⚠️') or line.startswith('**❌'):
            if current_paragraph:
                elements.append(Paragraph(' '.join(current_paragraph), styles['CustomBodyText']))
                current_paragraph = []
            # Properly format bold text
            formatted_line = format_bold_text(line)
            elements.append(Paragraph(formatted_line, styles['WarningBox']))
            in_list = False
            
        # Handle horizontal rules
        elif line.startswith('---'):
            if current_paragraph:
                elements.append(Paragraph(' '.join(current_paragraph), styles['CustomBodyText']))
                current_paragraph = []
            elements.append(Spacer(1, 12))
            in_list = False
            
        # Regular content
        else:
            if not in_list:
                current_paragraph.append(line)
    
    # Add any remaining paragraph
    if current_paragraph:
        formatted_text = format_bold_text(' '.join(current_paragraph))
        elements.append(Paragraph(formatted_text, styles['CustomBodyText']))
    
    return elements

def create_pdf(elements, output_path):
    """Create PDF document"""
    from reportlab.platypus import SimpleDocTemplate
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import inch
    
    try:
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=A4,
            rightMargin=inch,
            leftMargin=inch,
            topMargin=inch,
            bottomMargin=inch
        )
        
        doc.build(elements)
        print(f"✅ PDF created successfully: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")
        return False

def main():
    """Main function to generate the PDF learning guide"""
    print("🚀 C-Cube Learning Guide PDF Generator (ReportLab)")
    print("=" * 55)
    
    # Check and install requirements
    if not install_requirements():
        return
    
    # Set up paths
    current_dir = Path(__file__).parent
    markdown_file = current_dir.parent / "C-Cube_Wallet_Complete_Tutorial_Guide.md"
    output_file = current_dir / "C-Cube_Learning_Guide.pdf"
    
    print(f"📖 Reading markdown file: {markdown_file}")
    
    # Read markdown content
    markdown_content = read_markdown_file(markdown_file)
    if not markdown_content:
        return
    
    print("🔄 Processing markdown content...")
    
    # Create styles
    styles = create_styles()
    
    # Convert markdown to PDF elements
    elements = process_markdown_to_elements(markdown_content, styles)
    
    print("📄 Creating PDF...")
    
    # Create PDF
    if create_pdf(elements, output_file):
        print(f"🎉 Success! PDF learning guide created: {output_file}")
        print(f"📁 File size: {output_file.stat().st_size / 1024 / 1024:.2f} MB")
    else:
        print("❌ PDF generation failed.")

if __name__ == "__main__":
    main()