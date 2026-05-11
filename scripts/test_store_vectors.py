from loaders.pdf_loader import load_pdf

from preprocess.text_cleaner import clean_documents

from chunking.text_splitter import split_documents

from embeddings.embedder import load_embedding_model

from vectordb.create_collection import create_collection

from vectordb.store_vectors import store_vectors

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
# CREATE COLLECTION
# =========================

create_collection()


# =========================
# STORE VECTORS
# =========================

store_vectors(
    chunks,
    embeddings
)