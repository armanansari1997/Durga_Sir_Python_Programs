# Fibonacci series using recursion

def fib_ser(n):
    if n <= 1:
        return n
    else:
        return fib_ser(n - 1) + fib_ser(n - 2)


n = 10
if n < 0:
    print('Invalid')
else:
    for i in range(n):
        print(fib_ser(i))
