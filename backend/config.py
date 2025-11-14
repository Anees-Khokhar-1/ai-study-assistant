import os
from dotenv import load_dotenv

load_dotenv()

# Example of loading environment variables from a `.env` file
MODEL_NAME = os.getenv('MODEL_NAME', 'facebook/bart-large-cnn')
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///summaries.db') 