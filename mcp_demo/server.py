"""
MCP Server for mathematical operations and greetings.

This server provides a FastMCP-based Model Context Protocol server with:
- Mathematical operations: add, subtract, multiply, divide
- Dynamic greeting and farewell resources

Dependencies:
- fastmcp: FastMCP framework for building MCP servers

Usage:
    uv run python mcp/server.py
"""
from __future__ import annotations

import logging

from fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create MCP server instance
mcp = FastMCP("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers.
    
    Args:
        a: First number to add
        b: Second number to add
        
    Returns:
        The sum of a and b
    """
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
        
    Returns:
        The difference of a and b
    """
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers.
    
    Args:
        a: First number to multiply
        b: Second number to multiply
        
    Returns:
        The product of a and b
    """
    return a * b


@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        The quotient of a and b, or 0 if b is zero
        
    Note:
        Returns 0 for division by zero instead of raising an exception
        to maintain compatibility with existing client expectations.
    """
    if b == 0:
        logger.warning("Division by zero attempted, returning 0")
        return 0
    return a / b


@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Generate a personalized greeting.
    
    Args:
        name: Name of the person to greet
        
    Returns:
        A greeting message for the specified name
    """
    return f"Hello, {name}!"


@mcp.resource("farewell://{name}")
def farewell(name: str) -> str:
    """Generate a personalized farewell.
    
    Args:
        name: Name of the person to bid farewell
        
    Returns:
        A farewell message for the specified name
    """
    return f"Goodbye, {name}!"


def main() -> None:
    """Start the MCP server."""
    logger.info("Starting MCP server")
    mcp.run()


if __name__ == "__main__":
    main()


