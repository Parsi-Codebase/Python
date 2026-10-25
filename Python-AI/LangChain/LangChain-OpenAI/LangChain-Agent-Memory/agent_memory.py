from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
@tool
def calculate_total(
    price: float,
    quantity: int
) -> float:
    """
    Calculate the total cost.
    """
    return price * quantity


@tool
def calculate_discount(
    amount: float,
    percentage: float
) -> float:
    """
    Calculate the discount amount.
    """
    return amount * percentage / 100
# Create Model
model=ChatOpenAI(
    model='gpt-4.1-nano',
    temperature=0
)
# Createa Checkpointer
checkpointer=InMemorySaver()
# Create Angent
agent=create_agent(
    model=model,
    tools=[
        calculate_total,calculate_discount
    ],
    checkpointer=checkpointer,
    system_prompt="""
    You are a helpful purchasing assistant.

    Use the available tools whenever calculations
    are required.

    Keep track of the current conversation context.
    """
)
while True:
    prompt=input('\nYou: ')
    if prompt.lower()=='exit':
        break;
    result=agent.invoke(
      {
           "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
      },
      config={
          'configurable':{
              'thread_id':'conversation-1'
          }
      }
    )
    print('\nAI: ',result['messages'][-1].content)