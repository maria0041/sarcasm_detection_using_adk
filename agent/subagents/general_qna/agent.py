from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from agent.share_libraries import constants


question_answering_agent = Agent(
    model=constants.MODEL,
    name="general_question_answering_agent",
    description="An agent that answers general questions and uses Google Search when needed.",
    instruction="You are a helpful assistant who answers questions and uses Google Search to find information when needed. You specialize in truck shipments",
    # tools=[GoogleSearchTool()],
    
)
