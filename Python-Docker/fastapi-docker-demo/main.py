from fastapi import FastAPI
app=FastAPI(title='Docker FastAPI Demo')
@app.get('/')
def home():
    return{
        'message':'API is running inside docer'
    }
@app.get('/products')
def get_products():
    return [
        {'id':1,'name':'laptop'},
        {'id':2,'name':'keyboard'}
    ]