from loaders.pdf_loader import load_pdf

from preprocess.text_cleaner import clean_documents

from chunking.text_splitter import split_documents

from embeddings.embedder import load_embedding_model

from config.settings import settings


# =========================
# LOAD PDF
# =========================

docs = load_pdf(settings.PDF_PATH)


# =========================
# CLEAN DOCUMENTS
# =========================

cleaned_docs = clean_documents(docs)


# =========================
# SPLIT INTO CHUNKS
# =========================

chunks = split_documents(cleaned_docs)


# =========================
# EXTRACT CHUNK TEXTS
# =========================

chunk_texts = [
    chunk.page_content
    for chunk in chunks
]


# =========================
# EXTRACT METADATA
# =========================

chunk_metadata = [
    chunk.metadata
    for chunk in chunks
]


# =========================
# LOAD EMBEDDING MODEL
# =========================

embedding_model = load_embedding_model()


# =========================
# CREATE EMBEDDINGS
# =========================

embeddings = embedding_model.encode(
    chunk_texts,
    show_progress_bar=True
)


# =========================
# RESULTS
# =========================

print(f"\nTotal Chunks: {len(chunk_texts)}")

print(f"\nTotal Embeddings: {len(embeddings)}")

print(f"\nEmbedding Dimension: {len(embeddings[0])}")


print("\nFirst Chunk:\n")

print(chunk_texts[0][:500])


print("\nFirst Metadata:\n")

print(chunk_metadata[0])


print("\nFirst Embedding First 10 Values:\n")

print(embeddings[0][:10])