# resume template python PDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, '<NAME> - <Trade>', 0, 1, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)
        
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()
        
    def add_section(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, '<Name> - <Trade>', 0, 1, 'C')
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '<email@example.com> | <phone-number> | <LinkedIn profile>', 0, 1, 'C')
pdf.ln(10)

# Professional Summary
pdf.chapter_title('PROFESSIONAL SUMMARY')
pdf.chapter_body("Lorum Ipsum...3-4 sentences")

# Quantified Achievements
pdf.chapter_title('QUANTIFIED ACHIEVEMENTS')
pdf.chapter_body("* Something you are proud o at job 1..2...3")

# Technical Skills
pdf.chapter_title('TECHNICAL SKILLS')
pdf.chapter_body("List them, group them, bullet points, whatever")

# Professional Experience
pdf.chapter_title('PROFESSIONAL EXPERIENCE')
pdf.chapter_body("<role> | Company | 2024 - Present\n* description.\n\n <role> | Company | <dates> \n* description. n* <role> | Company | <dates> \n* <description.> \n\n")

# Education & Certifications
pdf.chapter_title('EDUCATION & CERTIFICATIONS')
pdf.chapter_body("Degree, School, Dates, Training, Certificates, etc.")

# Additional Information & Links
pdf.chapter_title('ADDITIONAL INFORMATION & LINKS')
pdf.chapter_body("* Degrees and Certifications\n* <link>\n* <Portfolio-link>\n* Projects on <link>\n* Twitter\n* Linkedin, your web-site etc.")

# Save the pdf with name .pdf
pdf_output = "/your-work-folder/Your_Name_Resume.pdf"
pdf.output(pdf_output)

pdf_output
