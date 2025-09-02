from dotenv import load_dotenv
import os

load_dotenv()  # make sure .env is loaded
api_key = os.getenv("GROQ_API_KEY")
print("Loaded GROQ_API_KEY:", api_key[:6] + "..." if api_key else "MISSING")


import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from utils import clean_text
from resume_parser import ResumeParser


def create_streamlit_app(llm, clean_text):
    st.title("📧 Cold/Cover Mail Generator (Resume + Job URL)")

    # Upload resume
    resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    url_input = st.text_input("Enter a Job URL:", value="")
    submit_button = st.button("Generate Cold/cover Email")

    if submit_button:
        if not resume_file:
            st.error("Please upload your resume first.")
            return

        try:
            # --- Load job description ---
            loader = WebBaseLoader([url_input])
            job_text = clean_text(loader.load().pop().page_content)

            # --- Parse resume ---
            parser = ResumeParser(resume_file)
            resume_data = parser.parse()

            # --- Generate tailored email ---
            email = llm.write_mail(job_text, resume_data["raw_text"], contact_info=resume_data)

            st.subheader("Generated Cold Email")
            st.code(email, language="markdown")

        except Exception as e:
            st.error(f"An Error Occurred: {e}")

            


if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, clean_text)
