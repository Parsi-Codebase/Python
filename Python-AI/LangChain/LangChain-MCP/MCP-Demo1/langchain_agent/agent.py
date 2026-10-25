import asyncio
import logging

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from mcp_config import create_mcp_client


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


MODEL_NAME = "gpt-4.1-nano"


def create_model() -> ChatOpenAI:
    """
    Create the LangChain ChatOpenAI model.
    """
    return ChatOpenAI(
        model=MODEL_NAME,
        temperature=0,
    )


def create_langchain_agent(model: ChatOpenAI, tools: list):
    """
    Create a LangChain agent using the MCP-discovered tools.
    """
    return create_agent(
        model=model,
        tools=tools,
    )


async def load_mcp_tools(client) -> list:
    """
    Connect to the configured MCP server through stdio
    and discover its tools.

    MultiServerMCPClient converts MCP tools into
    LangChain-compatible tools.
    """
    logger.info("Connecting to MCP server...")
    logger.info("Transport: stdio")

    try:
        tools = await client.get_tools()
    except (OSError, RuntimeError, ValueError) as exc:
        logger.exception("MCP server connection/tool discovery failed.")
        raise RuntimeError(
            "Unable to connect to the MCP server or discover its tools."
        ) from exc

    logger.info("MCP server connection successful.")
    logger.info("Discovered %d MCP tools.", len(tools))

    for tool in tools:
        logger.info("  - %s", tool.name)

    return tools


async def run_agent(agent) -> None:
    """
    Execute the LangChain agent with a user request.
    """
    user_prompt = "Calculate the cost of 5 products at ₹2000 each."

    logger.info("Executing LangChain agent...")
    logger.info("User: %s", user_prompt)

    try:
        result = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_prompt,
                    }
                ]
            }
        )
    except (RuntimeError, ValueError) as exc:
        logger.exception("Agent execution failed.")
        raise RuntimeError(
            "LangChain agent execution failed."
        ) from exc

    final_message = result["messages"][-1].content

    print("\nFinal Response:")
    print(final_message)


async def main() -> None:
    logger.info("Starting MCP + LangChain application.")

    # ---------------------------------------------------------
    # 1. Create MCP client
    # ---------------------------------------------------------
    client = create_mcp_client()

    # ---------------------------------------------------------
    # 2. Create OpenAI model
    # ---------------------------------------------------------
    model = create_model()

    logger.info("OpenAI model created: %s", MODEL_NAME)

    # ---------------------------------------------------------
    # 3. Discover MCP tools
    #
    # MCP Server
    #      ↓
    # stdio
    #      ↓
    # MultiServerMCPClient
    #      ↓
    # LangChain-compatible tools
    # ---------------------------------------------------------
    tools = await load_mcp_tools(client)

    # ---------------------------------------------------------
    # 4. Create LangChain agent
    # ---------------------------------------------------------
    agent = create_langchain_agent(
        model=model,
        tools=tools,
    )

    logger.info("LangChain agent created successfully.")

    # ---------------------------------------------------------
    # 5. Execute the agent
    # ---------------------------------------------------------
    await run_agent(agent)

    logger.info("Application completed successfully.")


if __name__ == "__main__":
    asyncio.run(main())