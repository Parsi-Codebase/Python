from fastapi import FastAPI
import asyncio
app=FastAPI()
async def get_customer():
    print('Getting customer..')
    await asyncio.sleep(2)
    return{
        'id':1,'name':'ram'
    }
async def get_orders():
    print('Getting orders...')
    await asyncio.sleep(3)
    return [
        {'id':101,'product':'laptop'},
        {'id':102,'product':'mouse'}
    ]
async def get_payments():
    print('Getting payments....')
    await asyncio.sleep(1)
    return [
        {'id':501,'amount':500}
    ]
@app.get('/customer-dashboard')
async def customer_dashboard():
    customer,orders,payments=await asyncio.gather(get_customer(),
                                                  get_orders(),
                                                  get_payments()) # Execute all async functions concurrently
    return {
        'customer':customer,
        'orders':orders,
        'payments':payments
    }