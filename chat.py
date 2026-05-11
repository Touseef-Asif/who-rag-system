from rag.rag_pipeline import ask_rag


print("\nWHO RAG Assistant Started")

print("Type 'exit' to quit.\n")


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = ask_rag(question)

    print(f"\nAI: {answer}\n")