from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


model = ChatOllama(
    model="phi3",
    temperature=0.3
)


explain_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a beginner in 50 words"
)


quiz_prompt = ChatPromptTemplate.from_template(
    "Create 5 MCQs about {topic}."
)


topic = "Python decorators"


messages = explain_prompt.invoke({
    "topic": topic
})

response = model.invoke(messages)

print("EXPLANATION")
print(response.content)


messages = quiz_prompt.invoke({
    "topic": topic
})

response = model.invoke(messages)

print("\nQUIZ")
print(response.content)