
def doubledecor(func):
    def inner():
        x=func()
        return x*22
    return inner
@doubledecor
def num():
    return 10

x=num()
print(x)