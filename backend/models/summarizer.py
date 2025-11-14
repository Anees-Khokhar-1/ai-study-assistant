# backend/models/summarizer.py

from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

class Summarizer:
    def __init__(self, model_name='facebook/bart-large-cnn', device=-1):
        """
        Initializes the Summarizer with a specified model and device.
        
        Args:
            model_name (str): The name of the Hugging Face model to load (default: 'facebook/bart-large-cnn').
            device (int): The device to run the model on (-1 for CPU, 0 for GPU) (default: -1).
        """
        # Load tokenizer and model using AutoModelForSeq2SeqLM for sequence-to-sequence tasks
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        # Set up the summarization pipeline
        self.pipeline = pipeline('summarization', model=self.model, tokenizer=self.tokenizer, device=device)

    def summarize(self, text):
        """
        Summarizes the given text using the initialized summarization pipeline.
        
        Args:
            text (str): The input text to summarize.
        
        Returns:
            list: A list of dictionaries containing the summary text.
        """
        return self.pipeline(text)

# Example usage (this part is for demonstration, you can remove it or use it as needed)
if __name__ == "__main__":
    summarizer = Summarizer(model_name='facebook/bart-large-cnn')
    text = """
    The quick brown fox jumps over the lazy dog. This is a classic sentence used to test fonts and keyboards.
    It contains every letter of the alphabet, making it ideal for font rendering tests. The sentence is short but full of information.
    """
    summary = summarizer.summarize(text)
    print(summary)
