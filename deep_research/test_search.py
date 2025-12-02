from dotenv import load_dotenv
load_dotenv(".env", override=True)

# To install: pip install tavily-python
from tavily import TavilyClient

client = TavilyClient()
response = client.search(
    query="如何在 Python 中使用 asyncio？",
)
print(response)