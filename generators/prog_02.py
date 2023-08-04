def my_gen():
    yield 'A'
    yield 'B'
    yield 'C'


g = my_gen()

# 1st way
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  # StopIteration


# 2nd way
for x in g:
    print(x)
