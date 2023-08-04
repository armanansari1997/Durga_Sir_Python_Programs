def f1(x, *y):
    print(x)
    for y1 in y:
        print(y1)


# f1(10, 20, 30, 40)
f1(10)


# factorial of a number
def factorial(n):
    if n == 0:
        result = 1
    if n >= 1:
        result = n * factorial(n - 1)
    return result


print(factorial(4))  # 24
print(factorial(6))  # 720
print(factorial(7))  # 5050
