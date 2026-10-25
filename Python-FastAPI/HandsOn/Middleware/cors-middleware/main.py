from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    #defines which frontend origins are allowed
    allow_origins=['http://localhost:4200'],
    allow_credentials=True,
    allow_methods=['*'], # allowed http methods
    allow_headers=['*'] # allowed http headers
)
@app.get('/products')
async def products():
    return {
        'products':[
            'laptop','mobile'
        ]
    }