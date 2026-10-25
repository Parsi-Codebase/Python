from langchain_core.tools import tool
from langchain_ollama import ChatOllama
# define the tool
@tool
def calculate_total(price:float,quantity:int)->float:
    '''
    Calculate the total price.
    Args:
    price: Price of one item.
    quantity: Number of items
    '''
    return price*quantity
model=ChatOllama(
    model='phi3',
    temperature=0.3
)
# bind tools to a model
model_with_tools=model.bind_tools([
    calculate_total
])
# invoke the tool
result=model_with_tools.invoke(
    'Calculate the total cost of 5 items at 250 each'
)
print(result)