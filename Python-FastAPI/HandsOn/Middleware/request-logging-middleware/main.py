from fastapi import FastAPI,Request
app=FastAPI()
@app.middleware("http")
async def logging_middleware(request:Request,call_next):
    client_host=request.client.host if request.client else 'Unknown'
    print(f'Client Ip:{client_host}')
    print(f'Request:{request.method} {request.url}')
    response=await call_next(request)
    print(f'Response Status:{response.status_code}')
    return response
@app.get('/products')
async def get_products():
    return{
        'products':[
            'laptop','mobile','keyboar'
        ]
    }
@app.post('/products')
async def create_product():
    return{
        'message':'Product Created!!'
    }