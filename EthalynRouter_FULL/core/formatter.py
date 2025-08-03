def stylize_response(text: str, style: str) -> str:
    if style == "poetic":
        return "\n".join([f"✨ {line}" for line in text.split("\n")])
    return text
