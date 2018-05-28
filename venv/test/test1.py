import asyncio


async def hello(loop):
    print("Hello world!")
    await asyncio.sleep(5)
    print("Hello again!")


def test(loop):
    print("ok")
    r = yield from hello(loop)
    print("okok");



loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(test(loop))
#loop.close()


