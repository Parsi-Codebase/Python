from fastapi import FastAPI
from app.routers.products import router as product_router
app=FastAPI(
    title='Shop Assit AI',
    version='1.0.0'
)
app.include_router(product_router)
@app.get('/health')
def health():
    return {
        'status':'ok'
    }