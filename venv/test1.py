import inspect

def simple_coroutine(a):
    print('-> coroutine 100')    # yield 在表达式中使用；如果协程只需要从客户那里接收数据，yield关键字右边不需要加表达式（yield默认返回None）
    yield 100

    print('-> coroutine 101')
    yield 101

    print('-> coroutine 102')
    yield 102


my_coro = simple_coroutine(10)# 和创建生成器的方式一样，调用函数得到生成器对象。

print(next(my_coro));
print("------------------------------");

print(next(my_coro));
print("------------------------------");


my_coro.send(10);

#print(next(my_coro));

