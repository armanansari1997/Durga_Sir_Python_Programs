def decor1(func):
    def inner1():
        print('Decorator1 Execution')

    return inner1


def decor2(func):
    def inner2():
        print('Decorator2 Execution')

    return inner2


@decor2
@decor1
def f1():
    print('Original function')


f1()  # Decorator2 Execution

'''what if we change the order of decorator'''


@decor1
@decor2
def f1():
    print('Original function')


f1()  # Decorator1 Execution
