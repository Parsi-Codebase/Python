from fastapi import FastAPI,Request
import asyncio
import time
app=FastAPI()
@app.middleware('http')
async def timing_middleware(request:Request,call_next):
    start_time=time.perf_counter()
    response=await call_next(request)
    end_time=time.perf_counter()
    duration=end_time-start_time
    # put the duration into response header
    response.headers["X-Process-Time"] = f"{duration:.4f}"
    print(
        f'{request.method} '
        f'{request.url.path} '
        f'took {duration:4f} seconds'
    )
    return response
@app.get('/products')
async def products():
    await asyncio.sleep(1)
    return {
        'message':'Products'
    }