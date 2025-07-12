from src.filter import estimate_tokens, filter_documents

def test_emty_string():
    assert estimate_tokens("") == 0

def test_whitespace_string():
    assert estimate_tokens("   ") == 0
    assert estimate_tokens(" \t     \n ") == 0

def test_single_word():
    assert estimate_tokens("Hello") == 1

def test_multiple_words():
    assert estimate_tokens("Hello world this is a test") == 6

def test_multiple_spaces_between_words():
    assert estimate_tokens("Hello     world") == 2

def test_tabs_and_newlines():
    assert estimate_tokens("Hello\tworld\nnew line") == 4

def test_mixed_whitespace_and_punctuation():
    text = "Hello, world!\nThis\tis a test."
    # Tokens are: Hello,, world!, This, is, a, test.
    assert estimate_tokens(text) == 6

def test_unicode_characters():
    text = "こんにちは 世界 🌏🚀"  # Japanese for hello world + emojis
    assert estimate_tokens(text) == 3

def test_long_input_exact_limit():
    text = "word " * 100_000
    assert estimate_tokens(text.strip()) == 100_000

def test_just_over_limit():
    text = "word " * 100_001
    assert estimate_tokens(text.strip()) == 100_001

def test_with_leading_and_trailing_whitespace():
    text = "   leading and trailing whitespace   "
    assert estimate_tokens(text) == 4

def test_special_characters():
    text = "!@#$%^&*()_+-=[]{}|;':,.<>/?"
    # Treated as one token since no spaces
    assert estimate_tokens(text) == 1

def test_empty_document_list():
    assert filter_documents([]) == []


def test_all_documents_under_limit():
    docs = ["short one", "tiny doc", "a word"]  # all very short
    assert filter_documents(docs) == docs  # nothing filtered

def test_all_documents_over_limit():
    docs = ["word " * 100_001, "another " * 200_000]
    assert filter_documents([doc.strip() for doc in docs]) == []

def test_mixed_document_lengths():
    docs = [
        "word " * 99_000,
        "word " * 100_000,
        "word " * 100_001
    ]
    docs = [doc.strip() for doc in docs]
    expected = [docs[0], docs[1]]
    assert filter_documents(docs) == expected

def test_document_exactly_on_token_limit():
    doc = "word " * 100_000
    assert filter_documents([doc.strip()]) == [doc.strip()]

def test_documents_with_whitespace_only():
    docs = ["     ", "\t\t", "\n\n"]
    assert filter_documents(docs) == docs  # estimate = 0 tokens → keep

def test_documents_with_leading_and_trailing_spaces():
    docs = ["  short doc  ", "     lots of space     "]
    assert filter_documents(docs) == docs