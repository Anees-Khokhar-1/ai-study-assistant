# backend/utils/text_chunker.py
import re
def chunk_text(text, max_chars=1000):
    text = text.strip()
    if len(text) <= max_chars:
        return [text]
    sentences = re.split(r'(?<=[\.\?\!])\s+', text)
    chunks = []
    current = ""
    for s in sentences:
        if len(current) + len(s) + 1 <= max_chars:
            current = (current + " " + s) if current else s
        else:
            if current:
                chunks.append(current)
            if len(s) > max_chars:
                for i in range(0, len(s), max_chars):
                    chunks.append(s[i:i+max_chars])
                current = ""
            else:
                current = s
    if current:
        chunks.append(current)
    return chunks 
