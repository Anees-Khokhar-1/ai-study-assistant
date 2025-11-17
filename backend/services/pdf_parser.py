# backend/services/pdf_parser.py
import pdfplumber
def parse_pdf(file_storage):
    text_parts = []
    try:
        # pdfplumber can read file-like objects
        with pdfplumber.open(file_storage.stream) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
    except Exception:
        pass
    return "\n".join(text_parts).strip()