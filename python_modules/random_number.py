from random import *

fruits = ['Apple', 'Banana', 'Orange', 'Mango']
for i in range(10):
    print(choice(fruits))

alphabets = 'ABCDEFGHIJKLMNOPQRS'
for i in range(10):
    print(choice(alphabets))

numbers = '0123456789'
for i in range(10):
    print(choice(numbers))


for i in range(101):
    print(randint(1, 10))
