# Fibonacci numbers

def get_fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


g = get_fib_generator()

print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # 5
print(next(g))  # 8
print(next(g))  # 13
print(next(g))  # 21


# for x in g:
#     print(x)
# O/p : Infinite loop

