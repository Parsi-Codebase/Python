from sqlalchemy.orm import Session #import Session from sqlalchemy.orm
from models.product import Product
class ProductRepository:
    def get_all(self,db:Session):
        return db.query(Product).all()
    def get_by_id(self,db:Session,id:int):
        return db.query(Product).filter(Product.id==id).first()
    def create(self,db:Session,product:Product):
        db.add(product)
        db.commit() # commit the transaction
        db.refresh(product) # refresh the instance with the new data from the database
        return product
    def update(self,db:Session,product:Product):
        db.commit() # commit the transaction
        db.refresh(product)
        return product
    def delete(self,db:Session,product:Product):
        db.delete(product)
        db.commit() # commit the transaction
        