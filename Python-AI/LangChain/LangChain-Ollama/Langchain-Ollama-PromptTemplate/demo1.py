from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_template(
     """
    Explain {topic} to a {level} developer.

    Use simple language.
    Include a practical example.
    """
)
model=ChatOllama(
    model='phi3',
    temperature=0.3
)
messages=prompt.invoke({
    "topic":'What is LLM',
    "level":'beginner'
})
response=model.invoke(messages)
print(response.content)