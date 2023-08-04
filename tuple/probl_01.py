tup1 = (1, 2, 3, 4)
tup2 = 3, 4, 6, 7, 8
print(id(tup1), ':', tup1)  # 1941795692656 : (1, 2, 3, 4)
print(id(tup2), ':', tup2)  # 1941790880720 : (3, 4, 6, 7, 8)

tup1 = tup1 + tup2  # Here a new tuple object is created
print(id(tup1), ':', tup1)  # 1941795459184 : (1, 2, 3, 4, 3, 4, 6, 7, 8)

# 2nd way of concatenate 2 tuples:
tup1 = (*tup1, *tup2)  # correct
tup1 = *tup1, *tup2  # correct
print(id(tup1), ':', tup1)  # 1822803041696 : (1, 2, 3, 4, 3, 4, 6, 7, 8, 3, 4, 6, 7, 8)

# we will get different result using this way :
t1 = 10, 20, 30, 40
t2 = 20, 40, 60
t1 = (t1, t2)  # correct
# t1 = t1, t2  # correct
print(id(t1), ':', t1)  # 1783784657600 : ((10, 20, 30, 40), (20, 40, 60))

# Note :-
# tup1[0] = 20 # TypeError: 'tuple' object does not support item assignment
# tup1[0] = 20, 20  # TypeError: 'tuple' object does not support item assignment
