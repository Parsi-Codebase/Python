from langchain_ollama import ChatOllama
model=ChatOllama(
    model='phi3'
)
def ask_ai(prompt:str):
    response=model.invoke(prompt)
    return response.content

response=ask_ai('What is AI')
print(response)