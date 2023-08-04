if __name__ == '__main__':

    # equality operator
    s1 = {10, 20, 30}
    s2 = {10, 20, 30}
    print(s1 == s2)  # True
    print(s1 != s2)  # False

    # Relational Operator
    s1 = {10, 20, 30}
    s2 = {20, 10, 5, 6, 7}
    print(s1 < s2)  # False
    print(s1 <= s2)  # False
    print(s1 > s2)  # False
    print(s1 >= s2)  # False

    # membership operator
    s = {10, 20, 30, 40}
    print(10 in s)  # True
    print(50 in s)  # False
    print(50 not in s)  # True

    # len()
    s = {10, 20, 30, 40, 10}
    print(s)  # {40, 10, 20, 30} Order we don't know
    print(len(s))  # 4

    # add()
    s.add(600)
    print(s)  # {40, 10, 20,600, 30} Order we don't know
    s.add(999)
    print(s)  # {999, 40, 10, 20, 600, 30} Order we don't know
    # s.add(10,20,30,40) # TypeError: set.add() takes exactly one argument (4 given)

    # update() - To add multiple items into set
    s = {10, 20}
    l = [30, 40]
    s.update(l)
    print(s)  # {40, 10, 20, 30} Order we don't know
    s.update(range(1, 6))
    print(s)  # {1, 2, 3, 4, 5, 40, 10, 20, 30} Order we don't know
    # s.update(100) # TypeError: 'int' object is not iterable
    s.update(range(8, 13), range(15, 19))
    print(s)  # {1, 2, 3, 4, 5, 40, 8, 10, 9, 11, 12, 15, 16, 17, 18, 20, 30} Order we don't know

    # remove()
    s = {10, 20, 30, 40}
    s.remove(30)
    print(s)  # {40, 10, 20} Order we don't know
    # s.remove(50) # KeyError: 50
    print(s)

    # discard()
    s = {10, 20, 30, 40}
    s.discard(30)
    print(s)  # {40, 10, 20} Order we don't know
    s.discard(50)  # No Error will come if element is not present in set
    print(s)  # {40, 10, 20}

    # pop()
    s = {10, 20, 30, 40}
    print(s.pop())  # 40 Element we don't know
    print(s.pop())  # 10 Element we don't know
    print(s.pop())  # 20 Element we don't know
    print(s.pop())  # 30 Element we don't know
    print(s)  # set()
    # print(s.pop()) # KeyError: 'pop from an empty set'

    # clear()
    s = {10, 20, 30, 40}
    print(s)  # {40, 10, 20, 30} Order we don't know
    s.clear()
    print(s)  # set()

    # union() or |
    s1 = {10, 20, 30, 40}
    s2 = {30, 40, 50, 60}
    s3 = s1.union(s2)
    s4 = s1 | s2  # using union operator
    print(s3)  # {40, 10, 50, 20, 60, 30} Order we don't know
    print(s4)  # {40, 10, 50, 20, 60, 30} Order we don't know

    # intersection() or &
    s1 = {10, 20, 30, 40}
    s2 = {30, 40, 50, 60}
    s3 = s1.intersection(s2)
    s4 = s1 & s2  # using intersection operator
    print(s3)  # {40, 30} Order we don't know
    print(s4)  # {40, 30} Order we don't know

    # difference() or -
    s1 = {10, 20, 30, 40}
    s2 = {30, 40, 50, 60}
    s3 = s1.difference(s2)
    s4 = s1 - s2
    print(s3)  # {10, 20} Order we don't know
    print(s4)  # {10, 20} Order we don't know

    # symmetric_difference()
    s1 = {10, 20, 30, 40}
    s2 = {30, 40, 50, 60}
    s3 = s1.symmetric_difference(s2)
    s4 = s1 ^ s2
    print(s3)  # {10, 50, 20, 60} Order we don't know
    print(s4)  # {10, 50, 20, 60} Order we don't know

    # Aliasing
    s1 = {10, 20, 30, 40}
    s2 = s1  # it refers the same object
    s1.pop()
    print(s1)  # {10, 20, 30} Order we don't know
    print(s2)  # {10, 20, 30} Order we don't know

    # cloning
    s3 = s1.copy()  # a new object will be created
    print(s3)  # {10, 20, 30} Order we don't know

    # set comprehension
    # eg-1
    s = {x * x for x in range(1, 6)}
    print(type(s))  # <class 'set'>
    print(s)  # {1, 4, 9, 16, 25} # Order we don't know

    # eg-2
    s = {2 ** x for x in range(1, 6)}
    print(s)  # {32, 2, 4, 8, 16} Order we don't know

    # WAP to remove duplicate elements from list
    l = [10, 20, 30, 40, 10, 20, 30]
    s = set(l)  # converting list into set
    print(s)  # {40, 10, 20, 30} Order we don't know
    l1 = list(s)  # converting set into list
    print(l1)  # [40, 10, 20, 30]

    # using 2nd way
    l = [10, 10, 20, 30, 40, 10, 20, 30]
    l1 = []
    for x in l:
        if x not in l1:
            l1.append(x)
    print(l1)  # [10, 20, 30, 40]

    word = input('Enter any word to search for vowel')
    s = set(word)
    v = {'a','e','i''o','u'}
    result = s & v
    print(result)

