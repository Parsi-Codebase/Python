import asyncio
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from mcp_config import create_mcp_client


async def main():
    # 1. create mcp client
    client = create_mcp_client()
    # 2. discover the tools
    tools = await client.get_tools()
    # 3. create LLM
    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0)
    # 4. create agent
    agent = create_agent(
        model=model,
        tools=tools,
    )
    while True:
        prompt = input("\nYou: ")
        if prompt == "exit":
            break
        result = await agent.ainvoke(
            {"messages": [{"role": "user", "content": prompt}]}
        )

        print("\nAI:")
        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
