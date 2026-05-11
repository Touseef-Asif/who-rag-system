from qdrant_client.models import Distance
from qdrant_client.models import VectorParams

from config.settings import settings

from vectordb.qdrant_client import get_qdrant_client


def create_collection():

    client = get_qdrant_client()

    client.recreate_collection(
        collection_name=settings.COLLECTION_NAME,

        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    print(f"\nCollection Created: {settings.COLLECTION_NAME}")