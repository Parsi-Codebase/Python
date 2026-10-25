from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an experienced Python instructor."
    ),
    (
        "human",
        "Explain {topic} for a {level} developer."
    )
])


model = ChatOllama(
    model="phi3",
    temperature=0.3
)


messages = prompt.invoke({
    "topic": "FastAPI Dependency Injection",
    "level": "beginner"
})


response = model.invoke(messages)

print(response.content)