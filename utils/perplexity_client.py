import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Perplexity API key
API_KEY = os.environ.get("PERPLEXITY_API_KEY")
BASE_URL = "https://api.perplexity.ai/v1/chat/completions"

def perplexity_chat_completion(messages, model="pplx-70b-chat", temperature=0.7, max_tokens=1000):
    if not API_KEY:
        raise ValueError("API key not found. Please set the PERPLEXITY_API_KEY environment variable.")
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(BASE_URL, headers=headers, json=payload)
    response.raise_for_status()  # throws error if the request fails
    return response.json()["choices"][0]["message"]["content"]

# Example usage:
# messages = [{"role": "user", "content": "Hello, Perplexity!"}]
# print(perplexity_chat_completion(messages))
