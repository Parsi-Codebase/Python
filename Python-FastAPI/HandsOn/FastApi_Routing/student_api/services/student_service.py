from fastapi import FastAPI,HTTPException
from repositories.student_repository import(
    get_all_students,
    get_student_by_id,
    create_student,
    delete_student
)
def get_students():
    return get_all_students()
def get_student(student_id:int):
    student=get_student_by_id(student_id)
    if student is None:
        raise HTTPException(
            status_code=404,
            detail='Student Not Found'
        )
    return student
def add_student(student):
    return create_student(student)
def remove_student(student_id:int):
    student=get_student_by_id(student_id)
    if student is None:
         raise HTTPException(
                    status_code=404,
                    detail='Student Not Found'
         )
    delete_student(student_id)
    return{
        'message':'student deleted successfully'
    }
    