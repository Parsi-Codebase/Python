from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
prompt=ChatPromptTemplate.from_template(
    'Explain {topic} in sample terms'
)
model=ChatOllama(
    model='phi3',
    temperature=0.3
)
parser=StrOutputParser() # The parser converts the AIMessage into normal python string
chain=prompt | model | parser
result=chain.invoke({
    'topic':'Python decorators'
})
print(result)