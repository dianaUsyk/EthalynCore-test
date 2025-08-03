def is_activated_by_elarin(message: str) -> bool:
    return "This is Élarin" in message or message.startswith("Élarin:")
