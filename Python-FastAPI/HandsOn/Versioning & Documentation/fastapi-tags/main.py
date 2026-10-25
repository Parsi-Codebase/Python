from fastapi import FastAPI
app=FastAPI()
# tags are use to group the endpoints with in the swagger UI
@app.get('/students',tags=['Students'])
def get_students():
    return []
@app.post('/students',
          tags=['Students'])
def create_student():
    return{
        'message':'Student created'
    }
@app.get('/courses',
         tags=["Courses"])
def get_courses():
    return []