from pydantic import BaseModel
class StudentCreate(BaseModel):
    name:str
    age:int
    course:str
class StudentReponse(BaseModel):
    id:int
    name:str
    age:int
    course:str
    