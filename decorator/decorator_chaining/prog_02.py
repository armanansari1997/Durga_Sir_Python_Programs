def decor1(func):
    def inner1():
        x = func()
        return x * x

    return inner1


def decor2(func):
    def inner2():
        x = func()
        return 2 * x

    return inner2


# eg-01
def num():
    return 20


print(num())  # 20


# eg-02
@decor1
def num():
    return 20


print(num())  # 400


# eg-03
@decor2
def num():
    return 20


print(num())  # 40


# eg-04
@decor2
@decor1
def num():
    return 20


print(num())  # 800


# eg-05
@decor1
@decor2
def num():
    return 20


print(num())  # 1600
