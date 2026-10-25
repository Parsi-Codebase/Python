from fastapi import FastAPI
from .database.database import Base,engine
from .routers.product_router import router as product_router
app=FastAPI(
    title='Product API',
    version='1.0.0'
)

app.include_router(product_router)
@app.get('/')
def home():
    return 'Product API Running!!!'
Base.metadata.create_all(bind=engine)