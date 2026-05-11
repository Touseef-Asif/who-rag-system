from embeddings.embedder import load_embedding_model

from retrieval.retriever import search_qdrant

from llm.groq_client import load_llm

from prompts.rag_prompt import RAG_PROMPT

from config.settings import settings


# =========================
# LOAD MODELS
# =========================

embedding_model = load_embedding_model()

llm = load_llm()


def ask_rag(question: str):

    # =========================
    # QUERY EMBEDDING
    # =========================

    query_embedding = embedding_model.encode(
        question
    )

    # =========================
    # RETRIEVE DOCUMENTS
    # =========================

    results = search_qdrant(
        query_embedding=query_embedding,
        top_k=settings.TOP_K
    )

    # =========================
    # BUILD CONTEXT
    # =========================

    context = "\n\n".join([
        result.payload["text"]
        for result in results
    ])

    # =========================
    # CREATE PROMPT
    # =========================

    final_prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    # =========================
    # GENERATE RESPONSE
    # =========================

    response = llm.invoke(
        final_prompt
    )

    return response.content