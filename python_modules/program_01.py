# WAP to generate 6 digit random number, which can be used as OTP
from random import *

print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), sep='')

# Recommended way
otp = ''
for i in range(6):
    otp += str(randint(0, 9))
print('OTP is :', otp)

# Wrong logics:
print(randint(000000, 999999))
print(randint(100000, 999999))
