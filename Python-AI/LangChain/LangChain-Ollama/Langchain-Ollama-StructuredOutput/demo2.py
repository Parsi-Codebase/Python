from pydantic import BaseModel
from langchain_ollama import ChatOllama
class TopicExplanation(BaseModel):
    topic:str
    difficulty:str
    summary:str
    key_points:list[str]
model=ChatOllama(
    model='phi3',
    temperature=0.3
)
structured_model=model.with_structured_output(
    TopicExplanation
)
result=structured_model.invoke(
    'Explain the fast api for the beginners in 50 words'
)
print(type(result)) # return the type
print('\n')
print(result)

# access the individual fields
print(result.topic)
print(result.difficulty)
print(result.summary)
print(result.key_points)