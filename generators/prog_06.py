# First 'n' Fibonacci series (from 0 to less than or equal to 10)

def get_fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


g = get_fib_generator()

n = int(input('Enter how many number of fibonacci series you want '))
count = 1
while count <= n:
    print(next(g))
    count += 1

# O/p: (If n value is 10)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


