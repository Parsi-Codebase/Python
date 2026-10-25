from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time

app = FastAPI()


# -----------------------------
# CORS Middleware
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Logging + Timing Middleware
# -----------------------------

@app.middleware("http")
async def logging_middleware(
    request: Request,
    call_next
):

    start_time = time.perf_counter()

    client = request.client.host if request.client else "Unknown"

    print("--------------------------------")
    print(f"Method : {request.method}")
    print(f"Path   : {request.url.path}")
    print(f"Client : {client}")

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = f"{duration:.4f}"

    print(f"Status : {response.status_code}")
    print(f"Time   : {duration:.4f} seconds")
    print("--------------------------------")

    return response


# -----------------------------
# Public API
# -----------------------------

@app.get("/public")
async def public():

    return {
        "message": "Public API"
    }


# -----------------------------
# Product API
# -----------------------------

@app.get("/products")
async def products():

    return {
        "products": [
            {
                "id": 1,
                "name": "Laptop"
            },
            {
                "id": 2,
                "name": "Mobile"
            }
        ]
    }


# -----------------------------
# Error Demo
# -----------------------------

@app.get("/error")
async def error():

    return JSONResponse(
        status_code=500,
        content={
            "message": "Something went wrong"
        }
    )