from typing import Any
from langchain_mcp_adapters.client import MultiServerMCPClient
MCP_SERVER_CONFIG:dict[str,dict[str,Any]]={
    'procurement':{
        'command':'uv',
        'args':[
            'run',
            'mcp_server/procurement_server.py'
        ],
        'transport':'stdio'
    }
}
def create_mcp_client()->MultiServerMCPClient:
    return MultiServerMCPClient(MCP_SERVER_CONFIG)