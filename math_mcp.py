from fastmcp import FastMCP
import math_mcp

math_mcp = FastMCP("Math MCP Server")

MATH_CONSTANTS = {
    "pi": 3.14159,
    "e": 2.71828,
    "phi": 1.61803,
    "golden_ratio": 1.61803,
}

@math_mcp.tool
def add(a: float, b: float) -> str:
    """ Add two numbers together.
    
    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        str: The sum of the two numbers.
    """
    result = a + b
    return f"{a} + {b} = {result}"

@math_mcp.tool
def subtract(a: float, b: float) -> str:
    """ Subtract two numbers.
    
    Args:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        str: The difference of the two numbers.
    """
    result = a - b
    return f"{a} - {b} = {result}"

@math_mcp.tool
def multiply(a: float, b: float) -> str:
    """ Multiply two numbers.
    
    Args:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        str: The product of the two numbers.
    """
    result = a * b
    return f"{a} * {b} = {result}"

@math_mcp.tool
def divide(a: float, b: float) -> str:
    """ Divide two numbers.
    
    Args:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        str: The quotient of the two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    return f"{a} / {b} = {result}"

@math_mcp.tool
def power(a: float, b: float) -> str:
    """ Raise a number to a power.
    
    Args:
        a (float): The base number.
        b (float): The exponent.
    
    Returns:
        str: The result of raising the base to the exponent.
    """
    result = a ** b
    return f"{a} ^ {b} = {result}"

@math_mcp.tool
def sqrt(a: float) -> str:
    """ Calculate the square root of a number.
    
    Args:
        a (float): The number to calculate the square root of.
    
    Returns:
        str: The square root of the number.
    """
    result = a ** 0.5
    return f"math.sqrt({a}) = {result}"

@math_mcp.resource("resource://pi")
def get_pi() -> str:
    """Get the value of pi (π)."""
    return f"π = {MATH_CONSTANTS['pi']}"

@math_mcp.resource("resource://e")
def get_e() -> str:
    """Get the value of e (Euler's number)."""
    return f"e = {MATH_CONSTANTS['e']}"

@math_mcp.resource("resource://phi")
def get_phi() -> str:
    """Get the value of phi (Golden Ratio)."""
    return f"φ = {MATH_CONSTANTS['phi']}"

@math_mcp.resource("resource://golden_ratio")
def get_golden_ratio() -> str:
    """Get the value of the golden ratio."""
    return f"Golden Ratio = {MATH_CONSTANTS['golden_ratio']}"

@math_mcp.resource("resource://factorial/{index}")
def get_factorial(index: int) -> str:
    """Get the factorial of a number."""
    if index < 0:
        raise ValueError("Index must be non-negative")
    
    def factorial(n: int, memo: dict[int, int] = {}) -> int:
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        memo[n] = n * factorial(n - 1)
        return memo[n]
    
    return f"Factorial at index {index} = {factorial(index)}"

@math_mcp.resource("resource://fibonacci/{index}")
def get_fibonacci(index: int) -> str:
    """Get the fibonacci sequence at a given index."""
    if index < 0:
        raise ValueError("Index must be non-negative")
    
    # get fibonacci sequence at index
    def fibonacci(n: int, memo: dict[int, int] = {}) -> int:
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]
    
    return f"Fibonacci at index {index} = {fibonacci(index)}"

@math_mcp.resource("resource://primes/{index}")
def get_primes(index: int) -> str:
    """Get the prime sequence at a given index."""
    if index < 0:
        raise ValueError("Index must be non-negative")
    
    # get prime sequence at index
    def prime(n: int, memo: dict[int, int] = {}) -> int:
        if n in memo:
            return memo[n]
        if n == 0:
            return 2
        if n == 1:
            return 3
        memo[n] = prime(n - 1) + prime(n - 2)
        return memo[n]
    
    return f"Prime at index {index} = {prime(index)}"


@math_mcp.prompt

def solve_equation_prompt() -> str:
    return "Solve the equation"

@math_mcp.prompt
def calculation_help_prompt() -> str:
    return "Help me with this calculation"

if __name__ == "__main__":
    math_mcp.run(transport="stdio")
