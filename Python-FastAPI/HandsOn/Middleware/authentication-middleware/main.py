from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
app=FastAPI()
@app.middleware('http')
async def auth_middleware(request:Request,call_next):
    if request.url.path=='/public':
        return await call_next(request)
     # Public endpoints
    public_paths = [
        "/docs",
        "/openapi.json",
        "/redoc",
    ]
    if request.url.path in public_paths:
        return await call_next(request)
    token=request.headers.get('Authorization')
    print(token)
    if token!='Bearer my-secret-token':
        return JSONResponse(
            status_code=401,
            content={
                'detail':'Unauthorized'
            }
        )
    response=await call_next(request)
    return response
@app.get('/public')
async def public():
    return{
        'message':'Public endpoint'
    }
@app.get('/products')
async def products():
    return{
        'message':'Protected products'
    }