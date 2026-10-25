from fastapi import FastAPI,Response,HTTPException,status
from pydantic import BaseModel
app=FastAPI()
# creaet models
class ProductCreate(BaseModel):
    name:str
    price:int
    category:str
class Product(ProductCreate):
    id:int
#in-memory database
products=[
    {'id':1,'name':'laptop','price':75000,'category':'Electronics'},
    {'id':2,'name':'mouse','price':1200,'category':'Electronics'}
]
@app.get('/')
def welcome():
    return 'Welcome to Fast API Request Response'
# get all products
@app.get('/products',response_model=list[Product])
def get_products(response:Response):
    response.headers['X-App-Version']="1.0"
    return products
# get product
@app.get(
    "/products/{product_id}",
    response_model=Product
)
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
# Create Product
@app.post('/products',response_model=Product,
          status_code=status.HTTP_201_CREATED)
def create_product(product:ProductCreate):
    new_product={
        'id':len(products)+1,
        'name':product.name,
        'price':product.price,
        'category':product.category
    }
    products.append(new_product)
    return new_product
# delete product
@app.delete('/products/{product_id}')
def delete_product(product_id:int):
    for product in products:
        if product['id']==product_id:
            products.remove(product)
            return
    raise HTTPException(
        status_code=404,
        detail='Product not found'
    )
