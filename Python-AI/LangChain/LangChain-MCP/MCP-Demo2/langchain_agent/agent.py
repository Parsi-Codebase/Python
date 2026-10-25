import asyncio
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from mcp_config import create_mcp_client
from langgraph.checkpoint.memory import InMemorySaver
checkpointer=InMemorySaver()
async def main():
    # 1 . Create MCP client
    client=create_mcp_client()
    # 2. Discover MCP tools
    tools=await client.get_tools()
    # 3. Create Open AI model
    model=ChatOpenAI(
        model='gpt-4.1-nano',
        temperature=0
    )
    # 4. Create langchain agent
    agent=create_agent(
        model=model,
        tools=tools,
        checkpointer=checkpointer
    )
    # 5 . Send User Request
    while True:
        prompt=input('\nYou: ')
        if prompt=="exit":
            break
        resulut=await agent.ainvoke(
            {
                'messages':[
                    {
                        'role':'user',
                        'content':prompt
                    }
                ]
            },
            config={
                'configurable':{
                    'thread_id':'procurement-001'
                }
            }
        )
        # 6. Display response
        print('\nAI: ')
        print(resulut['messages'][-1].content)
if __name__=='__main__':
    asyncio.run(main())