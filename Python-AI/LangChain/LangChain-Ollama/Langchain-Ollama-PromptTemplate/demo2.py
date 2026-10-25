from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_messages([
    ('system','You are an experienced Python instructor'),
    ('human','Explain {topic} to a {level} developer')
    
])
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