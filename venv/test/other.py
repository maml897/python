def greeting_conf(prefix):
    def greeting(name):
        print(prefix, name)
    return greeting


mGreeting = greeting_conf("Good Morning")

print(dir(mGreeting))
print(mGreeting.__closure__)
print(type(mGreeting.__closure__[0]))
print(mGreeting.__closure__[0].cell_contents)

 #在Python中，函数对象有一个__closure__属性，我们可以通过这个属性看看闭包的一些细节。

