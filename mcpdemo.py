from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def mystery_function(a: int, b: int) -> int:
    """Get a mysterious result"""
    return a * a - 2 * b

if __name__ == "__main__":
    mcp.run()