from fastapi import FastAPI,HTTPException
import httpx
app=FastAPI(
    title='order service'
)
PRODUCT_SERVICE_URL='http://localhost:8001'
orders = [
    {
        "id": 1,
        "product_id": 1,
        "quantity": 2
    }
]
@app.get('/orders')
async def get_orders():
    return orders
@app.get('/orders/{order_id}')
async def get_order(order_id:int):
    order=next(
        (
            order for order in orders
            if order['id']==order_id
        ),
        None
    )
    print(order)
    if order is None:
        raise HTTPException(
            status_code=404,
            detail='order not found'
        )
    async with httpx.AsyncClient() as client:
        response=await client.get(
            f'{PRODUCT_SERVICE_URL}/products/{order['product_id']}'
        )
    product=response.json()
    return{
        'order_id':order['id'],
        'quantity':order['quantity'],
        'product':product
    }
@app.get('/health/live')
async def health():
    return{
        'service':'order-service',
        'status':'alive'
    }