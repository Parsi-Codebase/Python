from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Product
from ..schemas import ProductCreate,ProductResponse
router=APIRouter(
    prefix='/api/products',
    tags=['Products']
)
@router.post('/',
             response_model=ProductResponse,
             status_code=201
)
def create_product(
     product:ProductCreate,
        db:Session=Depends(get_db)
):
    new_product=Product(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
@router.get('/',response_model=list[ProductResponse])
def get_products(
    db:Session=Depends(get_db)
):
    products=db.query(Product).all()
    return products
@router.get('/{product_id}',response_model=ProductResponse)
def get_product(product_id:int,
                db:Session=Depends(get_db)):
    product=db.get(Product,product_id)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail='Product not found'
        )
    return product
@router.put('/{product_id}',response_model=ProductResponse)
def update_product(
    product_id:int,
    product_data:ProductCreate,
    db:Session=Depends(get_db)
):
    product=db.get(Product,product_id)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail='Product not found'
        )
    product.name=product_data.name
    product.description=product_data.description
    product.price=product_data.price
    product.quantity=product_data.quantity
    db.commit()
    db.refresh(product)
    return product
@router.delete('/{product_id}',status_code=204)
def delete_product(product_id:int,
                   db:Session=Depends(get_db)):
    product = db.get(Product, product_id)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found")
    db.delete(product)
    db.commit()