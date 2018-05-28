import asyncio


async def other():
    i=yield asyncio.sleep(1)

a=other();

print(a)
print(next(a))
#print(next(next(a)))


'''
async def hello():
    print("Hello world!")
    r = await other()
    print("Hello again!"+str(r))




async def hello1():
    print("Hello1 world!")
    r = await asyncio.sleep(1)
    print("Hello1 again!"+str(r))

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine


tasks = [hello(), hello1()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''


