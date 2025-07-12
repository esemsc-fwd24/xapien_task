from src.pipeline import run_pipeline
from src.filter import estimate_tokens

def test_pipeline_removes_oversized_docs_and_batches_correctly():
    docs = [
        "Visit [Site](https://site.com) and http://link.com",      # should be cleaned + kept
        "word " * 101_000,                                          # oversized, should be dropped
        "word " * 50_000 + " Visit https://x.com",                 # cleaned, within limit
    ]
    
    batches = run_pipeline(docs)

    # Check constraints
    for batch in batches:
        assert len(batch) <= 10
        assert sum(estimate_tokens(doc) for doc in batch) <= 100_000
        for doc in batch:
            assert "http" not in doc
            assert "(...)" in doc or "..." in doc

    # One document should be filtered out (over limit)
    flattened = [doc for batch in batches for doc in batch]
    assert len(flattened) == 2




def test_pipeline_all_docs_under_limit_in_one_batch():
    docs = [
        "This is a [link](http://test.com)",             # markdown link
        "Just a simple doc",                              # no URL
        "Another one here with https://url.com"          # raw link
    ]

    batches = run_pipeline(docs)
    all_processed_docs = batches[0]
    
    # Sort original docs by token count (to match greedy bin-packing order)
    sorted_docs = sorted(docs, key=estimate_tokens, reverse=True)

    for original_doc, processed_doc in zip(sorted_docs, all_processed_docs):
        if "http" in original_doc:
            assert "http" not in processed_doc
            assert "(...)" in processed_doc or "..." in processed_doc
        else:
            assert processed_doc == original_doc




def test_pipeline_empty_input():
    assert run_pipeline([]) == []
