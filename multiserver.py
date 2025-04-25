import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()

    # Create configuration dictionary
    config = {
      "mcpServers": {
        "playwright": {
          "command": "npx",
          "args": ["@playwright/mcp@latest"],
          "env": {
            "DISPLAY": ":1"
          }
        }
      }
    }

    # Create MCPClient from configuration dictionary
    #client = MCPClient.from_dict(config)
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "client_config.json"))

    # Create LLM
    os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
    os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
    llm=ChatOpenAI(model='gpt-4o-mini')

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)
    #agent.run()

    # Run the query
    result = await agent.run(
    "Search for good india food near chicago",
     # Explicitly use the airbnb server
)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())