from pydantic import BaseModel,EmailStr,Field
class SupplierCreate(BaseModel):
    name:str=Field(min_length=2,max_length=100)
    email:EmailStr
    phone:str=Field(min_length=2,max_length=15)
    city:str=Field(min_length=2,max_length=50)
class SupplierResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    phone:str
    city:str
class SupplierUpdate(BaseModel):
    name:str|None=Field(default=None,min_length=2,max_length=100)
    email:EmailStr|None=None
    phone:str|None=Field(default=None,min_length=10,max_length=15)
    city:str|None=Field(default=None,min_length=2,max_length=50)