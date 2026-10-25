from fastapi import FastAPI,HTTPException
app=FastAPI(
    title='Product Service'
)
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 75000
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 30000
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 5000
    }
]
@app.get('/products')
async def get_products():
    return products
@app.get('/products/{product_id}')
async def get_product(product_id:int):
    for product in products:
        if product['id']==product_id:
            return product
        raise HTTPException(
            status_code=404,
            detail='Product not found'
        )
@app.get('/health/live')
async def health():
    return{
        'service':'product-service',
        'status':'alive'
    }