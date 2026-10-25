from fastapi import APIRouter
from models.student import StudentV2

router = APIRouter(
    prefix="/students",
    tags=["Students - V2"]
)


@router.get(
    "/",
    summary="Get students - V2",
    description="Returns students using the V2 response contract"
)
def get_students():

    return [
        {
            "id": 1,
            "full_name": "John Smith",
            "age": 25,
            "email": "john@example.com"
        },
        {
            "id": 2,
            "full_name": "David Smith",
            "age": 30,
            "email": "david@example.com"
        }
    ]


@router.post(
    "/",
    response_model=StudentV2,
    status_code=201,
    summary="Create student - V2"
)
def create_student(student: StudentV2):

    return student