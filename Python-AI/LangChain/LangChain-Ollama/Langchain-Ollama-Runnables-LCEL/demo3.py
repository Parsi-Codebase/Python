# RunnableLambda is use to your own function inside a LangChain pipeline
from langchain_core.runnables import RunnableLambda
def uppercase(text:str)->str:
    return text.upper()
runnable=RunnableLambda(uppercase)
result=runnable.invoke('hello langchain')
print(result)