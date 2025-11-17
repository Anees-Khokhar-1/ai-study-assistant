# backend/config.py
import os

APP_NAME = "AI Study Assistant Backend"
DEBUG = True
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {"pdf", "txt"}
CHUNK_SIZE = 2000
MODEL_NAME = os.environ.get("SUMMARIZER_MODEL", "sshleifer/distilbart-cnn-12-6")
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
