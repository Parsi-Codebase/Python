from pydantic import BaseModel,ConfigDict
class UserRegister(BaseModel):
    username:str
    password:str
    role:str='student'
class UserReponse(BaseModel):
    id:int
    username:str
    role:str
    model_config=ConfigDict(from_attributes=True)
class TokenReponse(BaseModel):
    access_token:str
    refresh_token:str
    token_type:str
class RefershTokenRequest(BaseModel):
    refresh_token:str
class StudentCreate(BaseModel):
    name:str
    age:int
    course:str
class StudentResponse(BaseModel):
    id:int
    name:str
    age:int
    course:str
    created_by:int|None
    model_config=ConfigDict(from_attributes=True)

