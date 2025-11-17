# backend/models/summarizer.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from utils.text_chunker import chunk_text

class Summarizer:
    def __init__(self, model_name="sshleifer/distilbart-cnn-12-6", device=-1):
        self.model_name = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.pipeline = pipeline("summarization", model=self.model, tokenizer=self.tokenizer, device=self.device)

    def summarize(self, text, max_chunk_chars=1000, max_length=150, min_length=40):
        if not text or not text.strip():
            return ""
        chunks = chunk_text(text, max_chunk_chars)
        if len(chunks) == 1:
            out = self.pipeline(chunks[0], max_length=max_length, min_length=min_length, do_sample=False)
            return out[0]["summary_text"].strip()
        partials = []
        for c in chunks:
            o = self.pipeline(c, max_length=max_length, min_length=min_length, do_sample=False)
            partials.append(o[0]["summary_text"].strip())
        merged = " ".join(partials)
        final = self.pipeline(merged, max_length=max_length, min_length=min_length, do_sample=False)
        return final[0]["summary_text"].strip() 