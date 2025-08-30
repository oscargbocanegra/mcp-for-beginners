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
import json
import logging
import os
from typing import NoReturn

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MCP server configuration
SERVER_PARAMS = StdioServerParameters(
    command=".venv/bin/python",
    args=["mcp_demo/server.py"],
    env=None,
)

def convert_to_llm_tool(tool):
    """Convert MCP tool to LLM-compatible tool schema."""
    tool_schema = {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "type": "function",
            "parameters": {
                "type": "object",
                "properties": tool.inputSchema["properties"]
            }  
        }
    }
    return tool_schema


def call_llm(prompt: str, functions: list) -> list:
    """Call LLM with prompt and available functions."""
    # Call the LLM with the prompt and functions
    token = os.getenv("MCP_CLIENT")
    endpoint = "https://models.inference.ai.azure.com"
    
    model_name = "gpt-4o"
    
    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
    )

    print("CALLING LLM")
    response = client.complete(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model=model_name,
        tools=functions,
        # Optional parameters
        temperature=1.,
        max_tokens=1000,
        top_p=1.    
    )

    response_message = response.choices[0].message
    
    functions_to_call = []

    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            print("TOOL: ", tool_call)
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            functions_to_call.append({"name": name, "args": args})

    return functions_to_call

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
            
            # Optional: LLM integration demo (requires Azure token)
            if os.getenv("MCP_CLIENT"):
                print("\nDemonstrating LLM integration:")
                functions = []
                
                for tool in tools.tools:
                    print("Tool: ", tool.name)
                    print("Tool: ", tool.inputSchema["properties"])

                    # Create a function for each tool
                    functions.append(convert_to_llm_tool(tool))

                prompt = "Add 2 to 20"

                try:
                    # ask LLM what tools to call, if any
                    functions_to_call = call_llm(prompt, functions)

                    # call suggested functions
                    for f in functions_to_call:
                        result = await session.call_tool(f["name"], arguments=f["args"])
                        print("TOOLS result: ", result.content)
                except Exception as e:
                    logger.warning(f"LLM integration failed: {e}")
                    print(f"LLM integration skipped: {e}")
            else:
                print("\nLLM integration skipped (no MCP_CLIENT token found)")
                print("Set MCP_CLIENT environment variable to test Azure integration")
            
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
