from fastapi import APIRouter
router=APIRouter(
    prefix='/api/v1/purchase-orders',
    tags=['purchase-orders']
)
@router.get('')
async def get_purchase_orders():
    return []