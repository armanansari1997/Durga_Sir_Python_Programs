# Problem -01

# def my_func(*args, **kwargs):
#     c = kwargs.get('my_dictionary')
#     c['a'] = 3
#     c['p'] = 4
#     print(c)
#
#
# def my_func_2():
#     c = {'p': 1, 'q': 2}
#     my_func(my_dictionary=c)
#     print(c)
#
#
# my_func_2()

# Output:
# {'p': 4, 'q': 2, 'a': 3}
# {'p': 4, 'q': 2, 'a': 3}


# problem -02

def my_func(*args, **kwargs):
    c = kwargs.get('my_dictionary')
    c = {k: v for k, v in c.items()}
    c['a'] = 3
    c['p'] = 4
    print(c)


def my_func_2():
    c = {'p': 1, 'q': 2}
    my_func(my_dictionary=c)
    print(c)


my_func_2()

# Output:
# {'p': 4, 'q': 2, 'a': 3}
# {'p': 1, 'q': 2}


