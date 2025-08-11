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
    name="generate_review_request",
    description="Call this to fetch a language specific code review prompt. Always provide the language if known.",
)
def generate_review_request(params: CodeReviewParams) -> CodeReviewResponse:
    """
    Review Code for a given language.
    """
    prompt = load_prompt(
        f"prompts/code_review/{params.language}.md",
        merge_with="prompts/code_review/shared.md",
    )

    return PromptMessage(role="user", content=TextContent(type="text", text=prompt))
