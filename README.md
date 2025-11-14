📘 AI Study Assistant / Notes Summarizer

Upload lecture PDFs or text → get clean, structured summarized notes. Optional TTS support.

🚀 Overview

AI Study Assistant is a full-stack web application that allows students and researchers to upload lecture notes (PDF/text) and get high-quality summaries generated using state-of-the-art NLP transformer models (BART/T5/GPT).
It also supports optional Text-to-Speech to generate MP3 audio summaries.

✨ Features

🔹 Upload PDFs or raw text
🔹 Automatic text extraction (PDF → text)
🔹 Summarization using HuggingFace Transformers
🔹 Chunking for long documents
🔹 Downloadable summary files
🔹 Optional text-to-speech (MP3 export)
🔹 React frontend + Flask backend
🔹 Docker & Docker Compose support
🔹 Modular, clean code structure

🏗️ Project Structure
ai-study-assistant/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── config.py
│   ├── models/
│   │   ├── summarizer.py
│   │   └── tts.py
│   ├── services/
│   │   ├── pdf_parser.py
│   │   ├── storage.py
│   │   └── db.py
│   ├── utils/
│   │   ├── text_chunker.py
│   │   └── cleanup.py
│   └── tests/
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── services/api.js
│   └── public/
├── infra/
│   ├── nginx.conf
│   └── deploy/
├── docker-compose.yml
└── README.md

🧰 Tech Stack
Backend

Python 3.11

Flask

HuggingFace Transformers (BART, T5)

pdfplumber / PyMuPDF

pytesseract (OCR fallback)

SQLAlchemy

gTTS (optional)

Frontend

React

Axios

Vite/Create-React-App

Infrastructure

Docker

Docker Compose

Nginx reverse proxy

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-study-assistant.git
cd ai-study-assistant

🖥️ Backend Setup (Flask)
2️⃣ Create virtual environment
cd backend
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the backend server
python app.py


Backend runs on:

http://127.0.0.1:8000

🌐 Frontend Setup (React)
1️⃣ Install dependencies
cd frontend
npm install

2️⃣ Start development server
npm start


Frontend runs on:

http://localhost:3000

🐳 Run With Docker (Full System)

Ensure Docker is installed.

1️⃣ Build and start all services
docker-compose up --build

2️⃣ Stop
docker-compose down

🧪 API Endpoints
POST /api/upload

Upload PDF and get summarized notes.

multipart/form-data:
- file: <pdf>

POST /api/summarize

Send raw text.

{
  "text": "your text here..."
}

GET /api/summary/<id>

Fetch previously generated summaries.

🔊 Text-to-Speech Support

To enable TTS:

from models.tts import text_to_speech
file = text_to_speech(summary)


Outputs MP3 audio file.

🧩 Future Enhancements

User accounts + login

Store user history

Flashcard generation

Export to Notion/Google Docs

Better summarization using GPT-4/LLMs

Fine-tuning on lecture datasets

🤝 Contribution

Pull requests are welcome!
Please open an issue for bugs or feature requests.

🪪 License

MIT License — free to use, modify, and distribute.

❤️ Acknowledgments

HuggingFace Transformers

Flask & React communities

pdfplumber / PyMuPDF

Google TTS