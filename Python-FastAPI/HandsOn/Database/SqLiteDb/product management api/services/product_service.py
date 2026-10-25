from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate,ProductResponse
from repositories.product_repository import ProductRepository
class ProductService:
    # initialize the ProductService with a ProductRepository instance
    def __init__(self):
        self.repository=ProductRepository()
    def get_all_products(self,db:Session):
        return self.repository.get_all(db)
    def get_product(self,db:Session,id:int):
        return self.repository.get_by_id(db,id)
    def create_product(self,db:Session,product_data:ProductCreate):
        product=Product(
            name=product_data.name,
            price=product_data.price
        )
        return self.repository.create(db,product)
    def update_product(
        self,db:Session,
        product_id:int,product_data:ProductCreate
    ):
        product=self.repository.get_by_id(db,product_id)
        if product is None:
            return None
        product.name=product_data.name
        product.price=product_data.price
        return self.repository.update(db,product)
    def delete(self,db:Session,product_id:int):
        product=self.repository.get_by_id(db,product_id)
        if product is None:
            return False
        self.repository.delete(db,product)
        return True