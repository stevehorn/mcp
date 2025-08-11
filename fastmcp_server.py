from fastmcp import FastMCP

mcp = FastMCP(name="My FastMCP Server")


@mcp.tool
def hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    print(f"Adding {a} and {b}")
    return a + b


@mcp.tool
def get_code_review_prompt(language: str) -> str:
    """
    Review Code for a given language.

    Supported languages:
    - typescript
    - csharp
    - markdown
    """
    print(f"Generating code review prompt for language: {language}")
    if language.lower() == "typescript":
        prompt = "Make sure that the codebase exemplifies SOLID principles. Strictly forbid commented or dead code."
    elif language.lower() == "csharp":
        prompt = "Please review the following C# code for best practices, readability, and potential improvements."
    elif language.lower() == "markdown":
        prompt = "Disallow sentences that do not use the oxford comma."
    return prompt


if __name__ == "__main__":
    mcp.run(transport="stdio")
