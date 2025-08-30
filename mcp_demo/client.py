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
from pathlib import Path
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from openai import OpenAI


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MCP server configuration
SERVER_PARAMS = StdioServerParameters(
    command=".venv/bin/python",
    args=["mcp_demo/server.py"],
    env=None,
)

def load_env_file(env_file_path: str = ".env") -> None:
    """
    Load environment variables from .env file if it exists.
    
    Args:
        env_file_path: Path to the .env file relative to project root
        
    Note:
        This is a simple implementation. For production use, consider python-dotenv
    """
    env_path = Path(env_file_path)
    if env_path.exists():
        logger.info(f"Loading environment variables from {env_path}")
        with open(env_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key and not os.getenv(key):  # Don't override existing env vars
                        os.environ[key] = value
                        logger.debug(f"Set environment variable: {key}")
    else:
        logger.debug(f"No .env file found at {env_path}")


def get_openai_token() -> str:
    """
    Get OpenAI token from environment variables.
    
    Returns:
        The OpenAI token string
        
    Raises:
        ValueError: If no token is found in any source
        
    Note:
        Checks multiple sources in order of precedence:
        1. MCP_OPENAI environment variable
        2. GITHUB_TOKEN environment variable (fallback)
        3. .env file (loaded automatically)
    """
    # Try to load from .env file first
    load_env_file()
    
    # Check environment variables in order of preference
    token = os.getenv("MCP_OPENAI") or os.getenv("GITHUB_TOKEN")
    
    if not token:
        raise ValueError(
            "No GitHub token found. Please set MCP_OPENAI environment variable "
            "or create a .env file with MCP_OPENAI=your_token"
        )
    
    logger.info("GitHub token loaded successfully")
    return token


def convert_to_llm_tool(tool: Any) -> dict[str, Any]:
    """
    Convert MCP tool to LLM-compatible tool schema.
    
    Args:
        tool: MCP tool object with name, description, and inputSchema
        
    Returns:
        Dictionary containing the tool schema in OpenAI format
    """
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": {
                "type": "object",
                "properties": tool.inputSchema["properties"],
                "required": tool.inputSchema.get("required", []),
            },
        },
    }


def call_llm(prompt: str, functions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Call LLM with prompt and available functions.
    
    Args:
        prompt: User prompt to send to the LLM
        functions: List of available function schemas in OpenAI tool format
        
    Returns:
        List of functions to call with their arguments, each containing:
        - name: Function name to call
        - args: Dictionary of function arguments
        
    Raises:
        ValueError: If token is not available
        Exception: If LLM call fails or response parsing errors occur
    """
    token = get_openai_token()
    endpoint = "https://models.github.ai/inference"
    model_name = "o3-mini"
    
    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )

    logger.info(f"Calling LLM with prompt: {prompt}")
    logger.debug(f"Available functions: {[f['function']['name'] for f in functions]}")
    
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Use the available tools when needed to solve problems accurately.",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]
    
    try:
        response = client.chat.completions.create(
            messages=messages,
            model=model_name,
            tools=functions if functions else None,
            # Removed temperature parameter - not supported by o3-mini
        )
        
        response_message = response.choices[0].message
        
        if response_message.content:
            logger.info(f"LLM response: {response_message.content}")
        
        functions_to_call = []
        
        if response_message.tool_calls:
            logger.info(f"LLM suggested {len(response_message.tool_calls)} tool calls")
            for tool_call in response_message.tool_calls:
                logger.debug(f"Tool call: {tool_call.function.name} with args: {tool_call.function.arguments}")
                
                try:
                    name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)
                    functions_to_call.append({"name": name, "args": args})
                except json.JSONDecodeError as e:
                    logger.error(f"Failed to parse tool arguments: {tool_call.function.arguments}")
                    raise ValueError(f"Invalid JSON in tool arguments: {e}") from e
        else:
            logger.debug("No tool calls suggested by LLM")
        
        return functions_to_call
        
    except Exception as e:
        logger.error(f"Error calling LLM: {e}")
        raise


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
    try:
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
                
                # Optional: LLM integration demo (requires token)
                try:
                    token = get_openai_token()
                    print("\nDemonstrating LLM integration:")
                    functions = []
                    
                    for tool in tools.tools:
                        logger.debug(f"Converting tool: {tool.name}")
                        functions.append(convert_to_llm_tool(tool))

                    prompt = "Add 2 to 25"

                    # Ask LLM what tools to call, if any
                    functions_to_call = call_llm(prompt, functions)

                    # Call suggested functions
                    for f in functions_to_call:
                        result = await session.call_tool(f["name"], arguments=f["args"])
                        print(f"Tool result: {result.content[0].text}")
                        
                    if not functions_to_call:
                        print("LLM didn't suggest any tool calls for this prompt")
                        
                except ValueError as e:
                    print(f"\nLLM integration skipped: {e}")
                    print("To enable LLM integration:")
                    print("1. Set MCP_OPENAI environment variable, or")
                    print("2. Create a .env file with: MCP_OPENAI=your_github_token")
                except Exception as e:
                    logger.warning(f"LLM integration failed: {e}")
                    print(f"LLM integration failed: {e}")

                print("\nMCP Client demo completed. Disconnecting...")
                logger.info("MCP client disconnected from server")
                
    except Exception as e:
        logger.error(f"Error in MCP client session: {e}")
        raise


def main() -> None:
    """
    Main function that executes the MCP client.
    
    Handles asynchronous execution of the client and provides
    basic error handling for MCP connections.
    """
    exit_code = 0
    
    try:
        asyncio.run(run_client())
        logger.info("MCP client terminated normally")
    except KeyboardInterrupt:
        logger.info("MCP client interrupted by user")
        print("\nMCP Client interrupted by user")
    except asyncio.CancelledError:
        logger.info("MCP client tasks were cancelled")
        print("MCP Client tasks were cancelled")
    except Exception as e:
        logger.error(f"Error in MCP client: {e}")
        print(f"Error in MCP client: {e}")
        exit_code = 1
    finally:
        # Ensure any remaining tasks are cleaned up
        try:
            # Cancel any remaining tasks
            pending = asyncio.all_tasks()
            for task in pending:
                if not task.done():
                    task.cancel()
            
            # Wait briefly for cleanup
            if pending:
                asyncio.get_event_loop().run_until_complete(
                    asyncio.wait_for(
                        asyncio.gather(*pending, return_exceptions=True),
                        timeout=1.0
                    )
                )
        except Exception as cleanup_error:
            logger.debug(f"Cleanup error (non-critical): {cleanup_error}")
        
        exit(exit_code)


if __name__ == "__main__":
    main()
