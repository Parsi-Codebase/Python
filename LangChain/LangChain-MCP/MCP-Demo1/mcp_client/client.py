import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="uv",
        args=["run", "mcp_server/server.py"],
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("Available tools:")
            for tool in tools.tools:
                print(tool.name)
            result=await session.call_tool(
                'calculate_total',
                {
                    'price':2000,
                    'quantity':5
                }
            )
            print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())