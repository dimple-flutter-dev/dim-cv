#!/usr/bin/env python3
"""
Generate ATS-optimized, recruiter-ready PDF CV from cv.json
Optimized for parsing and visual clarity
"""

import json
from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def load_cv_data(json_path):
    """Load CV data from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def create_styles():
    """Create custom paragraph styles"""
    styles = getSampleStyleSheet()

    # Name/Title style
    styles.add(ParagraphStyle(
        name='CVTitle',
        parent=styles['Normal'],
        fontSize=20,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=2,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))

    # Section header style
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=6,
        spaceBefore=8,
        fontName='Helvetica-Bold',
        borderColor=colors.HexColor('#2c3e50'),
        borderWidth=0.5,
        borderPadding=4
    ))

    # Company/Role style
    styles.add(ParagraphStyle(
        name='CompanyRole',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=2,
        fontName='Helvetica-Bold'
    ))

    # Dates style
    styles.add(ParagraphStyle(
        name='DateRange',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666'),
        spaceAfter=4,
        fontName='Helvetica'
    ))

    # Highlight bullets
    styles.add(ParagraphStyle(
        name='Highlight',
        parent=styles['Normal'],
        fontSize=9.5,
        textColor=colors.HexColor('#333333'),
        spaceAfter=3,
        leftIndent=15,
        bulletIndent=10,
        fontName='Helvetica'
    ))

    # Skills keyword style
    styles.add(ParagraphStyle(
        name='SkillKeyword',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=2,
        fontName='Helvetica'
    ))

    return styles

def format_date(date_str):
    """Format date string"""
    if not date_str:
        return "Present"
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m")
        return date_obj.strftime("%b %Y")
    except:
        return date_str

def build_cv_document(data):
    """Build list of document elements"""
    styles = create_styles()
    elements = []

    # Header with name and title
    basics = data['basics']
    elements.append(Paragraph(basics['name'].upper(), styles['CVTitle']))
    elements.append(Paragraph(basics['label'], styles['SectionHeader']))

    # Contact info
    contact_parts = []
    if basics.get('location'):
        contact_parts.append(basics['location'].get('countryCode', 'IN'))
    if basics.get('profiles'):
        for profile in basics['profiles']:
            if 'LinkedIn' in profile.get('network', ''):
                contact_parts.append(f"LinkedIn: {profile['url'].split('/')[-1]}")

    if contact_parts:
        elements.append(Paragraph(' | '.join(contact_parts), styles['Normal']))

    elements.append(Spacer(1, 0.15*inch))

    # Professional Summary
    if basics.get('summary'):
        elements.append(Paragraph('PROFESSIONAL SUMMARY', styles['SectionHeader']))
        elements.append(Paragraph(basics['summary'], styles['Highlight']))
        elements.append(Spacer(1, 0.1*inch))

    # Work Experience
    if data.get('work'):
        elements.append(Paragraph('PROFESSIONAL EXPERIENCE', styles['SectionHeader']))

        for job in data['work']:
            # Company and Role
            company_role = f"<b>{job['name']}</b> — {job['position']}"
            elements.append(Paragraph(company_role, styles['CompanyRole']))

            # Dates
            start = format_date(job.get('startDate'))
            end = format_date(job.get('endDate', ''))
            date_str = f"{start} – {end}" if end != "Present" else start
            elements.append(Paragraph(date_str, styles['DateRange']))

            # Summary if present
            if job.get('summary'):
                elements.append(Paragraph(job['summary'], styles['Highlight']))

            # Highlights
            if job.get('highlights'):
                for highlight in job['highlights']:
                    bullet_text = f"• {highlight}"
                    elements.append(Paragraph(bullet_text, styles['Highlight']))

            elements.append(Spacer(1, 0.08*inch))

        elements.append(Spacer(1, 0.05*inch))

    # Skills
    if data.get('skills'):
        elements.append(Paragraph('TECHNICAL SKILLS', styles['SectionHeader']))

        for skill_group in data['skills']:
            # Skill category and keywords
            keywords = ', '.join(skill_group.get('keywords', []))
            skill_text = f"<b>{skill_group['name']}:</b> {keywords}"
            elements.append(Paragraph(skill_text, styles['SkillKeyword']))

        elements.append(Spacer(1, 0.1*inch))

    # Education
    if data.get('education'):
        elements.append(Paragraph('EDUCATION', styles['SectionHeader']))

        for edu in data['education']:
            # Degree and Institution
            degree_text = f"<b>{edu['studyType']} in {edu['area']}</b>"
            elements.append(Paragraph(degree_text, styles['CompanyRole']))

            institution_text = f"{edu['institution']}"
            elements.append(Paragraph(institution_text, styles['DateRange']))

            # Score if available
            if edu.get('score'):
                score_text = f"GPA: {edu['score']}"
                elements.append(Paragraph(score_text, styles['Highlight']))

            elements.append(Spacer(1, 0.06*inch))

    return elements

def generate_pdf(json_path, output_path):
    """Generate PDF from CV JSON"""

    # Load data
    data = load_cv_data(json_path)

    # Create PDF document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch,
        title=f"{data['basics']['name']} - CV"
    )

    # Build document
    elements = build_cv_document(data)

    # Build PDF
    doc.build(elements)
    print(f"✅ CV PDF generated: {output_path}")

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    json_path = project_root / "cv.json"
    output_path = project_root / "Dimple_Shukla_CV.pdf"

    generate_pdf(str(json_path), str(output_path))
