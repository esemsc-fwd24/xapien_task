

def estimate_tokens(text: str) -> int:
    """
    Estimate the number of tokens in a string, here assuming 1 token per word.
    
    Args:
        test (str): The input string to estimate tokens for.
            
    Returns:
        int: Estimated number of tokens.
    """
    return len(text.split())


def filter_documents(docs: list[str], max_tokens: int = 100_000) -> list[str]:
    """
    Filter out documents that exceed the max token limit. 

    Args: 
        docs (list[str]): List of document texts to filter.
        max_tokens (int): Maximum allowed tokens per document.
        
    Returns:
        list[str]: Filtered list of documents that do not exceed the max token limit.
    """ 

    return [doc for doc in docs if estimate_tokens(doc) <= max_tokens]