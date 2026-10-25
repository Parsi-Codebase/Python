from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_ollama import ChatOllama
prompt=ChatPromptTemplate.from_template(
    'Give a one-line definition of {topic}'
)
model=ChatOllama(
    model='phi3',
    temperature=0.3
)
parser=StrOutputParser()
def add_prefix(text:str)->str:
    return 'AI Explanation: '+text
prefix_runnable=RunnableLambda(add_prefix)
chain=(
    prompt | model | parser | prefix_runnable
)
result=chain.invoke({
    'topic':'Dependency Injection'
})
print(result)