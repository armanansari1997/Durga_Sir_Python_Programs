if __name__ == '__main__':
    t = (10, 'durga', 20, 30)
    print(type(t)) # <class 'tuple'>

    t = 300, 'durga', 20, 30
    print(type(t)) # <class 'tuple'>

    print(t[0]) # 300
    print(t[-1]) # 30

    # t[0] = 777 # TypeError: 'tuple' object does not support item assignment
    # print(t)


    # Single Valued tuple
    t = (30)
    print(type(t)) # <class 'int'>
    print(t) # 30

    t = (30,)
    print(type(t)) # <class 'tuple'>
    print(t) # (30,)

    # empty tuple
    t = ()
    print(type(t)) # <class 'tuple'>

    # Invalid tuples are:
    t = (10)
    t = 10

    # Valid tuples are:
    t = ()
    t = (10,)
    t = 10,
    t = (10,20,30)
    t = 10,20,30
    t = (10,20,30,)
    t = 10,20,30,

    # By using tuple() function
    l = [10,20,30]
    t = tuple(l)
    print(t)

    t = tuple(range(1,11,2))
    print(t) # (1, 3, 5, 7, 9)

    t = tuple('durga')
    print(t) # ('d', 'u', 'r', 'g', 'a')

    # With dynamic input:
    # t = eval(input('Enter tuple of values'))
    # print(type(t)) # <class 'tuple'>
    # print(t)

    # equality operator
    s1 = {10,20,30}
    s2 = {10,20,30}
    print(s1 == s2)
    print(s1 != s2)

    # Relational Operator
    s1 = {10, 20, 30}
    s2 = {20, 10, 5,6,7}
    print(s1 < s2) # False
    print(s1 <= s2) # False
    print(s1 > s2) # False
    print(s1 >= s2) # False

    # membership operator
    s = {10,20,30,40}
    print(10 in s) # True
    print(50 in s) # False
    print(50 not in s) # True
















