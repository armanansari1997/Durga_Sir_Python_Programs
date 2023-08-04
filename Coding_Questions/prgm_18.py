s = 'python'
size = len(s)
for row in range(size):
    for col in range(row+1):
        print(s[col], end=' ')
    print()

# Output:

# p
# p y
# p y t
# p y t h
# p y t h o
# p y t h o n


# problem - 02

# s = 'python'
# size = len(s)
# for row in range(size):
#     for col in range(row+1):
#         print(s[row], end=' ')
#     print()

# Output:

# p
# y y
# t t t
# h h h h
# o o o o o
# n n n n n n
