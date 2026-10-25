from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
model=ChatOllama(
    model='phi3'
)
prompt=ChatPromptTemplate.from_template(
     """
    You are a Python instructor.

    Explain the following topic:
    {topic}

    Target audience:
    {audience}
    """
)
messages=prompt.invoke({
    "topic":'What is LLM',
    "audience":'beginner python developers'
})
response=model.invoke(messages)
print(response.content)