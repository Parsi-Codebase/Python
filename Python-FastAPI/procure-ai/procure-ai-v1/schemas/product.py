from pydantic import BaseModel,Field
class ProductCreate(BaseModel):
    name:str=Field(min_length=2,max_length=100)
    description:str|None
    category:str
    unit_price:int=Field(gt=0)
    sku:str
    
class ProductUpdate(BaseModel):
    description:str|None
    category:str
    unit_price:int=Field(gt=0)
    sku:str
class ProductResponse(BaseModel):
     id:int
     name:str
     description:str
     category:str
     unit_price:int
     sku:str
    
