from fastapi import APIRouter, HTTPException
from app.services.product_service import (
    get_all_products,
    get_product,
    get_all_products_by_category,
)
from app.schemas.product import Product
router = APIRouter(prefix="/products", tags=["products"])


@router.get("",response_model=list[Product])
def get_products_by_category(category: str | None=None):
    if not category:
        return get_all_products()
    products = get_all_products_by_category(category.lower())
    if products:
        return products
    raise HTTPException(status_code=404, detail="Product not found")


@router.get("/{product_id}",response_model=Product)
def get_by_id(product_id: int):
    product = get_product(product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")
