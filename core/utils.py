from pathlib import Path


def load_prompt(path: str, merge_with: str | None = None) -> str:
    base = Path(__file__).resolve().parents[1]
    text = (base / path).read_text(encoding="utf-8")
    if merge_with:
        shared = (base / merge_with).read_text(encoding="utf-8")
        return f"{shared}\n\n{text}"
    return text
