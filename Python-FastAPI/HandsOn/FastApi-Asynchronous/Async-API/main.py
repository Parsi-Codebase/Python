from fastapi import FastAPI
import asyncio
app=FastAPI()
@app.get('/students')
async def get_students():
    print('fetching stuents')
    await asyncio.sleep(3)
    print('students fetched')
    return[
        {'id':1,'name':'varun'},
        {'id':2,'name':'suren'}
    ]