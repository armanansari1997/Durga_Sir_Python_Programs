def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


num = -1
if num < 0:
    print('wrong input')
else:
    res = fact(num)
    print(res)
