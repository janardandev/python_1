
def decor2(func):
    def inner2():
        x=func()
        return x*x
    return inner2

def decor1(func):
    def inner1():
        x=func()
        return x*2
    return inner1

@decor2
@decor1
def num():
    return 10

x=num()
print(x)