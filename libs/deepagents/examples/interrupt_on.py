import os
from typing import Any
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from deepagents import create_deep_agent
from utils import format_messages

@tool
def get_weather(city: str) -> str:
    """Get the weather in a city."""
    return f"The weather in {city} is sunny."

model: Any = init_chat_model(
    model="openai:deepseek-v3-1-terminus",
    temperature=0.0,
    base_url=os.environ.get("OPENAI_BASE_URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)

agent = create_deep_agent(
    model=model,
    tools=[get_weather],
    interrupt_on={
        "get_weather": {
            "allowed_decisions": ["approve", "edit", "reject"]
        },
    }
)

png_data: bytes = agent.get_graph().draw_mermaid_png()
png_path: str = "interrupt_on.png"
with open(png_path, "wb") as f:
    f.write(png_data)
print(f"Workflow diagram saved to {png_path}")

result: dict[str, Any] | Any = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "北京的天气怎么样",
            }
        ],
    }, 
)

format_messages(result["messages"])