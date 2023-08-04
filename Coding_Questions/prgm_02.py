# tuple is immutable

t1 = 10, 20, 30, 40
t2 = 50, 60, 70, 40
print(id(t1))
print(id(t2))
t1 = t1 + t2
t3 = t1
print(t1)
print(id(t1))
print(id(t3))
