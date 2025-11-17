# backend/models/tts.py
import hashlib
from pathlib import Path
import os

AUDIO_DIR = Path(__file__).resolve().parents[1] / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# try gTTS then pyttsx3
try:
    from gtts import gTTS
    _GTTS = True
except Exception:
    _GTTS = False

try:
    import pyttsx3
    _PYT = True
except Exception:
    _PYT = False

def _hash_text(text: str, lang="en", voice="default"):
    key = f"{text}|{lang}|{voice}"
    return hashlib.sha1(key.encode("utf-8")).hexdigest()

def text_to_speech(text: str, lang="en", voice="default", force=False):
    if not text.strip():
        raise ValueError("Empty text")
    h = _hash_text(text, lang, voice)
    mp3_path = AUDIO_DIR / f"tts_{h}.mp3"
    wav_path = AUDIO_DIR / f"tts_{h}.wav"

    if mp3_path.exists() and not force:
        return str(mp3_path.resolve())

    if _GTTS:
        try:
            tts = gTTS(text=text, lang=lang)
            tts.save(str(mp3_path))
            return str(mp3_path.resolve())
        except Exception:
            pass

    if _PYT:
        try:
            engine = pyttsx3.init()
            engine.save_to_file(text, str(wav_path))
            engine.runAndWait()
            # prefer wav if no conversion available
            return str(wav_path.resolve())
        except Exception as e:
            raise RuntimeError("pyttsx3 error: " + str(e))

    raise RuntimeError("No TTS engine available. Install gTTS or pyttsx3.")
