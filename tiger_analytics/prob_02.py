# Factorial of a number in different ways

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


n = 5
result = fact(n)
print(f'The factorial of {n} is', result)
