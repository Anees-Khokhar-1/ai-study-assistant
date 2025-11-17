# backend/app.py
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# fixed import path to backend/model/
from model.summarizer import Summarizer
from services.pdf_parser import parse_pdf
from services.storage import save_summary, get_summary_by_id

# Config
MODEL_NAME = os.environ.get("SUMMARIZER_MODEL", "sshleifer/distilbart-cnn-12-6")  # lightweight default
DEVICE = int(os.environ.get("MODEL_DEVICE", "-1"))  # -1 = CPU, 0 = GPU

app = Flask(__name__)
CORS(app)

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Study Assistant Backend is running.",
        "routes": {
            "/summarize": "POST - Summarize text",
            "/chat": "POST - Chat with AI (placeholder)",
            "/mcq": "POST - Generate MCQs (placeholder)",
            "/notes": "POST - Generate Notes",
            "/api/upload": "POST - Upload PDF and summarize",
            "/api/summary/<id>": "GET - Fetch saved summary"
        }
    })

# Load model once (avoid debug reloader running it twice in production)
print(f">>> Loading summarizer model ({MODEL_NAME})... (device={DEVICE})")
summarizer = Summarizer(model_name=MODEL_NAME, device=DEVICE)
print(">>> Summarizer model loaded successfully.")


@app.route("/summarize", methods=["POST"])
def summarize_text():
    payload = request.get_json(force=True, silent=True)
    if not payload or "text" not in payload:
        return jsonify({"error": "Missing 'text' in request body"}), 400
    text = payload["text"]
    summary = summarizer.summarize(text)
    return jsonify({"summary": summary})


@app.route("/chat", methods=["POST"])
def chat():
    payload = request.get_json(force=True, silent=True)
    if not payload or "message" not in payload:
        return jsonify({"error": "Missing 'message'"}), 400
    msg = payload["message"]
    # placeholder: echo + summarize short context
    reply = f"AI Reply (placeholder): {msg}"
    return jsonify({"reply": reply})


@app.route("/mcq", methods=["POST"])
def mcq():
    payload = request.get_json(force=True, silent=True)
    if not payload or "text" not in payload:
        return jsonify({"error": "Missing 'text'"}), 400
    text = payload["text"]
    # placeholder simple MCQ generation: pick first sentence and make dummy options
    sentences = text.strip().split(".")
    question = sentences[0].strip() if sentences and sentences[0] else "What is the main idea?"
    mcq = [{
        "question": question + "?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": "Option A"
    }]
    return jsonify({"mcq": mcq})


@app.route("/notes", methods=["POST"])
def notes():
    payload = request.get_json(force=True, silent=True)
    if not payload or "text" not in payload:
        return jsonify({"error": "Missing 'text'"}), 400
    text = payload["text"]
    # Use summarizer to produce compact notes — return bullets
    summary = summarizer.summarize(text)
    # simple bullet split by sentence
    bullets = [s.strip() for s in summary.split(".") if s.strip()]
    return jsonify({"notes": bullets})


@app.route("/api/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    text = parse_pdf(file)
    if not text or not text.strip():
        return jsonify({"error": "No readable text extracted from PDF"}), 400
    summary = summarizer.summarize(text)
    summary_id = save_summary(text, summary)
    return jsonify({"summary_id": summary_id, "summary": summary})


@app.route("/api/summary/<summary_id>", methods=["GET"])
def get_summary(summary_id):
    rec = get_summary_by_id(summary_id)
    if not rec:
        return jsonify({"error": "Summary not found"}), 404
    return jsonify({"summary_id": summary_id, "text": rec["text"], "summary": rec["summary"]})


if __name__ == "__main__":
    # debug=False prevents double-loading the model in the dev reloader
    app.run(host="127.0.0.1", port=5000, debug=False)
