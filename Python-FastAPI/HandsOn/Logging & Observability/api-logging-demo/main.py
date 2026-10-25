from fastapi import FastAPI
import logging
app=FastAPI()
logging.basicConfig(
    level=logging.INFO
)
logger=logging.getLogger(__name__)
@app.get('/students')
async def get_students():
    logger.info('Fetching students')
    students=[
        {'id':1,'name':'John'},
        {'id':2,'name':'David'}
    ]
    return students