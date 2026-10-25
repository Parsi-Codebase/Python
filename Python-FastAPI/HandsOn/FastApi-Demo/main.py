from fastapi import FastAPI #import FastAPI class
app=FastAPI() # app rep FastAPI Web App
#path operation decorator
@app.get('/') # end point
def hello():
    return {'message':'Hello World'}
@app.get('/welcome')
def welcome():
    return {'message':'Welcome to FastAPI'}

#run the app
# uvicorn main:app --reload
# main  → main.py
# app   → FastAPI object
# --reload server automatically restarts when you modify the source code.