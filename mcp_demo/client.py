"""
MCP Client for demonstrating Model Context Protocol capabilities.

This client connects to a local MCP server and demonstrates the capabilities
of the Model Context Protocol using FastMCP. Includes examples of:
- Connection to MCP server via stdio
- Listing available tools and resources
- Calling mathematical tools
- Accessing dynamic resources

Dependencies:
- mcp: MCP client library for Python
- fastmcp: FastMCP framework for the server

Usage:
    python mcp_demo/client.py
"""
from __future__ import annotations

import asyncio
import logging
from typing import NoReturn

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MCP server configuration
SERVER_PARAMS = StdioServerParameters(
    command=".venv/bin/python",
    args=["mcp_demo/server.py"],
    env=None,
)

async def run_client() -> None:
    """
    Connect to MCP server and demonstrate its capabilities.
    
    Establishes a stdio connection with the local MCP server and executes
    a series of demonstrations including:
    - Listing available tools
    - Listing available resources  
    - Executing mathematical operations
    - Accessing greeting and farewell resources
    
    Raises:
        Exception: If connection to server fails or operations error
    """
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize MCP session
            await session.initialize()
            logger.info("MCP client connected to server")

            print("MCP Client connected to server!")
            print("=" * 50)

            # List available tools on the server
            print("\nAvailable tools:")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # List available resources on the server
            print("\nAvailable resources:")
            resources = await session.list_resources()
            for resource in resources.resources:
                print(f"  - {resource.uri}: {resource.name}")

            print("\n" + "=" * 50)

            # Demonstrate mathematical tools
            print("\nDemonstrating mathematical tools:")

            # Addition operation
            result = await session.call_tool("add", {"a": 10, "b": 5})
            print(f"  10 + 5 = {result.content[0].text}")

            # Subtraction operation
            result = await session.call_tool("subtract", {"a": 10, "b": 3})
            print(f"  10 - 3 = {result.content[0].text}")

            # Multiplication operation
            result = await session.call_tool("multiply", {"a": 7, "b": 8})
            print(f"  7 x 8 = {result.content[0].text}")

            # Division operation
            result = await session.call_tool("divide", {"a": 20, "b": 4})
            print(f"  20 / 4 = {result.content[0].text}")

            # Edge case: division by zero
            result = await session.call_tool("divide", {"a": 10, "b": 0})
            print(f"  10 / 0 = {result.content[0].text}")

            # Demonstrate dynamic resources
            print("\nDemonstrating dynamic resources:")

            # Personalized greeting resource
            greeting_resource = await session.read_resource("greeting://Juan")
            print(f"  Greeting: {greeting_resource.contents[0].text}")

            # Personalized farewell resource
            farewell_resource = await session.read_resource("farewell://Juan")
            print(f"  Farewell: {farewell_resource.contents[0].text}")

            print("\n" + "=" * 50)
            print("Demo completed successfully!")
            logger.info("MCP client demo completed successfully")


def main() -> NoReturn:
    """
    Main function that executes the MCP client.
    
    Handles asynchronous execution of the client and provides
    basic error handling for MCP connections.
    
    Raises:
        SystemExit: Always exits after completion or error
    """
    try:
        asyncio.run(run_client())
        logger.info("MCP client terminated normally")
    except KeyboardInterrupt:
        logger.info("MCP client interrupted by user")
        print("\nMCP Client interrupted by user")
    except Exception as e:
        logger.error(f"Error in MCP client: {e}")
        print(f"Error in MCP client: {e}")
        raise
    finally:
        exit(0)


if __name__ == "__main__":
    main()
# Test change
