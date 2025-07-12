from src.cleaner import clean_markdown


def test_clean_markdown_links_and_urls():
    input_text = (
        "Visit [Xapien](https://xapien.com) and check https://example.com for info.\n"
        "Also, [Docs](http://docs.example.com) are useful."
    )

    expected_output = (
        "Visit [Xapien](...) and check ... for info.\n"
        "Also, [Docs](...) are useful."
    )

    assert clean_markdown(input_text) == expected_output