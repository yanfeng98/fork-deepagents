import os
from dotenv import load_dotenv
load_dotenv(".env", override=True)

from typing import Any
from langchain.chat_models import init_chat_model

model: Any = init_chat_model(
    model="openai:deepseek-v3-1-terminus",
    temperature=0.0,
    base_url=os.environ.get("OPENAI_BASE_URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)

conversation: list[dict[str, str]] = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "write a quick sort algorithm in python."},
]

response = model.invoke(conversation)
print(response)