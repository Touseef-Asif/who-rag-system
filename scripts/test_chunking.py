from loaders.pdf_loader import load_pdf

from preprocess.text_cleaner import clean_documents

from chunking.text_splitter import split_documents

from config.settings import settings


docs = load_pdf(settings.PDF_PATH)

cleaned_docs = clean_documents(docs)

chunks = split_documents(cleaned_docs)

print(f"\nTotal Chunks: {len(chunks)}\n")

print(chunks[0].page_content)

print("\nMetadata:\n")

print(chunks[0].metadata)