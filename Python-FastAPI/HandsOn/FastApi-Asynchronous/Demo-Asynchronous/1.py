import asyncio
async def greet():
    print('hello')
    await asyncio.sleep(3)
    print('welcome to fast api')
asyncio.run(greet()) # run the async functions