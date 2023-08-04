# way -01

# def fib(num):
#     a, b = 0, 1
#     for i in range(num):
#         print(a)
#         a, b = b, a+b
#
#
# fib(10)

# way -02 using recursion

def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


n_terms = 10

if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
    print(fib(i))

# way - 03 using generator

# def fib(num):
#     a, b = 0, 1
#     for i in range(num):
#         yield a
#         a, b = b, a+b
#
#
# result = fib(10)
#
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
#
# print("------------------------------------")
#
# for i in result:
#     print(i)
