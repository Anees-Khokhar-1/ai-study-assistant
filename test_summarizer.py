from backend.models.summarizer import Summarizer

def test_summarizer():
    summarizer = Summarizer(model_name='facebook/bart-large-cnn', device=-1)
    text = """
    OpenAI is an AI research lab that focuses on developing advanced AI models.
    It was founded in December 2015 with the goal of advancing digital intelligence
    in a way that could benefit humanity as a whole. The lab is known for developing 
    the GPT (Generative Pretrained Transformer) series of models, including GPT-3,
    which has been widely used for natural language processing tasks.
    """
    summary = summarizer.summarize(text)
    print("Summary:", summary)

if __name__ == "__main__":
    test_summarizer()
