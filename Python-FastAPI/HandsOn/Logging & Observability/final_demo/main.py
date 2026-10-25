from fastapi import FastAPI, Request, HTTPException
import logging
import time
from uuid import uuid4


# -----------------------------------
# Logging Configuration
# -----------------------------------

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(name)s "
        "%(message)s"
    )
)

logger = logging.getLogger("student-api")


# -----------------------------------
# FastAPI Application
# -----------------------------------

app = FastAPI(
    title="Student API",
    version="1.0.0"
)


# -----------------------------------
# Correlation ID + Request Logging
# -----------------------------------

@app.middleware("http")
async def observability_middleware(
    request: Request,
    call_next
):

    correlation_id = request.headers.get(
        "X-Correlation-ID"
    )

    if not correlation_id:
        correlation_id = str(uuid4())

    start_time = time.perf_counter()

    logger.info(
        "Request started "
        "method=%s path=%s correlation_id=%s",
        request.method,
        request.url.path,
        correlation_id
    )

    try:

        response = await call_next(request)

        duration = (
            time.perf_counter() - start_time
        )

        logger.info(
            "Request completed "
            "method=%s path=%s status=%s "
            "duration=%.3fs correlation_id=%s",

            request.method,
            request.url.path,
            response.status_code,
            duration,
            correlation_id
        )

        response.headers[
            "X-Correlation-ID"
        ] = correlation_id

        return response

    except Exception:

        logger.exception(
            "Unhandled exception "
            "correlation_id=%s",
            correlation_id
        )

        raise


# -----------------------------------
# Health Check
# -----------------------------------

@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }


# -----------------------------------
# Readiness Check
# -----------------------------------

@app.get("/health/ready")
async def readiness():

    return {
        "status": "ready",
        "database": "available"
    }


# -----------------------------------
# Student API
# -----------------------------------

students = [
    {
        "id": 1,
        "name": "John"
    },
    {
        "id": 2,
        "name": "David"
    }
]


@app.get("/students")
async def get_students():

    logger.info(
        "Fetching all students"
    )

    return students


# -----------------------------------
# Get Student
# -----------------------------------

@app.get("/students/{student_id}")
async def get_student(student_id: int):

    logger.info(
        "Fetching student id=%s",
        student_id
    )

    for student in students:

        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# -----------------------------------
# Demo Exception
# -----------------------------------

@app.get("/error")
async def error():

    try:

        result = 10 / 0

        return {
            "result": result
        }

    except Exception:

        logger.exception(
            "Unexpected error occurred"
        )

        raise