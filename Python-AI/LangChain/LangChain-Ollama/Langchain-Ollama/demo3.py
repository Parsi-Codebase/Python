from langchain_ollama import ChatOllama


model = ChatOllama(
    model="phi3"
)


def ask_ai(question: str) -> str:

    response = model.invoke(question)

    return response.content


print("Python AI Assistant")
print("--------------------")

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        break

    answer = ask_ai(question)

    print("\nAI:", answer)