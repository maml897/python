def log(func):
    print(func)
    def a(*args, **kw):
        print('call %s():' % func.__name__)

        for i in args:
            print(i);

        return func(*args, **kw)
    return a


#@log
def now(*a,b):
    print('2015-3-25:'+str(a))


#now(6666,589);

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


print("======================================")

f=fab(5);
print(f);
print(next(f));
print(next(f));

print( [ x for x in fab(5)] )
print (x for x in fab(5))

print("======================================")

r = range (3);
print ([x for x in r])
print (x for x in r)

print("======================================")

r1 = [0,1,2]
print (x for x in r1)
print ([x for x in r1])

g=(x for x in r1)
print(next(g))
print(next(g))
print(next(g))

g1=[x for x in r1];
print(g1)


print("======================================")

'''
def g1(x):
     yield  range(x)
def g2(x):
     yield  from range(x)

it1 = g1(5)
it2 = g2(5)


print( [ x for x in it1] )
#out [range(0, 5)]

print( [ x for x in it2] )
#out [0, 1, 2, 3, 4]
'''
