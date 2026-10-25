from fastapi import FastAPI,Depends
from studentRegistry import StudentRepository
from studentService import StudentService
app = FastAPI()
# dependecy functions
def get_student_repository():
    return StudentRepository()
def get_student_service(repository=Depends(get_student_repository)): # type: ignore
    return StudentService(repository)
#API
@app.get('/students')
def get_students(service=Depends(get_student_service)): # type:ignore
    return service.get_students()
@app.get('/students/{student_id}')
def get_student(student_id:int,service=Depends(get_student_service)):
    student= service.get_student(student_id)
    if student is None:
        return{'message':'student not found'}
    return student