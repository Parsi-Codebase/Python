from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
class TopicExplanation(BaseModel):
    topic:str
    difficulty:str
    summary:str
    key_points:list[str]
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an experienced programming instructor."
    ),
    (
        "human",
        """
        Explain {topic} for a {level} developer.
        """
    )
])
model=ChatOllama(
    model='phi3',
    temperature=0.3
)
structured_model=model.with_structured_output(
    TopicExplanation
)
chain=prompt | structured_model
result=chain.invoke({
    'topic':'FastAPI',
    'level':'beginner'
})
print(result)