from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet
    Args :
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

class Source(BaseModel):
    """Scheme for a source used by agent"""

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Scheme for agent response"""

    answer: str = Field(description="The final answer from the agent")
    sources: List[Source] = Field(default_factory=list, description="The list of sources used by the agent")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tools = [search]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for an ai engineer in New York in linkedin and list their details")})
    print(f"Agent result: {result}")

if __name__ == "__main__":
    main()