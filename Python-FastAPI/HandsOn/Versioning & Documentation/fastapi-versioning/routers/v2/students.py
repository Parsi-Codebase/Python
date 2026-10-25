from fastapi import APIRouter

router = APIRouter(
    prefix="/students",
    tags=["Students V2"]
)


@router.get("/")
def get_students():
    return [
        {
            "id": 1,
            "full_name": "John",
            "email": "john@example.com"
        },
        {
            "id": 2,
            "full_name": "David",
            "email": "david@example.com"
        }
    ]