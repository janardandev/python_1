def decor(func):
    def inner(x,y):
        print("the sum of {} and {}:".format(x,y),end='')
        func(x,y)
    return inner


@decor
def add(a,b):
    print(a+b)

add(10,30)