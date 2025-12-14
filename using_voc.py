# read the api key from the .env file
from dotenv import load_dotenv
load_dotenv()
import os

import requests

url = "https://claude.vocareum.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "x-api-key": os.getenv("LLM_API_KEY"),
    "anthropic-version": "2023-06-01"
}
data = {
    "model": "claude-sonnet-4-5-20250929",
    "max_tokens": 1024,
    "messages": [
        {"role": "system", "content": "You are a helpful assistant. always start with \"Hi Dear\""},
        {"role": "user", "content": "Hello, Claude!"}
    ]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
# print(result)
print(result["choices"][0]["message"]["content"])
