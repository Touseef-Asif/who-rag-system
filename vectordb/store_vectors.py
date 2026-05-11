from qdrant_client.models import PointStruct

from config.settings import settings

from vectordb.qdrant_client import get_qdrant_client


def store_vectors(
    chunks,
    embeddings
):

    client = get_qdrant_client()

    points = []

    for idx, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):

        point = PointStruct(

            id=idx,

            vector=embedding.tolist(),

            payload={

                "text": chunk.page_content,

                "source": chunk.metadata.get("source"),

                "page": chunk.metadata.get("page"),

                "title": chunk.metadata.get("title"),

                "total_pages": chunk.metadata.get("total_pages")
            }
        )

        points.append(point)

    client.upsert(
        collection_name=settings.COLLECTION_NAME,
        points=points
    )

    print(f"\nStored {len(points)} vectors in Qdrant")