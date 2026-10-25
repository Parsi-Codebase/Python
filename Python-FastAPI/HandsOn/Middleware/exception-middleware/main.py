from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
app=FastAPI()
@app.middleware("http")
async def exception_middleware(
    request: Request,
    call_next
):

    try:

        response = await call_next(request)

        return response

    except Exception as ex:

        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal Server Error",
                'error':str(ex)
                
            }
        )
@app.get('/{n}')
def welcome(n:int):
    if n==5:
        raise Exception()
    return 'hello'
    
@app.get('/{a}/{b}')
def div(a:int,b:int):
    if b==0:
        raise ZeroDivisionError('b value should not zero')
    return a/b