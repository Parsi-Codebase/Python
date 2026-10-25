from langchain_core.tools import tool
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
print(calculate_total.name)
print(calculate_total.description)
print(calculate_total.args_schema)
print(calculate_total.args)
# invoke the tool
result=calculate_total.invoke({
    'price':250,
    'quantity':4
})
print(result)