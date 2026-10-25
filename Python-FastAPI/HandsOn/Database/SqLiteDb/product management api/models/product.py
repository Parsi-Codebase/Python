from sqlalchemy import Column,Integer,String,Float #import Column,Integer,String,Float from sqlalchemy
from database import Base # import Base from database.py
# create Product model
class Product(Base):
    __tablename__='products' # create table name
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    price=Column(Float,nullable=False)
    