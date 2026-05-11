from config.settings import settings

from vectordb.qdrant_client import get_qdrant_client


def search_qdrant(
    query_embedding,
    top_k=5
):

    client = get_qdrant_client()

    results = client.query_points(

        collection_name=settings.COLLECTION_NAME,

        query=query_embedding.tolist(),

        limit=top_k
    )

    return results.points