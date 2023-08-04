def smart_division(func):
    def inner(a, b):
        if b == 0:
            print('Hello stupid, How we can divide with zero')
        else:
            func(a, b)
    return inner


@smart_division
def division(a, b):
    print(a/b)


division(10, 2)  # 5.0
division(5, 0)  # Hello stupid, How we can divide with zero



