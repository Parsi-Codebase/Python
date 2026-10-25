from fastapi import APIRouter
from schemas.student import(
    StudentCreate,StudentReponse
)
from services.student_service import(
    get_students,get_student,add_student,remove_student
)
router=APIRouter(
    prefix='/students',
    tags=['Students']
)
@router.get('/',response_model=list[StudentReponse])
def get_all():
    return get_students()
@router.get('/{student_id}',response_model=StudentReponse)
def get_by_id(student_id:int):
    return get_student(student_id)
@router.post('/',response_model=StudentReponse,
             status_code=201)
def create(student:StudentCreate):
    return add_student(student)
@router.delete('/{student_id}')
def delete(student_id:int):
    return remove_student(student_id)
    