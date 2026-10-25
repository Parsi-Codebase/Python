from fastapi import APIRouter
from schemas.product import ProductCreate,ProductResponse,ProductUpdate
router=APIRouter(
    prefix='/api/v1/products',
    tags=['Products']
)
@router.get("",response_model=list[ProductResponse])
async def get_products():
    return [
       {'id':1,'name':'laptop','category':'product','description':'product','unit_price':80000,'sku':'2'},
       {'id':2,'name':'mouse','category':'product','description':'product','unit_price':800,'sku':'2'}
    ]
@router.post('',response_model=ProductResponse)
async def create_product(product:ProductCreate):
    return {
        id:1,
        'name':product.name,
        'category':product.category,
        'description':product.description,
        'unit_price':product.unit_price,
        'sku':product.sku
    }
@router.patch('/{product_id}',response_model=ProductResponse)
async def update_product(product_id:int,product:ProductUpdate):
    return {
        'id':product_id,
        'name':'somename',
        'description':product.description or 'sample',
        'category':product.category or 'product',
        'unit_price':product.unit_price or 1000,
        'sku':product.sku or 2
        
    }