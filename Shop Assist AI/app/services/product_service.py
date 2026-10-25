from typing import List
from app.schemas.product import Product
import json
from app.config import settings

# convert json data into List of Product schema
def load_products() -> List[Product]:
    with open(settings.products_file, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return [Product(**item) for item in raw]


products = load_products()


def get_all_products()->List[Product]:
    return products


def get_all_products_by_category(category: str)->List[Product]:
    category_products = []
    for product in products:
        if product.category == category:
            category_products.append(product)
    return category_products


def get_product(product_id: int)->Product|None:
    for product in products:
        if product.id == product_id:
            return product
    return None
