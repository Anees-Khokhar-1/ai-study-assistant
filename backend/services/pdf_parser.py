import pdfplumber
import pytesseract
from io import BytesIO

def parse_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        if not text:  # fallback to OCR
            text = ocr_pdf(file)
    return text

def ocr_pdf(file):
    from PIL import Image
    import pytesseract
    img = Image.open(BytesIO(file.read()))
    text = pytesseract.image_to_string(img)
    return text
