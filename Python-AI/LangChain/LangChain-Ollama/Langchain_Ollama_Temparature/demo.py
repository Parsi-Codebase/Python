from langchain_ollama import ChatOllama


creative_model = ChatOllama(
    model="phi3",
    temperature=0.8
)

controlled_model = ChatOllama(
    model="phi3",
    temperature=0
)


question = "Give me three ideas for an AI application."


print("CONTROLLED RESPONSE")
print("-------------------")

response = controlled_model.invoke(question)

print(response.content)


print("\nCREATIVE RESPONSE")
print("------------------")

response = creative_model.invoke(question)

print(response.content)