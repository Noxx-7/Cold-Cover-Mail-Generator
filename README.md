# 📨 AI Cold Email Generator

A Streamlit app that generates **personalized cold/cover emails** for job applications using **Groq LLMs**.  
It takes in a **job description (via URL)** + your **resume** and outputs a professional cold email tailored to the role.  
It also automatically inserts your **contact info (LinkedIn, GitHub, Portfolio, etc.)** from your resume.

---

## ✨ Features
- Extracts job details (title, skills, responsibilities).
- Parses your resume (contact info, skills, portfolio links).
- Generates a personalized cold email in under 250 words.
- Automatically includes your contact info (email, phone, LinkedIn, GitHub).
- Powered by **Groq LLM (Llama 3.3 70B Versatile)**.
- Simple **Streamlit UI**.

---

## 📂 Project Structure
```
app/
├── main.py          # Streamlit UI
├── chains.py        # LLM logic (job extraction + email generation)
├── resume_parser.py # Resume parsing logic
├── portfolio.py     # Portfolio retrieval (skills → project links)
├── utils.py         # Helper functions
├── .env             # Store your GROQ_API_KEY here
├── requirements.txt # Dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ai-cold-email-generator.git
cd ai-cold-email-generator/app
```

### 2. Create and activate virtual environment (optional but recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Groq API Key
Create a `.env` file inside the `app/` folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the app
```bash
streamlit run main.py
```

The app will be available at:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 🔄 How It Works (Flowchart)
Below is the flow of how the app works:

![Flowchart](cold_email_flowchart_black.png)

---

## 📸 Demo
(Add screenshots or a GIF here once you run the app)

---

## 🚀 Future Improvements
- Polished signature block for emails.
- Multiple email styles (short, formal, casual).
- Option to summarize job description separately.

---

## 🛠️ Tech Stack
- **Streamlit** – UI  
- **LangChain** – Prompt chaining  
- **Groq LLM (Llama 3.3 70B)** – AI model  
- **Python-dotenv** – API key management  
- **pdfplumber, python-docx** – Resume parsing  

---

## 🤝 Contributing
Pull requests are welcome!  
For major changes, please open an issue first to discuss what you’d like to change.

---

## 📬 Author
Made with ❤️ by [Your Name]
