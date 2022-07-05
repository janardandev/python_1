def decor(func):
    def inner():
        print("I am decor function")
    return inner



@decor
def display():
    print("i am original display function")
display()