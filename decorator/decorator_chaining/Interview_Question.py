def decor1(func):
    def inner1():
        print('Decorator1 Execution')
    return inner1


def decor2(func):
    def inner2():
        print('Decorator2 Execution')
        f1()  # recursion will happen here
    return inner2


@decor2
@decor1
def f1():
    print('Original Function')


f1()  # RecursionError: maximum recursion depth exceeded while calling a Python object

