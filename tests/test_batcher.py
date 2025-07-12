
from src.batcher import batch_documents
from src.filter import estimate_tokens

def test_empty_input():
    assert batch_documents([]) == []

def test_single_small_document():
    docs = ["short document"]
    batches = batch_documents(docs)
    assert len(batches) == 1
    assert batches[0] == docs

def test_exact_batch_size_limit():
    docs = ["word"] * 10  # 10 documents, each 1 token
    batches = batch_documents(docs, max_batch_size=10)
    assert len(batches) == 1
    assert batches[0] == docs

def test_exceeds_batch_size_limit():
    docs = ["word"] * 11
    batches = batch_documents(docs, max_batch_size=10)
    assert len(batches) == 2
    assert sum(len(batch) for batch in batches) == 11

def test_token_limit_enforced():
    # Each doc is 50,000 tokens, so only two can fit across two batches
    docs = ["word " * 50_000] * 3  # 3 documents, each with 50k tokens
    batches = batch_documents(docs)
    for batch in batches:
        total_tokens = sum(estimate_tokens(doc) for doc in batch)
        assert total_tokens <= 100_000
    assert len(batches) == 2  # First batch gets two, second gets one

def test_all_documents_accounted_for():
    docs = [f"doc {i}" for i in range(25)]
    batches = batch_documents(docs)
    flattened = [doc for batch in batches for doc in batch]
    assert sorted(flattened) == sorted(docs)
