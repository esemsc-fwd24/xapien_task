from src.cleaner import clean_markdown
from src.filter import filter_documents
from src.batcher import batch_documents

def run_pipeline(documents: list[str]) -> list[list[str]]:
    cleaned = [clean_markdown(doc) for doc in documents]
    filtered = filter_documents(cleaned)
    return batch_documents(filtered)
