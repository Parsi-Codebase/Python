from fastapi import FastAPI
from routers.student_router import router as student_router
app=FastAPI(
    title='Student Managment API',
    version='1.0.0'
)
app.include_router(student_router)