from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
@tool
def calculate_total(
    price: float,
    quantity: int
) -> float:
    """
    Calculate the total price.
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
model=ChatOpenAI(
    model='gpt-4.1-nano',
    temperature=0
)
agent=create_agent(
    model=model,
    tools=[
        calculate_total,calculate_discount
    ]
)
result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": (
                "Calculate the total cost of "
                "5 items at ₹1000 each and "
                "then calculate a 10% discount."
            )
        }
    ]
})
final_message=result['messages'][-1]
print(final_message.content)