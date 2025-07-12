from src.cleaner import clean_markdown


def test_clean_markdown_links_and_urls():
    input_text = (
        "Visit [Xapien](https://xapien.com) and check https://example.com \n"
        "for info.\n"
        "Also, [Docs](http://docs.example.com) are useful."
    )
    expected_output = (
        "Visit [Xapien](...) and check ... \n"
        "for info.\n"
        "Also, [Docs](...) are useful."
    )
    assert clean_markdown(input_text) == expected_output


def test_multiple_links_on_same_line():
    text = "See [one](http://a.com) and [two](https://b.com)"
    expected = "See [one](...) and [two](...)"
    assert clean_markdown(text) == expected


def test_non_http_links_ignored():
    text = "Contact [me](mailto:test@example.com)"
    expected = "Contact [me](mailto:test@example.com)"  # Should not change
    assert clean_markdown(text) == expected


def test_link_text_with_unicode():
    text = "Visit [Xapien 💼](https://xapien.com)"
    expected = "Visit [Xapien 💼](...)"
    assert clean_markdown(text) == expected


def test_already_cleaned_link():
    text = "Already cleaned: [Text](...)"
    expected = "Already cleaned: [Text](...)"
    assert clean_markdown(text) == expected


def test_empty_input():
    assert clean_markdown("") == ""


def test_no_links_or_urls():
    text = "This text has no links."
    assert clean_markdown(text) == text


def test_trailing_punctuation_after_url():
    text = "See this: https://example.com."
    expected = "See this: ...."
    assert clean_markdown(text) == expected


def test_naked_link_with_query_parameters():
    text = "Go to https://x.com?q=test&sort=asc"
    expected = "Go to ..."
    assert clean_markdown(text) == expected


def test_mix_of_raw_and_markdown_links():
    text = "Check [Docs](https://docs.com) or go to https://site.com directly."
    expected = "Check [Docs](...) or go to ... directly."
    assert clean_markdown(text) == expected


def test_link_with_trailing_space_before_closing_paren():
    text = "Here is a [link](http://example.com )"
    expected = "Here is a [link](...)"
    assert clean_markdown(text) == expected
