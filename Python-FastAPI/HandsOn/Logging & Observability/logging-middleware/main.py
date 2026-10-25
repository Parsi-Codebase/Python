from fastapi import FastAPI,Request
import logging
import time
app=FastAPI()
logging.basicConfig(
    level=logging.INFO
)
logger=logging.getLogger(__name__)
@app.middleware('http')
async def logging_middleware(request:Request,call_next):
    start_time=time.time()
    logger.info(
        'request started: %s %s',
        request.method,
        request.url.path
    )
    response=await call_next(request)
    duration=time.time()-start_time
    logger.info(
        'Request completed: %s %s status=%s druation=%.3f',
        request.method,
        request.url.path,
    response.status_code,
    duration
    )
    return response
@app.get('/students')
def get_studenets():
    return 'students fetched!!'