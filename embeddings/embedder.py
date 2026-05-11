from sentence_transformers import SentenceTransformer

from config.settings import settings


def load_embedding_model():

    model = SentenceTransformer(
        settings.EMBEDDING_MODEL
    )

    return model