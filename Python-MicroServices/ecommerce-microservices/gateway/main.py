from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx
app=FastAPI(title='API Gateway')
PRODUCT_SERVICE_URL='http://localhost:8001'
ORDER_SERVICE_URL='http://localhost:8002'
@app.get('/api/products')
async def get_products():
    async with httpx.AsyncClient() as client:
        response=await client.get(
            f'{PRODUCT_SERVICE_URL}/products'
        )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json()
    )
@app.get('/api/orders')
async def get_orders():
    async with httpx.AsyncClient() as client:
        response=await client.get(
            f"{ORDER_SERVICE_URL}/orders"
        )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json()
    )
@app.get('/api/orders/{order_id}')
async def get_order(order_id:int):
    async with httpx.AsyncClient() as client:
        response=await client.get(
            f'{ORDER_SERVICE_URL}/orders/{order_id}'
        )
        print(response.json())
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
@app.get('/health')
async def health():
    return{
        'service':'api-gateway',
        'status':'alive'
    }
    