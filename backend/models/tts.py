from gtts import gTTS
import os

def text_to_speech(text, lang='en', filename='summary.mp3'):
    tts = gTTS(text, lang=lang)
    tts.save(filename)
    return filename
