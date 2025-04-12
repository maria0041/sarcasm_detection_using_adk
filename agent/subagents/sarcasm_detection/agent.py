from google.adk.agents import Agent
from .prompt import SYSTEM_PROMPT




sarcasm_detection = Agent(
    name="sarcasm_detection_agent",
    model="gemini-2.0-flash-exp",
    description=(
        "Agent to detect sarcasm in text. "
    ),
    instruction=(
        SYSTEM_PROMPT
    ),
)