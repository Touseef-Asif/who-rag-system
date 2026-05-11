import re

from langchain_core.documents import Document


def clean_text(text: str) -> str:

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove repeated dots
    text = re.sub(r"\.{2,}", ".", text)

    # Strip spaces
    text = text.strip()

    return text


def clean_documents(documents):

    cleaned_docs = []

    for doc in documents:

        cleaned_text = clean_text(doc.page_content)

        cleaned_doc = Document(
            page_content=cleaned_text,
            metadata=doc.metadata
        )

        cleaned_docs.append(cleaned_doc)

    return cleaned_docs