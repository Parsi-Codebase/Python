from fastapi import FastAPI

app = FastAPI(
    #metadata
    title="Student Management API",
    summary="Student management REST API",
    description="""
    This API provides operations for managing students.

    Features:
    - Create students
    - Get students
    - Update students
    - Delete students
    """,
    version="1.0.0",
    #contact information
    contact={
        "name": "API Support",
        "email": "support@example.com"
    },
    #license information
    license_info={
        "name": "MIT"
    }
)
@app.get('/')
def welcome():
    return 'welcome'