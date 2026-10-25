from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from dotenv import load_dotenv
import os
load_dotenv()
@tool
def calculate_total(
    price: float,
    quantity: int
) -> float:
    """
    Calculate the total price.

    Args:
        price: Price of one item.
        quantity: Number of items.
    """

    return price * quantity
model=ChatOpenAI(
    model='gpt-4.1-nano',
    temperature=0.3,
    api_key=os.getenv('OPENAI_API_KEY')
)
# bind tools with model
model_with_tools=model.bind_tools([
    calculate_total
])
messages=[
    {
        'role':'user',
        'content':(
            'Calculate the total cost '
            'of 5 items at 250 each'
        )
    }
]
# step 1 - Aks GPT
response=model_with_tools.invoke(messages)
# Step 2 -Execute tool
tool_call=response.tool_calls[0] # access the first tool
result=calculate_total.invoke(
    tool_call['args']
)
# step 3- Add GPT response
messages.append(response)
# step 4 - Add tool result
messages.append(
    ToolMessage(
        content=str(result),
        tool_call_id=tool_call['id']
    )
)
# step 5 - Ask GPT for final answer
final_response=model_with_tools.invoke(messages)
print(final_response.content)