# Nameless Function / Lambda Function
from functools import reduce

s = lambda n: n * n
print(s(4))  # 16
print(s(5))  # 25
print(s(10))  # 100

# eg-2
add = lambda a, b: a + b

print(add(10, 20))  # 30
print(add(50, 40))  # 90

# biggest of given 2 numbers
bigger = lambda a, b: a if a > b else b
print(bigger(10, 20))  # 20
print(bigger(30, 20))  # 30

# biggest of 3 given numbers
bigger = lambda a, b, c: a if a > b and a > c else b if b > c else c
print(bigger(10, 20, 30))  # 30
print(bigger(9, 8, 7))  # 9
print(bigger(80, 100, 90))  # 100

# Functions as argument to another function

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Even numbers
even = list(filter(lambda n: n % 2 == 0, l))
print('Even number list: ', even)

# Odd Numbers
odd = list(filter(lambda n: n % 2 != 0, l))
print('Odd number list :', odd)

# divisible by 3 and odd number
div_by_3_and_odd = list(filter(lambda n: n % 3 == 0 and n % 2 != 0, l))
print('divisible by 3 and odd number :', div_by_3_and_odd)

heroines = ['KatrinaKaif', 'KareenaKapoor', 'Anushka', 'Deepika', 'SunnyLeone', 'Mallika']
# print heroine names if heroines name starts with 'K' in a list
strats_with_k = list(filter(lambda name: name[0] == 'K', heroines))
print('first letter of heroines name list :', strats_with_k)

# name length divisible by 5
result = list(filter(lambda name: len(name) % 5 == 0, heroines))
print(result)  # ['SunnyLeone']

# print heroies name if name length is odd
name_length_is_odd = list(filter(lambda name: len(name) % 2 != 0, heroines))
print('Name length is Odd : ',
      name_length_is_odd)  # Name length is Odd :  ['KatrinaKaif', 'KareenaKapoor', 'Anushka', 'Deepika', 'Mallika']

# map() function:
l = [1, 2, 3, 4, 5]
# square of a number
squareit = list(map(lambda num: num * num, l))
print(squareit)  # [1, 4, 9, 16, 25]

# 2 power number 2^(1-5)
power = list(map(lambda num: 2 ** num, l))
print(power)  # [2, 4, 8, 16, 32]

# eg-1
l1 = [1, 2, 3, 4, 5]
l2 = [5, 10, 15, 20, 25]
l3 = list(map(lambda x, y: x * y, l1, l2))
print('Multiplication of l1 with l2 :', l3)  # Multiplication of l1 with l2 : [5, 20, 45, 80, 125]

# eg-2
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [5, 10, 15, 20, 25]
l3 = list(map(lambda x, y: x * y, l1, l2))
print('Remaining argument will be ignored: ', l3)  # Remaining argument will be ignored:  [5, 20, 45, 80, 125]

# eg-3
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
l3 = [1, 2, 3, 4, 5]
add = list(map(lambda x, y, z: x + y + z, l1, l2, l3))
print('The sum is : ', add)

# reduce() function:
l = [10, 20, 30, 40, 50]
result = reduce(lambda a, b: a + b, l)
# result = reduce(lambda n: n, l) # TypeError: <lambda>() takes 1 positional argument but 2 were given
print(result) # 150
