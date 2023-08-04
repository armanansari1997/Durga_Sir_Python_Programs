if __name__ == '__main__':
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    print(fruits.count('apple'))  # 2
    print(fruits.count('tangerine'))  # 0
    print(fruits.index('banana'))  # 3
    print(fruits.index('banana', 4))  # Find next banana starting a position 4   # 6

    fruits.reverse()
    print(fruits)  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

    fruits.append('grape')
    print(fruits)  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

    fruits.sort()
    print(fruits)  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

    # fruits.sort(reverse=True)
    # print(fruits) # ['pear', 'orange', 'kiwi', 'grape', 'banana', 'banana', 'apple', 'apple']

    fruits.pop()  # 'pear'
    print(fruits)  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

    fruits.insert(1, "Arman")
    print(fruits)  # ['apple', 'Arman', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

    squares = []
    for x in range(10):
        squares.append(x ** 2)
    print(squares)

    # more concise and readable
    squares = [x ** 2 for x in range(10)]
    print(squares)

    vec = [-4, -2, 0, 2, 4]
    # create a new list with the values doubled
    print([x * 2 for x in vec])

    # filter the list to exclude negative numbers
    filter = [x for x in vec if x >= 0]
    print(filter)

    # apply a function to all the elements
    print([abs(x) for x in vec])

    # create a list of 2-tuples like (number, square)
    print([(x, x ** 2) for x in range(6)])

    # the tuple must be parenthesized, otherwise an error is raised
    # print([x,x**2 for x in range(6)])

    # del keyword
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[1]
    print(a)
    del a[2:4]
    print(a)
    del a[:]
    print(a)
    # del can also be used to delete entire variables:
    del a

    a = ['apple', 'banana', 'grapes', 'pineapple']
    print(a)

    # 1) Copy a list
    b = a[:]
    print(b)

    # 2) Copy a list
    c = b[::]
    print(c)

    # 3) copy a list using built in method
    d = c.copy()
    print(d)

    # Reverse a List
    d.reverse()
    print(d)

    # Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
    d.extend('ABC')
    print(d)

    # list.clear will Remove all items from the list. Equivalent to del a[:].
    d.clear()
    print(d)
