from src.filter import estimate_tokens

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