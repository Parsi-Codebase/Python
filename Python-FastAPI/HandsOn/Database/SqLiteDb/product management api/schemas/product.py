from pydantic import BaseModel #import BaseModel from pydantic
class ProductCreate(BaseModel):
    name:str
    price:float
class ProductResponse(BaseModel):
    id:int
    name:str
    price:float