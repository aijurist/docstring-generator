import os
from dotenv import load_dotenv

def get_gemini_api_key():

    load_dotenv()
    
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")
    
    return api_key