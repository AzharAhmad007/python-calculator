from mcp.server.fastmcp import FastMCP

from backend.calculator import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
)

# Initialize the MCP server
mcp = FastMCP("Python Calculator")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum."""
    return add(a, b)


@mcp.tool()
def subtract_numbers(a: float, b: float) -> float:
    """Subtract the second number from the first number."""
    return subtract(a, b)


@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers and return their product."""
    return multiply(a, b)


@mcp.tool()
def divide_numbers(a: float, b: float) -> float:
    """Divide the first number by the second number."""
    return divide(a, b)


@mcp.tool()
def modulus_numbers(a: float, b: float) -> float:
    """Return the remainder after dividing the first number by the second."""
    return modulus(a, b)


@mcp.tool()
def power_numbers(a: float, b: float) -> float:
    """Raise the first number to the power of the second number."""
    return power(a, b)


if __name__ == "__main__":
    mcp.run(transport="stdio")