import asyncio

async def simple_coro2():
    await asyncio.sleep(5)
    print("ok");

async def init(loop):
   await simple_coro2();
   print("haha");


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
