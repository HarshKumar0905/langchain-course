from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent

from schemas import AgentResponse

load_dotenv()

tools = [TavilySearch()]
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

agent = create_agent(
    model, 
    tools=tools, 
    response_format=AgentResponse)

def main():
    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Search 3 job openings for AI Engineer from linkedin in the NYC region."
            }
        ]
    })
    print(result["structured_response"])

if __name__ == "__main__":
    main()