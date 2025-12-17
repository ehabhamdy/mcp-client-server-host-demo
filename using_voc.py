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
        {"role": "user", "content": "Hello, Claude! what is are the tools you have access to?"}
    ],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_stock_price",
                "description": "Get the current stock price for a given ticker symbol.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
                        }
                        },
                    "required": ["ticker"]
                }
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)
print(result["choices"][0]["message"]["content"])
