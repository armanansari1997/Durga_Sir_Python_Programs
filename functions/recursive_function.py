# Factorial of a given number
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result


print('Factorial is :', factorial(5)) # Factorial is : 120
print('Factorial is :', factorial(6)) # Factorial is : 720