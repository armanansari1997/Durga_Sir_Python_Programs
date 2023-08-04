#  Iterator

li = iter(['A', "B", 'C'])
print(next(li))
print(next(li))
print(next(li))
# print(next(li))

# Generator


def sqr(n):
    for i in range(1, n+1):
        yield i*i


a = sqr(3)
print(next(a))
print(next(a))
print(next(a))
# print(next(a))  # StopIteration

a = sqr(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a))  # StopIteration
