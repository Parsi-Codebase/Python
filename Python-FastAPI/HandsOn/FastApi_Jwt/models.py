from fastapi import FastAPI
from sqlalchemy import Integer,String,Column,ForeignKey
from database import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,nullable=False,index=True)
    password_hash=Column(String,nullable=False)
    role=Column(String,nullable=False,default='student')
class Student(Base):
    __tablename__='students'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)
    course=Column(String,nullable=False)
    created_by=Column(Integer,ForeignKey('users.id'),nullable=True)