from sqlalchemy.orm import Session
from ..models.product import Product
class ProductRepository:
    def __init__(self,db:Session):
        self.db=db
    def create(self,product:Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    def get_all(self):
        return self.db.query(Product).all()
    def get_by_id(self,product_id:int):
        product=self.db.get(Product,product_id)
        return product
    def delete(self,product_id:int):
        product=self.db.get(Product,product_id)
        self.db.delete(product)
        self.db.commit()
    def update(self,product:Product):
        self.db.commit()
        self.db.refresh(product)
        return product
    