# using multiple tools
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from dotenv import load_dotenv
import os
load_dotenv()
# 1. Define Tools
@tool
def calculate_total(
    price:float,
    quantity:int
)->float:
    '''
    Calculate the total price
    Args:
    price:Price of one item.
    quantity: Number of items
    '''
    return price*quantity
@tool
def calculate_discount(
    amount:float,
    percentage:float
)->float:
    '''
    Calculate the discount amount.
    Args:
    amount:Orginal amounts
    percentage: Discount percentage
    '''
    return amount*percentage/100
@tool
def message()->str:
    '''simple tool'''
    return 'Hello world!!!'
    
# 2. Register Tools
tools=[
        calculate_total,
        calculate_discount,
        message
    ]
# 3. create model
model=ChatOpenAI(
        model='gpt-4.1-nano',
        temperature=0,
        api_key=os.getenv('OPENAI_API_KEY')
    )
# 4. Bind Tools
model_with_tools=model.bind_tools(
        tools
    )
# 5. Tool Map
tool_map={
    tool.name:tool for tool in tools
}
# 6. Tool Calling Loop
messages=[
    {
        'role':'user',
        'content':(
            'Calculate the total cost of '
            '5 items at 1000 each and '
            'then calculate a 10% discount '
            'finally show the Total amount after discount'
        )
    }
]
while True:
    # Ask GPT
    response=model_with_tools.invoke(messages)
    # Add GPT response to conversation
    messages.append(response)
    # Check for tool calls
    if not response.tool_calls:
        print('\nFinal Answer:')
        print(response.content)
        break
    #Execute requested tools
    for tool_call in response.tool_calls:
        tool_name=tool_call['name']
        tool_args=tool_call['args']
        #find tool
        selected_tool=tool_map[tool_name]
        #execute tool
        result=selected_tool.invoke(
            tool_args
        )
        # Send result back to GPT
        messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call['id']
            )
        )
    
