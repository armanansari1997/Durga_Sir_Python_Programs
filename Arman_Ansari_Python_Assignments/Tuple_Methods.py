if __name__ == '__main__':

    t = 12345, 54321, 'hello!'  # This is a tuple initialization
    print(t[0])  # 12345
    print(type(t))  # <class 'tuple'>

    u = t, (1, 2, 3, 4, 5)  # Tuples may be nested:
    print(u)    # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

    # t[0] = 88888  # TypeError: 'tuple' object does not support item assignment

    v = ([1, 2, 3], [3, 2, 1])  # # but they can contain mutable objects:
    print(v)

    #---------------------------------------------------------------#

    empty = ()
    singleton = 'hello',
    print(len(empty))   # 0

    print(len(singleton)) # 1

    print(singleton) # ('hello',)

