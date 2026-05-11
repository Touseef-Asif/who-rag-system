from llm.groq_client import load_llm


llm = load_llm()

response = llm.invoke("What is WHO?")

print(response.content)