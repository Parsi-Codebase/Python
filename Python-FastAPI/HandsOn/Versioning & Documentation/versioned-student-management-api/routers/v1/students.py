from fastapi import APIRouter
from models.student import StudentV1

router = APIRouter(
    prefix="/students",
    tags=["Students - V1"]
)


@router.get(
    "/",
    summary="Get students - V1",
    description="Returns students using the V1 response contract"
)
def get_students():

    return [
        {
            "id": 1,
            "name": "John",
            "age": 25
        },
        {
            "id": 2,
            "name": "David",
            "age": 30
        }
    ]


@router.post(
    "/",
    response_model=StudentV1,
    status_code=201,
    summary="Create student - V1"
)
def create_student(student: StudentV1):

    return student