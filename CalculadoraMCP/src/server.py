import json
import random
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("calculadoramcp")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers.
    
    Args:
        a: First number to add
        b: Second number to add
        
    Returns:
        The sum of a and b
    """
    return a + b

@server.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
        
    Returns:
        The difference of a and b
    """
    return a - b

@server.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers.
    
    Args:
        a: First number to multiply
        b: Second number to multiply
        
    Returns:
        The product of a and b
    """
    return a * b

@server.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers.
    
    Args:
        a: Number to divide (dividend)
        b: Number to divide by (divisor)
        
    Returns:
        The quotient of a divided by b
        
    Raises:
        ValueError: If b is zero (division by zero)
    """
    if b == 0:
        raise ValueError("Division by zero attempted")
    return a / b