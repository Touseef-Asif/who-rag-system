from embeddings.embedder import load_embedding_model

from retrieval.retriever import search_qdrant

from config.settings import settings


# =========================
# LOAD EMBEDDING MODEL
# =========================

embedding_model = load_embedding_model()


# =========================
# USER QUERY
# =========================

query = "What substances are under surveillance?"


# =========================
# QUERY EMBEDDING
# =========================

query_embedding = embedding_model.encode(
    query
)


# =========================
# SEARCH QDRANT
# =========================

results = search_qdrant(
    query_embedding=query_embedding,
    top_k=settings.TOP_K
)


# =========================
# SHOW RESULTS
# =========================

print(f"\nQuery: {query}\n")


for idx, result in enumerate(results):

    print("=" * 80)

    print(f"\nResult {idx + 1}")

    print(f"\nScore: {result.score}")

    print(f"\nPage: {result.payload.get('page')}")

    print(f"\nText:\n")

    print(result.payload.get("text")[:1000])

    print("\n")