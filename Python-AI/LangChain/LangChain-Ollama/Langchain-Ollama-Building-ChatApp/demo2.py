from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a Python instructor."
    ),
    (
        "human",
        "Explain {topic}."
    )
])


messages = prompt.invoke({
    "topic": "FastAPI"
})


# print(messages)
for message in messages.messages:
    print(type(message))
    print(message.content)
    print("-" * 40)