# A function can return another function

def outer():
    def inner():
        print('inner function execution')

    return inner


f1 = outer()
f1()  # inner function execution
f1()  # inner function execution
f1()  # inner function execution
f1()  # inner function execution
