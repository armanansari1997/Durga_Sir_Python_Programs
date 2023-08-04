def decor1(func):
    def inner1():
        print('Decorator1 Execution')
        func()
    return inner1


def decor2(func):
    def inner2():
        print('Decorator2 Execution')
        func()
    return inner2


@decor2
@decor1
def f1():
    print('Original Function')


f1()

# Output:
# Decorator2 Execution
# Decorator1 Execution
# Original Function
