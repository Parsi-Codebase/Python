from fastapi import FastAPI
from database import Base
from database import engine
from models.product import Product
from routers.product_router import router
# create FastAPI app instance
app=FastAPI(
    title='Product Management API'
)
Base.metadata.create_all(bind=engine) # create tables in the database
app.include_router(router) # include the product router