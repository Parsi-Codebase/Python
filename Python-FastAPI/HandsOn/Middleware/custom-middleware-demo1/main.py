from fastapi import FastAPI,Request
app=FastAPI()
# Custom middleware
# middleware is a function that runs before and after each request. 
# It can be used to modify the request or response, 
# or to perform some action before or after the request is processed.
@app.middleware('http')
async def my_middleware(request:Request,call_next):
    print('Before endpoint')
    #call_next() passes the request to the next component in the pipeline.
    response=await call_next(request) # Call the next middleware or endpoint
    print('After endpoint')
    return response
@app.get('/')
async def home():
    print('Inside endpoint')
    return {
        'message':'Hello FastAPI'
    }
    