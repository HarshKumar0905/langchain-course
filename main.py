from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent

load_dotenv()
client = Client()
tools = [TavilyClient()]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt = client.pull_prompt("hwchase17/react")
agent = create_agent(model=llm, tools=tools)

def main():
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for an ai engineer in New York in linkedin and list their details")})


if __name__ == "__main__":
    main()