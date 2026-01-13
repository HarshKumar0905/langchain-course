from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent

load_dotenv()

tools = [TavilySearch()]
react_prompt = hub.pull("hwchase17/react")
# Upgraded to Gemini 3 Flash for improved performance and reasoning
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor

def main():
    result = chain.invoke(
        input={
            "input": "Fetch me the latest 3 job openings for AI Engineer from linkedin in the NYC region."
        }
    )
    print(result)

if __name__ == "__main__":
    main()