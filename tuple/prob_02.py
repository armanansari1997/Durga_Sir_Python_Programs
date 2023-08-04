# Tuple object methods :
tup = 1, 1, 1, 2, 2, 3, 4, 5, 6, 6

print(tup.index(1))  # 0
print(tup.index(3))  # 5
# print(tup.index(100))  # ValueError: tuple.index(x): x not in tuple

print(len(tup))  # 10

print(tup.count(1))  # 3
print(tup.count(4))  # 1
print(tup.count(6))  # 2
print(tup.count(100))  # 0
