from langchain_ollama import ChatOllama


model = ChatOllama(
    model="phi3",
    temperature=0.1
)
for chunk in model.stream(
    "Explain AI in detail"
):
    print(chunk.content,end='',flush=True)
