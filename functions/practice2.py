def calculate(a, b):
    print(a + b)
    print(a * b)
    print(a // b)


# calculate(10, 20)
# calculate(20, 10)

# WAF to accept 2 numbers as input and return sum?
def add(a, b):
    sum_v = a + b
    return sum_v


result = add(10, 20)
print(result)  # 30


def add(a, b):
    print(a + b)


result = add(10, 50)
print(result)  # 60 None


# Factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


print(factorial(5))
print(factorial(6))

for i in range(1, 6):
    print(factorial(i))


# Returning multiple values from a function
def sum_sub(a, b):
    sum = a + b
    sub = a - b
    return sum, sub


x, y = sum_sub(40, 30)
print(x)  # 70
print(y)  # 10

print(sum_sub(10, 20))  # (30, -10)


def calc(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div


t = calc(10, 20)
print(type(t))  # <class 'tuple'>
print(t)  # (30, -10, 200, 0.5)


# for x in t:
#     print(x)


# 1) positional argument
def sub(a, b):
    result = a - b
    print(result)


sub(10, 20)  # -10


# sub(10) # TypeError: sub() missing 1 required positional argument: 'b'


# 2) Keyword argument
def sub(a, b):
    print(a - b)


sub(200, 100)  # 100
sub(a=100, b=200)  # -100
sub(a=200, b=100)  # 100
sub(100, b=200)  # -100


# sub(a=200,100) # SyntaxError:
# sub(100, a=200) # TypeError: sub() got multiple values for argument 'a'


# 3) default argument
def wish(name='Guest'):
    print('Hello', name, 'Good Evening')


wish()  # Hello Guest Good Evening
wish('Arman')  # Hello Arman Good Evening


# function defination syntax
def wish(name, msg):
    pass


def wish(name='Guest', msg='Good Evening'):
    pass


def wish(name, msg='Good Evening'):
    pass


# def wish(name='Guest',msg): # SyntaxError: Invalid Syntax
#     pass

# Note: Default argument must be at last


# 4) variable length arguments:
def f1(*n):
    print('variable length argument function')


f1()  # variable length argument function
f1(10)  # variable length argument function
f1(100, 200, 300)  # variable length argument function


def f1(*n):
    print(type(n))
    print(n)


f1()  # <class 'tuple'>
# ()
f1(10, 20, 30)  # <class 'tuple'>


# (10, 20, 30)


def sum(*n):
    total = 0
    for x in n:
        total += x
    print('The Sum: ', total)


sum(10, 20)  # The Sum:  30
sum(10, 20, 30)  # The Sum:  60
sum(10, 20, 30, 40, 50)  # The Sum:  150


def f1(*n):
    print(n)


f1()
f1(20)  # (20,)
f1(10, 20)  # (10, 20)
f1((10, 20, 30))  # ((10, 20, 30),)
f1((10, 20, 30), (40, 50, 60))  # ((10, 20, 30), (40, 50, 60))


def f1(x, *y):
    print(x)
    for y1 in y:
        print(y1)


f1(10, 20)
f1(10, 20, 30, 40)
f1(10)


def f(*x, y):
    print(x, end=' and ')
    print('y:', y)


# f(10,20,30,40) # TypeError: f() missing 1 required keyword-only argument: 'y'
f(10, 20, 30, y=40)  # (10, 20, 30) and y: 40


# def f1(*x,*y): # SyntaxError : Invalid Syntax
#     print(x,y)


# **kwargs
def f1(**kwargs):
    print(kwargs)


f1()  # {}
f1(name='Arman', Roll_num=2890)  # {'name': 'Arman', 'Roll_num': 2890}


def f1(*args, **kwargs):
    print(args, end=' and ')
    print(kwargs)


f1(10, 20, A=40, B=50)  # (10, 20) and {'A': 40, 'B': 50}


# def f1(**kwargs, *args): # SyntaxError : Invalid Syntax
#     print(**args,end=' and ')
#     print(*args)


def f1(*y, x=10):
    print(y, end=' and ')
    print(x)


f1(30)  # (30,) and 10
f1(30, 40)  # (30, 40) and 10
f1(30, 40, 50, x=100)  # (30, 40, 50) and 100


def f1(arg1, arg2, arg3=4, arg4=8, ):
    print(arg1, arg2, arg3, arg4)


f1(10, 20)  # 10 20 4 8
f1(10, 20, 30, 40)  # 10 20 30 40
f1(25, 50, arg4=100)  # 25 50 4 100
f1(arg4=2, arg1=3, arg2=4)  # 3 4 4 2
# f1() # TypeError: f1() missing 2 required positional arguments: 'arg1' and 'arg2'
# f1(arg3=10,arg4=20,30,40) # SyntaxError: positional argument follows keyword argument
# f1(4, 5, arg2=10)  # TypeError: f1() got multiple values for argument 'arg2'
# f1(4,5,arg3=5,arg5=10) # TypeError: f1() got an unexpected keyword argument 'arg5'
