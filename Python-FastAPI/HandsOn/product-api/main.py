from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
app=FastAPI(
    title='ECar App',
    description='Product API',
    version='1.0.0'
)
#create product Model
class Product(BaseModel):
    id:int
    name:str
    price:int
products=[
    Product(id=1,name='laptop',price=90000),
     Product(id=2,name='keyboard',price=900),
  
]
#Get all products
@app.get('/products')
def getall(skip:int=0,limit:int=10):
    return products[skip:skip+limit]
#Get product by id
@app.get('/product/{product_id}')
def get(product_id:int):
    for product in products:
        if(product.id==product_id):
            return product
    raise HTTPException(
        status_code=404,
        detail='Product not found'
    )
#Create product
@app.post('/create')
def create(product:Product):
    products.append(product)
    return{
        'message':'Product added successfully',
        'product':product
    }
#Update entire product
@app.put('/edit/{product_id}')
def update(product_id:int,productUpdate:Product):
     for existing_product in products:

        if existing_product.id == product_id:

            existing_product.name = productUpdate.name
            existing_product.price = productUpdate.price

            return existing_product

     raise HTTPException(
        status_code=404,
        detail='Product not found'
    )
    
# Delete product
@app.delete('/delete/{product_id}')
def delete(product_id:int):
    for product in products:
        if(product.id==product_id):
            products.remove(product)
            return {'message':'Product deleted successfully'}
    raise HTTPException(
        status_code=404,
        detail='Product not found'
    )