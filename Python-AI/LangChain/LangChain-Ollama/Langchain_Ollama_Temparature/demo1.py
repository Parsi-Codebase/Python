from langchain_ollama import ChatOllama


model = ChatOllama(
    model="phi3",
    temperature=0.3
)


def ask_ai(question: str) -> str:

    response = model.invoke(question)

    return response.content


questions = [
    "What is Python?",
    "What is FastAPI?",
    "What is LangChain?"
]


for question in questions:

    print("\nQUESTION:")
    print(question)

    print("\nANSWER:")

    answer = ask_ai(question)

    print(answer)