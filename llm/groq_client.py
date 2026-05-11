from langchain_groq import ChatGroq

from config.settings import settings


def load_llm():

    llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=settings.GROQ_MODEL,
        temperature=0
    )

    return llm