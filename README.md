# Syllabus-questions-generator
Upload any syllabus PDF/image and auto-generate unit-wise exam questions using Gemini + LangChain.
# 📚 Syllabus Question Generator | GenAI + Streamlit

Generate **exam-style questions** from any syllabus PDF or image using **Google Gemini**, **LangChain**, and **OCR**.

---

## 🚀 Features

- 📤 Upload a syllabus (PDF or image)
- 🧠 Extracts content via PDF parser or OCR
- ✍️ Generates 3 questions per unit:
  - 1 Easy (2 marks)
  - 1 Medium (5 marks)
  - 1 Hard (10 marks)
- 🤖 Powered by Gemini 2.5 Flash + LangChain
- 🖥️ Clean, minimal Streamlit interface

---

## 🛠 Tech Stack

- `Streamlit` – UI & app logic  
- `LangChain` – Prompt templating & chaining  
- `Gemini API` – Question generation  
- `pytesseract` – OCR for scanned images  
- `PyPDFLoader` – For PDF text parsing

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/syllabus-question-generator.git
cd syllabus-question-generator
pip install -r requirements.txt
