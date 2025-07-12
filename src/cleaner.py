import re

def clean_markdown(text: str) -> str:
    """
    Removes URLs from markdown text.
    - Replaces [text](http...) with [text](...)
    - Replaces raw http(s) URLs with '...', preserving punctuation
    """
    # Replace markdown links [text](http...) → [text](...)
    text = re.sub(r'\[([^\]]+)\]\((http[s]?://[^\)]+)\)', r'[\1](...)', text)

    # Replace raw URLs outside of markdown with ..., preserving end punctuation
    text = re.sub(r'(?<!\()http[s]?://\S+?([.,!?])?(?=\s|$)', r'...\1', text)

    return text