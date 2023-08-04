def fib_series(n):
    a, b = 0, 1
    i = 0
    while i < n:
        print(a)
        a, b = b, a+b
        i += 1


fib_series(10)


# def fib_series(n):
#     a, b = 0, 1
#     while True:
#         if a == 0:
#             return a
#         if b == 1:
#             return 1
#         elif b > 1:
#             return fib_series(a - b), fib_series(a + b)
#
#
# f = fib_series(10)
# print(f)
