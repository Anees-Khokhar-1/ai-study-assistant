📘 AI Study Assistant

An AI-powered tool that helps students summarize PDFs, generate notes, create MCQs, and chat with an AI tutor. Built with Flask (backend) and React (frontend).

🚀 Features

📄 PDF Summarizer – Upload a PDF and get a clean summary

📝 Notes Generator – Convert text into structured study notes

❓ MCQ Generator – Automatically create practice MCQs

🤖 AI Chat – Ask questions and get intelligent answers

🔊 Text-to-Speech – Listen to your summaries and notes

📂 Project Structure
backend/        → Flask API (summaries, chat, MCQs, notes, TTS)
frontend/       → React UI
docker-compose.yml
README.md

⚙️ Backend Setup (Flask)
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


Backend runs at:
👉 http://localhost:5000

🌐 Frontend Setup (React)
cd frontend
npm install
npm start


Frontend runs at:
👉 http://localhost:3000

Automatically connects to the backend.

🔗 API Endpoints
Endpoint	Method	Description
/api/upload	POST	Upload PDF & summarize
/summarize	POST	Summarize text
/notes	POST	Generate notes
/mcq	POST	Generate MCQs
/chat	POST	AI chat
🐳 Docker (Optional)
docker-compose up --build

📜 License

MIT License