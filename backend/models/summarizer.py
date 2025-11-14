from transformers import pipeline

class Summarizer:
    def __init__(self, model_name='facebook/bart-large-cnn', device=-1):
        self.pipeline = pipeline('summarization', model=model_name, device=device)

    def summarize(self, text, max_len=200, min_len=50):
        # Naive single-call summarization — replace with chunking for long text
        out = self.pipeline(text, max_length=max_len, min_length=min_len, do_sample=False)
        return out[0]['summary_text']
