# Xapien Preprocessor Task

This Python package was developed as part of a technical task for **Xapien**. It provides utilities for preprocessing Markdown documents, including cleaning links, filtering overly long documents, and batching them intelligently for downstream use.

---

## ✨ Features

- 🔗 **Cleans and anonymizes external URLs**  
  Converts `[text](url)` and raw `http(s)` links to `[text](...)` or `...`

- 🧮 **Estimates token count**  
  Uses a word-count heuristic: 1 word ≈ 1 token

- 🧹 **Filters excessively long documents**  
  Removes documents over 100,000 tokens

- 📦 **Batches documents**  
  Uses a greedy bin-packing algorithm to group docs into batches within token and size limits

---


## 📁 Project Structure

xapien_task/
├── src/
│ ├── init.py # Package initializer
│ ├── cleaner.py # Cleans and anonymizes URLs in markdown
│ ├── filter.py # Token estimation and length filtering
│ └── batcher.py # Batching with greedy bin-packing
│
├── tests/
│ ├── test_cleaner.py # Unit tests for cleaner
│ ├── test_filter.py # Unit tests for filter
│ └── test_batcher.py # Unit tests for batcher
│
├── README.md # Project documentation
├── requirements.txt # Dependency list (if needed)
└── pyproject.toml # Package metadata and config

---

## 🚀 Installation & Usage

Clone the repo:

```bash
git clone https://github.com/esemsc-fwd24/xapien_task.git
cd xapien_task


Install pytest for running tests:
```bash
pip install pytest
```

Example usage:
```python
from src.cleaner import clean_markdown
from src.filter import estimate_tokens, filter_documents
from src.batcher import batch_documents

text = "Visit [Xapien](https://xapien.com) and https://example.com"
cleaned = clean_markdown(text)

tokens = estimate_tokens(cleaned)

docs = [cleaned, "word " * 99_000, "word " * 101_000]
filtered = filter_documents(docs)

batches = batch_documents(filtered)
```

Running tests:
```bash
pytest tests/
```


## Assumptions
- One word ≈ one token (for fast filtering without external NLP libraries)
- Token/document constraints    
    - Max 100,000 tokens per document
    - Max 10 documents or 100,000 tokens per batch
- Markdown cleaning uses regular expressions for [text](url) and raw http(s) links