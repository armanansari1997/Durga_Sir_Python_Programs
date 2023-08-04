# 1) fibonacci series using simple function
# 2) fibonacci series using recursion function
# 3) nth fibonacci using recursion function

# 1)
def fib_num(n):
    first, second = 0, 1
    for i in range(n):
        print(first)
        temp = first
        first = second
        second = temp + first


n = int(input('Enter how many numbers you want in this series : '))
fib_num(n)


# 2) print nth fibonacci number
def fibonacci(n):
    # if type(n) != int:
    #     raise TypeError('n must be a positive int')
    # if n < 1:
    #     raise ValueError('n must be a positive int')
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


print('---------------')
for i in range(n):
    print(fibonacci(i))


# 3)
# n = int(input('Enter the no'))
print('--------------')
print(f'{n}th Fibonacci number :', fibonacci(n))
