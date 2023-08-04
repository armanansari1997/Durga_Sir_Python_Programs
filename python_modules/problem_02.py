# WAP to generate random password of 6 length where 1,3,5 characters are alphabet symbols
# and 2, 4, 6 characters are digits

from random import *
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
print(choice(alphabets), choice(digits), choice(alphabets), choice(digits), choice(alphabets), choice(digits))
print(choice(alphabets), choice(digits), choice(alphabets), choice(digits), choice(alphabets), choice(digits), sep='')


# Recommended way
pwd = ''
for i in range(6):
    if i % 2 == 0:
        pwd += choice(alphabets)
    else:
        pwd += choice(digits)
print(pwd)