from typing import Literal
from fastmcp import FastMCP
from pydantic import BaseModel, Field
from core.utils import load_prompt
from fastmcp.prompts.prompt import Message, PromptMessage, TextContent
from livefront_mcp.mcp_instance import mcp


import livefront_mcp.code_review


@mcp.tool
def hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    print(f"Adding {a} and {b}")
    return a + b


if __name__ == "__main__":
    mcp.run(transport="stdio")
