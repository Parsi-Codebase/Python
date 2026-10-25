import asyncio
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient(
        {
            "products": {
                "transport": "stdio",
                "command": "uv",
                "args": ["run", "python", "mcp_server/server.py"],
            }
        }
    )
    model = ChatOpenAI(model="gpt-5-nano", temperature=0)
    tools = await client.get_tools()
    # print(f"\nTool: {tool.name}")
    # print(f"Description: {tool.description}")
    agent = create_agent(model=model, tools=tools)
    while True:
        prompt = input("\nYou: ")
        if prompt == "exit":
            break
        
        result = await agent.ainvoke(
            {"messages": [{"role": "user", "content": prompt}]}
        )
        
        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
