from langchain_ollama import ChatOllama
model=ChatOllama(
    model='phi3'
)
response=model.invoke(
    'Explain AI in simple terms'
)
print(response.content)