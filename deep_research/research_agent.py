import os
from dotenv import load_dotenv
load_dotenv(".env", override=True)

from typing import Any
from datetime import datetime
from langchain.chat_models import init_chat_model
from deepagents import create_deep_agent
from deepagents.backends.utils import file_data_to_string

from utils import show_prompt, format_messages
from research_agent.prompts import (
    RESEARCHER_INSTRUCTIONS,
    RESEARCH_WORKFLOW_INSTRUCTIONS,
    SUBAGENT_DELEGATION_INSTRUCTIONS,
)
from research_agent.tools import tavily_search, think_tool

tools: list[Any] = [tavily_search, think_tool]

show_prompt(RESEARCHER_INSTRUCTIONS)
current_date: str = datetime.now().strftime("%Y-%m-%d")
research_sub_agent: dict[str, Any] = {
    "name": "research-agent",
    "description": "Delegate research to the sub-agent researcher. Only give this researcher one topic at a time.",
    "system_prompt": RESEARCHER_INSTRUCTIONS.format(date=current_date),
    "tools": [tavily_search, think_tool],
}

max_concurrent_research_units: int = 3
max_researcher_iterations: int = 3
INSTRUCTIONS: str = (
    RESEARCH_WORKFLOW_INSTRUCTIONS
    + "\n\n"
    + "=" * 80
    + "\n\n"
    +  SUBAGENT_DELEGATION_INSTRUCTIONS.format(
        max_concurrent_research_units=max_concurrent_research_units,
        max_researcher_iterations=max_researcher_iterations,
    )
)
show_prompt(INSTRUCTIONS)

model: Any = init_chat_model(
    model="openai:deepseek-v3-1-terminus",
    temperature=0.0,
    base_url=os.environ.get("OPENAI_BASE_URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)

agent: Any = create_deep_agent(
    model=model,
    tools=tools,
    system_prompt=INSTRUCTIONS,
    subagents=[research_sub_agent],
)

png_data: bytes = agent.get_graph().draw_mermaid_png()
png_path: str = "agent_workflow.png"
with open(png_path, "wb") as f:
    f.write(png_data)
print(f"Workflow diagram saved to {png_path}")

result: dict[str, Any] | Any = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "research context engineering approaches used to build AI agents",
            }
        ],
    }, 
)
format_messages(result["messages"])

file_content: str = file_data_to_string(result["files"]['/final_report.md'])
show_prompt(file_content) 