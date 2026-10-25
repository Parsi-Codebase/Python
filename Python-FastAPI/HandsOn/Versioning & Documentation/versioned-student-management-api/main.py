from fastapi import FastAPI

from routers.v1.students import router as students_v1
from routers.v2.students import router as students_v2


app = FastAPI(
    title="Student Management API",
    summary="Versioned Student Management REST API",
    description="""
    A demonstration FastAPI application showing:

    - API Versioning
    - OpenAPI
    - Swagger UI
    - ReDoc
    - Tags
    - API Metadata
    - Request Examples
    """,
    version="2.0.0",
    docs_url="/swagger",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    contact={
        "name": "API Support",
        "email": "support@example.com"
    }
)


app.include_router(
    students_v1,
    prefix="/api/v1"
)

app.include_router(
    students_v2,
    prefix="/api/v2"
)