# backend/utils/cleanup.py
import re
def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()
