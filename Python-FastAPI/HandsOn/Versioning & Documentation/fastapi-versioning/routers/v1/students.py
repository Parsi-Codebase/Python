from fastapi import APIRouter
router=APIRouter(
    prefix='/students',
    tags=['Students V1']
)
@router.get('/')
def get_students():
    return [
        {'id':1,'name':'john'},
        {'id':2,'name':'david'}
    ]