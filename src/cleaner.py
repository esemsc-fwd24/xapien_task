import re

def clean_markdown(text: str) -> str:
    """
    Cleans the input markdown by stripping out all URLs, replacing each URL with "..." whilst retaning the link text.
    
    Args:
        text (str): The input markdown text containing URLs.
    
    Returns:
        str: The cleaned markdown text with URLs replaced by "...".
    """
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'[\1](...)', text)
    text = re.sub(r'http[s]?://\S+','...',text)
    return text