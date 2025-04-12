from google.adk.agents import Agent
from .prompt import SYSTEM_PROMPT
from .share_libraries import constants
from .subagents.sarcasm_detection.agent import sarcasm_detection
from .subagents.general_qna.agent import question_answering_agent


root_agent = Agent(
    name="NLP_agent",
    model=constants.MODEL,
    description=(
        "Handles NLP tasks, including sarcasm detection and general conversation."
    ),
    instruction=(
        SYSTEM_PROMPT
    ),
    sub_agents=[
        sarcasm_detection,
        question_answering_agent,
    ]
)