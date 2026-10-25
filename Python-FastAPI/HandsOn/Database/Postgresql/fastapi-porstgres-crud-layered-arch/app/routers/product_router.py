from fastapi import APIRouter,Depends,HTTPException
from ..schemas.product import ProductUpdate,ProductCreate,ProductResponse
from ..services.product_service import ProductServie
from sqlalchemy.orm import Session
from ..database.database import get_db
router=APIRouter(
    prefix='/api/products',
    tags=["Products"]
)
@router.get('/',response_model=list[ProductResponse])
def get_all(db:Session=Depends(get_db)):
    service=ProductServie(db)
    return service.get_all()
@router.post('/',response_model=ProductResponse)
def create(product_data:ProductCreate,db:Session=Depends(get_db)):
    service=ProductServie(db)
    return service.create(product_data)
@router.get('/{product_id}',response_model=ProductResponse)
def get_by_id(product_id:int,db:Session=Depends(get_db)):
    service=ProductServie(db)
    product=service.get_by_id(product_id)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail='Product not found'
        )
    return product
@router.delete('/{product_id}',status_code=204)
def delete(product_id:int,db:Session=Depends(get_db)):
    service=ProductServie(db)
    result=service.delete(product_id)
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return {
        'message':'Product deleted successfully'
    }
@router.put('/{product_id}',response_model=ProductResponse)
def update(product_id:int,
           product_update:ProductUpdate,
           db:Session=Depends(get_db)):
    service=ProductServie(db)
    product= service.update(product_id,product_update)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    