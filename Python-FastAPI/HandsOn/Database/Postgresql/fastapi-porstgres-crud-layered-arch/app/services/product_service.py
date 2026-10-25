from ..schemas.product import ProductCreate,ProductResponse,ProductUpdate
from sqlalchemy.orm import Session
from ..models.product import Product
from ..repositories.product_repository import ProductRepository
class ProductServie:
    def __init__(self,db:Session):
        self.repository=ProductRepository(db)
    def create(self,product:ProductCreate):
        new_product=Product(
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity
        )
        return self.repository.create(new_product)
    def get_all(self):
        return self.repository.get_all()
    def get_by_id(self,product_id:int):
        return self.repository.get_by_id(product_id)
    def delete(self,product_id:int):
        product=self.repository.get_by_id(product_id)
        if product is None:
            return False
        self.repository.delete(product_id)
        return True
    def update(self,product_id:int,product_update:ProductUpdate):
        product=self.repository.get_by_id(product_id)
        product.price=product_update.price
        product.quantity=product_update.quantity
        product.name=product_update.name
        product.description=product_update.description
        return self.repository.update(product)
        