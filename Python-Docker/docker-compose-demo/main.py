from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine,String,Integer
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,Session
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL=os.getenv('DATABASE_URL')
engine=create_engine(DATABASE_URL)
class Base(DeclarativeBase):
    pass
class Student(Base):
    __tablename__='students'
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    age:Mapped[int]
    Base.metadata.create_all(engine)
app=FastAPI()
class StudentRequest(BaseModel):
    name:str
    age:int
@app.post('/students')
def create_student(student:StudentRequest):
    with Session(engine) as session:
        new_student=Student(
            name=student.name,
            age=student.age
        )
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        return{
            'id':new_student.id,
            'name':new_student.name,
            'age':new_student.age
        }
@app.get('/students')
def get_students():
    with Session(engine) as session:
        students=session.query(Student).all()
        return students
        