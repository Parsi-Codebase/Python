from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from pydantic import BaseModel
app = FastAPI()

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


class Base(DeclarativeBase):
    pass


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    age = Column(Integer)


Base.metadata.create_all(bind=engine)
#create database session
SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
)
#create model
class StudentCreate(BaseModel):
    name:str
    email:str
    age:int
@app.post('/students')
def create_student(student:StudentCreate):
    db=SessionLocal() # create a database session
    # create sqlalchemy object
    new_student=Student(
        name=student.name,
        email=student.email,
        age=student.age
    )
    db.add(new_student) # add object to the db session
    db.commit() # commit the transaction, record saved
    db.refresh(new_student) #Refresh the object from the database.Refresh the object from the database.
    db.close() # close the database session
    return new_student
@app.get('/students')
def get_students():
    db=SessionLocal()
    students=db.query(Student).all() # get all the students
    db.close()
    return students
@app.get('/students/{student_id}')
def get_student(student_id:int):
    db=SessionLocal()
    student=db.query(Student).filter(Student.id==student_id).first()
    db.close()
    if student is None:
          raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return student
@app.put('/students/{student_id}')
def update_student(student_id:int,student_update:StudentCreate):
    db=SessionLocal()
    student=db.query(Student).filter(Student.id==student_id).first()
    if student is None:
          raise HTTPException(
            status_code=404,
            detail="Student not found"
          )
    student.age=student_update.age
    student.email=student_update.email
    student.name=student_update.name
    db.commit()
    db.refresh(student)
    db.close()
    return student
@app.delete('/students/{student_id}')
def delete_student(student_id:int):
    db=SessionLocal()
    student=db.query(Student).filter(Student.id==student_id).first()
    if student is None:
              raise HTTPException(
                status_code=404,
                detail="Student not found"
              )
    db.delete(student)
    db.commit()
    db.close()
    return {
        "message": "Student deleted successfully"
    }