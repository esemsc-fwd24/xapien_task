

def estimate_tokens(text: str) -> int:
    """
    Estimate the number of tokens in a string, here assuming 1 token per word.
    
    Args:
        test (str): The input string to estimate tokens for.
            
    Returns:
        int: Estimated number of tokens.
    """
    return len(text.split())

