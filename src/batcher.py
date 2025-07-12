from src.filter import estimate_tokens


def batch_documents(
    documents: list[str], max_batch_size: int = 10, max_tokens: int = 100_000
) -> list[list[str]]:
    """
    Batches documents using a greedy bin-packing algorithm, keeping
    each batch within token and size limits.

    Args:
        documents (list[str]): List of document texts to batch.
        max_batch_size (int): Maximum number of documents per batch.
        max_tokens (int): Maximum allowed tokens per batch.

    Returns:
        list[list[str]]: List of batches, where each batch is a list
        of document strings.
    """
    tokenized_docs = [(doc, estimate_tokens(doc)) for doc in documents]
    sorted_docs = sorted(tokenized_docs, key=lambda x: x[1], reverse=True)

    batches = []

    for doc, tokens in sorted_docs:
        placed = False
        for batch in batches:
            batch_docs, batch_tokens = batch
            if (
                len(batch_docs) < max_batch_size
                and (batch_tokens + tokens) <= max_tokens
            ):
                batch_docs.append(doc)
                batch[1] += tokens  # Mutate token count directly in the list
                placed = True
                break

        if not placed:
            batches.append([[doc], tokens])

    return [batch_docs for batch_docs, _ in batches]
