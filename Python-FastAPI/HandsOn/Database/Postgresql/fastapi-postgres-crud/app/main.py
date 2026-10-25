from fastapi import FastAPI
from .database import engine,Base
from .routers import products
Base.metadata.create_all(bind=engine)
app=FastAPI(
    title='Product API',
    version='1.0.0'
)
app.include_router(products.router)
@app.get('/')
def root():
    return{
        'message':'Product API is running'
    }