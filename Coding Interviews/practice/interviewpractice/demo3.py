def fact(n):
    if n <= 1:
        return n
    else:
        return n * fact(n-1)


num = 1
if num < 1:
    print('Wrong Input')
else:
    print(fact(num))

