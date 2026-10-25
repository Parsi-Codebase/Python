from fastapi import FastAPI
from pydantic import BaseModel,Field,ConfigDict,field_validator
app=FastAPI()
# model creation
class Address(BaseModel):
    city:str=Field(min_length=2,max_length=50)
    state:str=Field(min_length=2,max_length=50)
class Student(BaseModel):
    model_config=ConfigDict(
        extra='forbid'
    )
    name:str
    age:int=Field(ge=18,le=60)
    course:str=Field(min_length=2,max_length=50)
    email:str
    address:Address
    @field_validator('name')
    @classmethod
    def validate_name(cls,value):
        if not value.strip():
            raise ValueError('Name cannot be empty')
        return value

@app.post('/students')
def register_student(student:Student):
    return {'message':'Student registered successfully',
            'student':student.model_dump()}
    
@app.get('/')
def welcome():
    return 'Welcome to fast api data validation'