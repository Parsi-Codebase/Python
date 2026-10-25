from typing import Any

from langchain_mcp_adapters.client import MultiServerMCPClient


MCP_SERVER_CONFIG: dict[str, dict[str, Any]] = {
    "calculator": {
        "command": "uv",
        "args": [
            "run",
            "mcp_server/server.py",
        ],
        "transport": "stdio",
    }
}


def create_mcp_client() -> MultiServerMCPClient:
    """
    Create the LangChain MCP client.

    MultiServerMCPClient is the adapter layer between
    MCP servers and LangChain tools.
    """
    return MultiServerMCPClient(MCP_SERVER_CONFIG)