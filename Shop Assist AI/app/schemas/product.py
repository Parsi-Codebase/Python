from pydantic import BaseModel,Field
class Product(BaseModel):
    id:int
    name:str
    category:str
    price:float=Field(gt=0)
    description:str
    stock:int=Field(ge=0)