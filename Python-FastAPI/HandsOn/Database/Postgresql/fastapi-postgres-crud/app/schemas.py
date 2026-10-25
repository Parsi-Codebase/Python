from pydantic import BaseModel,ConfigDict
class ProductCreate(BaseModel):
    name:str
    description:str|None=None
    price:float
    quantity:int
class ProductResponse(BaseModel):
    id:int
    name:str
    description:str|None
    price:float
    quantity:int
    model_config=ConfigDict(
        from_attributes=True
    )