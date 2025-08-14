from typing import Literal
from pydantic import BaseModel, Field
from fastmcp.prompts.prompt import PromptMessage, TextContent
from core.utils import load_prompt
from livefront_mcp.mcp_instance import mcp


class CodeReviewParams(BaseModel):
    language: Literal["typescript", "csharp", "markdown"] = Field(
        description="The programming language for which to retrieve the code review prompt."
    )


class CodeReviewResponse(BaseModel):
    prompt: str = Field(
        description="The complete code review prompt text for the given language."
    )


@mcp.prompt(
    name="diff_code_review_csharp",
    description="Call this to fetch the C# code review prompt for a diff between main and the current branch.",
)
def code_review_csharp() -> CodeReviewResponse:
    """
    Fetches the C# code review prompt specifically for reviewing diffs between the main branch and the current branch.
    """
    prompt = load_prompt(
        "prompts/code_review/csharp/diff_review.md",
        merge_with=[
            "prompts/code_review/csharp/csharp.md",
            "prompts/code_review/shared/shared.md",
        ],
    )

    return PromptMessage(role="user", content=TextContent(type="text", text=prompt))


@mcp.prompt(
    name="code_review_csharp",
    description="Call this to fetch the C# code review prompt.",
)
def code_review_csharp() -> CodeReviewResponse:
    """
    Convenience wrapper to fetch the C# code review prompt.
    """
    prompt = load_prompt(
        f"prompts/code_review/csharp/csharp.md",
        merge_with=["prompts/code_review/shared/shared.md"],
    )

    return PromptMessage(role="user", content=TextContent(type="text", text=prompt))


@mcp.prompt(
    name="code_review",
    description="Call this to fetch a language specific code review prompt. Always provide the language if known.",
)
def code_review(params: CodeReviewParams) -> CodeReviewResponse:
    """
    Review Code for a given language.
    """
    prompt = load_prompt(
        f"prompts/code_review/{params.language}/{params.language}.md",
        merge_with=["prompts/code_review/shared/shared.md"],
    )

    return PromptMessage(role="user", content=TextContent(type="text", text=prompt))
