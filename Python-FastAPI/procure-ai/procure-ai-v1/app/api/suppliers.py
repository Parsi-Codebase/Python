from fastapi import APIRouter
from schemas.supplier import SupplierCreate,SupplierResponse,SupplierUpdate
router=APIRouter(
    prefix='/api/v1/supplies',
    tags=['Suppliers']
)
@router.get('',response_model=list[SupplierResponse])
async def get_suppliers():
    return [
        {'id':1,'name':'ABC Technologies','city':'Hyderabad'},
        {'id':2,'name':'XYZ Solutions','city':'Banglore'}
    ]
@router.post('',response_model=SupplierResponse)
async def create_supplier(supplier:SupplierCreate):
    return{
        'id':1,
        "name":supplier.name,
        "email":supplier.email,
        'phone':supplier.phone,
        'city':supplier.city
    }
@router.patch('/{supplier_id}',response_model=SupplierResponse)
async def update_supplier(
    supplier_id:int,
    supplier:SupplierUpdate
):
    return {
        'id':supplier_id,
        'name':supplier.name or 'ABC Tech',
        'email':supplier.email or 'abc@test.com',
        'phone':supplier.phone or '9098909890',
        'city':supplier.city or 'Hyderabad'
    }