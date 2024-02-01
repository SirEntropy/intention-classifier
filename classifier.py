import openai
from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_text(text):
    base_prompt = """
    Please classify the user questions into one of the following categories:
    1. Greetings
    2. Data Security
    3. Software Development
    4. Documentation
    """
    messages = [{"role": "system", "content": base_prompt}, {"role": "user", "content": text}]
    
    client = OpenAI()
    res = client.chat.completions.create(
        model = "gpt-4-1106-preview",
        messages = messages
    )
    
    return res