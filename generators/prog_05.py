# Fibonacci series from 0 to less than or equal to 10

def get_fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


g = get_fib_generator()


for x in g:
    if x <= 10:
        print(x)
    else:
        break
# O/p:
# 0
# 1
# 1
# 2
# 3
# 5
# 8


