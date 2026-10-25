from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert programming instructor.

        Explain concepts clearly and practically.
        """
    ),
    (
        "human",
        """
        Explain {topic}.

        Language: {language}
        Level: {level}

        Include a code example.
        """
    )
])


model = ChatOllama(
    model="phi3",
    temperature=0.3
)


def explain_topic(
    topic: str,
    language: str,
    level: str
):

    messages = prompt.invoke({
        "topic": topic,
        "language": language,
        "level": level
    })

    response = model.invoke(messages)

    return response.content


answer = explain_topic(
    topic="Decorators",
    language="Python",
    level="beginner"
)

print(answer)