def decor(func):
    def inner(a, b):
        return func(a, b)

    return inner


# 1:
def div(a, b):
    return a / b


result = decor(div)
print(result(10, 20))

# 2:
# @decor
# def div(a, b):
#     return a/b
#
#
# result = div(100, 40)
# print(result)
