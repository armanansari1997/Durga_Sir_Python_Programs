def decor(func):
    def inner(name):
        names = ['CM', 'PM', 'Minister']
        if name in names:
            print('#' * 30)
            func(name)
            print('#' * 30)
        else:
            func(name)
    return inner


@decor
def wish(name):
    print('Good evening', name)


wish('Arman')  # Good evening Arman
wish('Sunny')  # Good evening Sunny
wish('CM')
# Output:
# Good evening Arman
# Good evening Sunny
# ##############################
# Good evening CM
# ##############################


