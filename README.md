# 🤖 Simple Groq AI Chatbot

This is a simple command-line and API-based chatbot built using Python, FastAPI, LangChain, and the Groq LLaMA 3 model. It answers user questions using real AI logic.

---

## 🚀 Features

- Chat via terminal or API
- Real-time responses using Groq LLaMA3
- FastAPI `/ask` endpoint for web interaction
- Secure `.env` for API key

---

## 🛠 Installation

bash
git clone https://github.com/kalaiyarasan105/simple-chatbot
cd simple-chatbot
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
Create .env:

ini
GROQ_API_KEY="your_groq_api_key"
💬 Usage
▶ Terminal Mode
python main.py
🌐 API Mode
bash
uvicorn main:app --reload
Test at: http://127.0.0.1:8000/docs

📁 Files
main.py – Bot logic + FastAPI server

.env – API key

vercel.json – Optional deployment

🎥 Demo
Run the bot in terminal
