from .bot_replies import replies

def get_reply(key: str, kwargs: dict = None) -> str:
    """
    Safely fetch a reply and replace placeholders and return as reply
    
    Example usage:
        get_reply("welcome", {"username": "Alice", "chatname": "FunGroup"})
    """
    template = replies.get(key, "")
    if not template:
        return ""  # or return default message

    result = template
    if kwargs:
        for placeholder, value in kwargs.items():
            # Replace safely, even if placeholder is missing
            result = result.replace(f"{{{placeholder}}}", str(value))
    return result