def decor(func):
    def inner(name):
        if name == 'Sunny':
            print('#' * 30)
            func(name)
            print('#' * 30)
        else:
            func(name)
    return inner


@decor
def wish(name):
    print('Good evening', name)


wish('Arman')
wish('Sunny')
# Output:


