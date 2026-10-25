from fastapi import FastAPI
from routers.v1.students import router as students_v1
from routers.v2.students import router as students_v2

app=FastAPI(
    title='Student API Management API',
    version='2.0.0'
)
app.include_router(
    students_v1,
    prefix='/api/v1'
)
app.include_router(
    students_v2,
    prefix='/api/v2'
)