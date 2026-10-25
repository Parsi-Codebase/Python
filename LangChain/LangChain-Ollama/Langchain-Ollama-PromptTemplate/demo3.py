from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an experienced programming instructor.

        Explain concepts clearly.
        Use practical examples.
        """
    ),
    (
        "human",
        """
        Explain {topic}.

        Programming language: {language}
        Experience level: {level}

        Include:
        1. Definition
        2. Explanation
        3. Code example
        4. Real-world use case
        """
    )
])


model = ChatOllama(
    model="phi3",
    temperature=0.3
)


messages = prompt.invoke({
    "topic": "Dependency Injection",
    "language": "Python",
    "level": "beginner"
})


response = model.invoke(messages)

print(response.content)