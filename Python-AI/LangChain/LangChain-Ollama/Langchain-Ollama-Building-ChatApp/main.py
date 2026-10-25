from langchain_ollama import ChatOllama
from langchain_core.messages import (SystemMessage,HumanMessage,AIMessage)
model=ChatOllama(
    model='phi3',
    temperature=0.3
)

messages=[
    SystemMessage(
        content='You are a helpful python instructor'
    )
]
while True:
    user_input=input('\n You:')
    if user_input.lower()=='exit':
        break
    messages.append(HumanMessage(content=user_input))
    response=model.invoke(messages)
    messages.append(response)
# print(type(response))
    print('\nAI:',response.content)