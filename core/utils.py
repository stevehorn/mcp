from pathlib import Path


def load_prompt(path: str, merge_with: list[str] | None = None) -> str:
    base = Path(__file__).resolve().parents[1]
    text = (base / path).read_text(encoding="utf-8")
    if merge_with:
        merged_texts = []
        for merge_path in merge_with:
            merged_texts.append((base / merge_path).read_text(encoding="utf-8"))
        merged = "\n\n".join(merged_texts)
        return f"{merged}\n\n{text}"
    return text
