from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
@tool
def calculate_total(
    price: float,
    quantity: int
) -> float:
    """
    Calculate total cost.
    """
    return price * quantity


@tool
def calculate_discount(
    amount: float,
    percentage: float
) -> float:
    """
    Calculate discount amount.
    """
    return amount * percentage / 100
model=ChatOpenAI(
    model='gpt-4.1-nano',
    temperature=0
)
agent=create_agent(
    model=model,
    tools=[
        calculate_total,
        calculate_discount
    ],
    system_prompt="""
    You are an AI programming and purchasing assistant.

    Explain concepts clearly.

    When a calculation is required,
    use the appropriate tool.

    Never perform important calculations mentally
    when a calculation tool is available.
    """   
)
while True:
    user_input=input('\nYou:')
    if user_input.lower()=='exit':
        break
    result=agent.invoke({
        'messages':[
            {
                'role':'user',
                'content':user_input
            }
        ]
    })
    final_message=result['messages'][-1]
    print('\nAI:',final_message.content)