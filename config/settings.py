from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    # =========================
    # QDRANT
    # =========================

    QDRANT_URL = os.getenv("QDRANT_URL")

    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

    COLLECTION_NAME = os.getenv("COLLECTION_NAME")

    # =========================
    # EMBEDDINGS
    # =========================

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    # =========================
    # GROQ
    # =========================

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    GROQ_MODEL = os.getenv("GROQ_MODEL")

    # =========================
    # DATA
    # =========================

    PDF_PATH = os.getenv("PDF_PATH")

    # =========================
    # CHUNKING
    # =========================

    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))

    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))

    # =========================
    # RETRIEVAL
    # =========================

    TOP_K = int(os.getenv("TOP_K"))


settings = Settings()