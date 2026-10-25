from fastapi import FastAPI,Request
app=FastAPI()
@app.middleware('http')
async def response_middleware(request:Request,call_next):
    response=await call_next(request)
    response.headers['X-App-Name']='FastAPI Training'
    response.headers["X-API-Version"] = "1.0"
    return response
@app.get('/')
async def home():
    return{
        'message':'hello'
    }