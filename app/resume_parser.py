import re
import docx
import pdfplumber


class ResumeParser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        if self.file.name.endswith(".pdf"):
            text = self._parse_pdf()
        else:
            text = self._parse_docx()

        return self._extract_sections(text)

    def _parse_pdf(self):
        text = ""
        with pdfplumber.open(self.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    def _parse_docx(self):
        doc = docx.Document(self.file)
        return "\n".join([para.text for para in doc.paragraphs])

    def _extract_sections(self, text):
        # Extract contact info
        email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
        phone_match = re.search(r'\+?\d[\d\s-]{8,}\d', text)
        links = re.findall(r'(https?://[^\s]+)', text)

        # Extract skills (basic: look for "Skills" section)
        skills_match = re.findall(r"(?i)(skills|technologies|tools)[:\-]?\s*(.+)", text)
        skills = []
        for _, s in skills_match:
            skills.extend([x.strip() for x in re.split(r"[;,]", s)])

        return {
            "raw_text": text,
            "email": email_match.group(0) if email_match else "",
            "phone": phone_match.group(0) if phone_match else "",
            "links": links,
            "skills": skills,
        }
