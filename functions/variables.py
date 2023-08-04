# Global Variable and local variable

# 1)
a = 10


def f1():
    print(a)


def f2():
    print(a)


f1()  # 10
f2()  # 10

# 2)
def f1():
    a = 20
    print(a)


def f2():
    print(a)


f1() # 20
f2() # 10

# Need of global keyword
def f1():
    # print(a) # SyntaxError: name 'a' is used prior to global declaration
    global a
    a = 20
    print(a)


def f2():
    print(a)


f1() # 20
f2() # 20

a = 888


def f1():
    a = 999
    print(a) # 999
    print(globals()['a']) # 888
    print(globals().get('a')) # 888


f1()



