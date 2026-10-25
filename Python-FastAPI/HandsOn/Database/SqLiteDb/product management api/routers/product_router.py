from fastapi import APIRouter # API router for product-related endpoints
from fastapi import Depends # Dependency injection for database session
from fastapi import HTTPException # HTTPException for handling errors
from sqlalchemy.orm import Session # import Session from sqlalchemy.orm
from database import get_db # import get_db function to get database session
from schemas.product import ProductCreate,ProductResponse
from services.product_service import ProductService
router=APIRouter(
    prefix='/products',
    tags=['products']
)
service=ProductService()
#get all products
@router.get('/',response_model=list[ProductResponse])
def get_products(db:Session=Depends(get_db)):
    return service.get_all_products(db)
# get product
@router.get('/{product_id}',response_model=ProductResponse)
def get_product(product_id:int,db:Session=Depends(get_db)):
    product=service.get_product(db,product_id)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return product
@router.post('/',status_code=201)
def create_product(product:ProductCreate,db:Session=Depends(get_db)):
    return service.create_product(db,product)
@router.put('/{product_id}')
def update_product(product_id:int,product:ProductCreate,db:Session=Depends(get_db)):
    updated_product=service.update_product(db,product_id,product)
    if update_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return updated_product
@router.delete('/{product_id}')
def delete_product(product_id:int,db:Session=Depends(get_db)):
    deleted=service.delete(db,product_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return {'message':'Product deleted successfully'}
    