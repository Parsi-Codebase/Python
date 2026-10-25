from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI(
    title='student crud api',
    description='A simple student crud api using fastapi',
    version='1.0.0'
)
#pydantic model
class Student(BaseModel):
    id:int
    name:str
    age:int
    course:str

#in-memory list
students=[
Student(id=1,name='john',age=10,course='python'),
Student(id=2,name='mark',age=11,course='dotnet'),
Student(id=3,name='tim',age=12,course='java')
]
#get all students
@app.get('/students')
def getall():
    return students
#get student by ID
@app.get('/student/{student_id}')
def getstudent(student_id:int):
    for student in students:
        if(student.id==student_id):
            return student
    raise HTTPException(
        status_code=404,
        detail='Student not found'
    )
# create student
@app.post('/student',status_code=201)
def addstudent(student:Student):
    students.append(student)
    return {'message':'student created successfully',
            'student':student}
#update student
@app.put('/update/{student_id}',status_code=201)
def updatestudent(student_id:int,update_student:Student):
    for index,student in enumerate(students):
        if(student.id==student_id):
           student[index]=update_student
           return {'message':'student updated successfully',
            'student':student}
    raise HTTPException(
    status_code=404,
    detail="Invalid Student Id"
)
            
@app.delete('/delete/{student_id}')
def deletestudent(student_id:int):
    for index, student in enumerate(students):

        if student.id == student_id:

            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )