from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
prompt=ChatPromptTemplate.from_template(
    'Explain {topic} in simple terms'
)
model=ChatOllama(
    model='phi3',
    temperature=0.3
)
#Runnable
chain=prompt|model
resuult=chain.invoke({
    'topic':'FastAPI'
})
print(resuult.content)