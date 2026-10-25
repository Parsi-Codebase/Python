from fastapi import FastAPI,HTTPException
import logging
app=FastAPI()
logging.basicConfig(
    level=logging.DEBUG
)
logger=logging.getLogger(__name__)
def get_student(student_id:int):
    raise Exception('Internal Server Error')
@app.get('/students/{student_id}')
def student_by_id(student_id:int):
    try:
        student=get_student(student_id)
        if student is None:
         raise ValueError('Student not found')
        return student
    except Exception:
        logger.exception(
            "Faild to retrive student %s",student_id
        )