from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
@tool
def calculate_total(price: float, quantity: int) -> float:
    """
    Calculate the total price.

    Args:
        price: Price of one item.
        quantity: Number of items.
    """
    return price * quantity
model=ChatOpenAI(
    model='gpt-4.1-nano',
    temperature=0
)
# Create Agent
agent=create_agent(
    model=model,
    tools=[calculate_total]
)
result=agent.invoke(
    {
        'messages':[
            {
                'role':'user',
                'content':'Calculate the cost of 5 items at 1000 each'
            }
        ]
    }
)
# for message in result['messages']:
#     print(message.content)
print(result['messages'][-1].content)