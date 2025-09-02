from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import re

load_dotenv()  # Load environment variables (GROQ_API_KEY)

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",  # ✅ Supported model
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

    def extract_jobs(self, job_text: str):
        """
        Extract structured job details (title, skills, responsibilities)
        from the raw job description.
        """
        prompt = f"""
        Analyze the following job description and extract structured details.

        === Job Description ===
        {job_text}

        Return the result in JSON with keys:
        - title
        - company (if available)
        - skills (list of required skills)
        - responsibilities (list of responsibilities)
        """

        response = self.llm.invoke(prompt)
        return response.content

    def _extract_links_from_resume(self, resume_text: str):
        """
        Automatically detect links (LinkedIn, GitHub, portfolio) from resume text.
        """
        url_pattern = r"(https?://[^\s]+)"
        found_links = re.findall(url_pattern, resume_text)
        return list(set(found_links))  # remove duplicates

    def write_mail(self, job_text: str, resume_text: str, contact_info: dict = None):
        """
        Generate a personalized cold email.
        """
        # Auto-extract links from resume
        extracted_links = self._extract_links_from_resume(resume_text)

        # Merge with provided contact info
        links = set(extracted_links)
        if contact_info and "links" in contact_info:
            links.update(contact_info["links"])

        # Build prompt
        prompt = f"""
        You are a professional career assistant.
        Write a cold email applying for the following job.

        === Job Description ===
        {job_text}

        === Candidate Resume ===
        {resume_text}

        Instructions:
        - Include subject, greeting, body, and closing.
        - Mention 1–2 projects or skills that best fit the job.
        - Keep under 250 words.
        - End the email with clear contact information.
        """

        # Always append contact info
        if contact_info:
            prompt += f"""

            === Contact Info ===
            Email: {contact_info.get('email','')}
            Phone: {contact_info.get('phone','')}
            Links: {', '.join(links)}
            """
        elif links:
            prompt += f"""

            === Contact Info (auto-detected) ===
            Links: {', '.join(links)}
            """

        response = self.llm.invoke(prompt)
        return response.content
