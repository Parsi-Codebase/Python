from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import jwt
from database import Base,engine,get_db
from models import User,Student
from schemas import UserRegister,UserReponse,TokenReponse,RefershTokenRequest,StudentCreate,StudentResponse
from auth import (hash_password,
                  verify_password,
                  create_access_token,
                  create_refresh_token,
                  decode_token)
from dependencies import (
    get_current_user,
    require_role
)
app=FastAPI(
    title='Student JWT API',
    version='1.0.0'
)
# create database tables
Base.metadata.create_all(bind=engine)
#api
@app.post('/register',response_model=UserReponse)
async def register(
    user:UserRegister,
    db:Session=Depends(get_db)
):
    existing_user=(
        db.query(User)
        .filter(User.username==user.username)
        .first()
    )
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exisits"
        )
    new_user=User(
        username=user.username,
        password_hash=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@app.post('/login',response_model=TokenReponse)
async def login(
    form_data:OAuth2PasswordRequestForm=Depends(),
    db:Session=Depends(get_db)
):
    user=(
        db.query(User)
        .filter(
            User.username==form_data.username
        )
        .first())
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )
    if not verify_password(
        form_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )
    access_token=create_access_token(
           user.username,
           user.role
    )
    refresh_token=create_refresh_token(
        user.username
    )
    return {
        'access_token':access_token,
        'refresh_token':refresh_token,
        'token_type':'bearer'
    }
@app.post(
    "/refresh"
)
async def refresh_token(
    request: RefershTokenRequest,
    db: Session = Depends(get_db)
):

    try:

        payload = decode_token(
            request.refresh_token
        )

        username = payload.get("sub")
        token_type = payload.get("type")

        if (
            username is None
            or token_type != "refresh"
        ):

            raise HTTPException(
                status_code=401,
                detail="Invalid refresh token"
            )

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    new_access_token = create_access_token(
        user.username,
        user.role
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }


# --------------------------------------------------
# CURRENT USER
# --------------------------------------------------

@app.get(
    "/me",
    response_model=UserReponse
)
async def get_me(
    current_user: User = Depends(
        get_current_user
    )
):

    return current_user

    # student api
@app.get(
    "/students",
    response_model=list[StudentResponse]
)
async def get_students(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    students = db.query(Student).all()

    return students
@app.post(
    "/students",
    response_model=StudentResponse
)
async def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    if current_user.role not in [
        "admin",
        "teacher"
    ]:

        raise HTTPException(
            status_code=403,
            detail="Only admin or teacher can create students"
        )

    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course,
        created_by=current_user.id
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student
@app.delete(
    "/students/{student_id}"
)
async def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_role("admin")
    )
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }