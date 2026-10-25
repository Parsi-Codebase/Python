# Prompt + Structured Output
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


class TopicExplanation(BaseModel):

    topic: str
    difficulty: str
    summary: str
    key_points: list[str]


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an experienced programming instructor.
        Explain programming topics clearly.
        """
    ),
    (
        "human",
        """
        Explain the following topic:

        Topic: {topic}

        Experience level: {level}
        """
    )
])


model = ChatOllama(
    model="phi3",
    temperature=0.3
)


structured_model = model.with_structured_output(
    TopicExplanation
)


messages = prompt.invoke({
    "topic": "Python decorators",
    "level": "beginner"
})


result = structured_model.invoke(messages)

print(result)