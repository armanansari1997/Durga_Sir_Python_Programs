def decor(func):
    def inner(name):
        if name == 'Sunny':
            print('#' * 30)
            func(name)
            print('#' * 30)
        else:
            func(name)

    return inner


'''Calling same function with decorator'''


@decor
def wish(name):
    print('Good Evening', name)


# wish('Arman')  # Good Evening Arman
# wish('Durga')  # Good Evening Durga
# wish('Sunny')
# Output:
# Good Evening Arman
# Good Evening Durga
# ##############################
# Good Evening Sunny
# ##############################


'''Calling same function without using decorator'''


def wish(name):
    print('Good Evening', name)


'''Assigning the returned values by decor function into the decorated_wish'''
decorated_wish = decor(wish)

decorated_wish('Durga')
decorated_wish('Arman')
decorated_wish('Sunny')
