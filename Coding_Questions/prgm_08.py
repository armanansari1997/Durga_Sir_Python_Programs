# Create a generator for generating infinite number

def generator():
    count = 0
    while True:
        yield count
        count += 1


g = generator()

# Infinite loop
# for i in g:
#     print(i)

# print one by one
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # 4
print(next(g))  # 5
