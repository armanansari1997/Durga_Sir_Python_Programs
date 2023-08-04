if __name__ == '__main__':
    d = {100: 'durga', 200: 'Ravi', 100: 'Arman'}
    print(d)

    d = {}
    d = dict()
    print(d)

    l = [(100, 'A'), (200, 'B'), (300, 'C'), (400, 'D')]
    d = dict(l)
    print(d)

    # d = eval(input('Enter a dictionary'))
    # print(type(d))
    # print(d)

    # How to access data from dictionary
    d = {100: 'Durga', 200: 'Ravi', 300: 'Shiva'}
    print(d[100])
    print(d[300])
    # print(d[700]) # KeyError: 700

    # How to prevent KeyError
    # d = {100: 'Durga', 200: 'Ravi', 300: 'Shiva'}
    # key = int(input('Enter a key to search value'))
    # if key in d:
    #     print('The specified value is:',d[key])
    # else:
    #     print('The specified key is not available')

    # How to add/Update data to dict
    d = {100: 'Durga', 200: 'Ravi', 300: 'Shiva'}
    d[400] = 'Arman'
    d[100] = 'Durga_Updated'
    print(d)  # {100: 'Durga_Updated', 200: 'Ravi', 300: 'Shiva', 400: 'Arman'}

    # How to delete data from dict
    d = {100: 'Durga', 200: 'Ravi', 300: 'Shiva'}
    del d[100]
    print(d)  # {200: 'Ravi', 300: 'Shiva'}
    # delete multiple data at once
    del d[200], d[300]
    print(d)  # {}

    # WAP to enter name and marks into a dictionary and display information on the sources
    # n = int(input('Enter number of student:'))
    # d = {}
    # for i in range(n):
    #     name = input('Enter name of the student:')
    #     marks = int(input('Enter marks of the student:'))
    #     d[name] = marks
    # print(d)
    # print('*' * 30)
    # print('NAME','\t\t','MARKS')
    # print('*' * 30)
    # for k in d:
    #     print(k,'\t\t',d[k])

    # Equality Operator
    d1 = {100: 'A', 200: 'B'}
    d2 = {300: 'C', 400: 'D'}
    d3 = {200: 'B', 100: 'A'}
    print(d1 == d2)  # False
    print(d1 != d2)  # True
    print(d1 == d3)  # True
    print(d1 != d3)  # False

    # Membership Opertor(according to key)
    d1 = {100: 'A', 200: 'B'}
    print(100 in d1)  # True
    print(200 in d1)  # True
    print('A' in d1)  # False
    print('A' not in d1)  # True

    d = {100: 'A', 200: 'B', 300: 'C'}
    print(len(d))  # 3

    print(d.get(100))  # A
    print(d.get(700))  # None

    # Usinf default value
    print(d.get(300, 'Guest'))  # C
    print(d.get(700, 'Guest'))  # Guest
    print(d.get(999, 0))  # 0

    # update():
    d1 = {100: 'A', 200: 'B'}
    d2 = {300: 'C', 400: 'D'}
    d1.update(d2)
    print(d1)  # {100: 'A', 200: 'B', 300: 'C', 400: 'D'}

    # keys():
    d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    k = d.keys()
    print(k)  # dict_keys([100, 200, 300, 400])
    for key in k:
        print(key)

    # values():
    d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    v = d.values()
    print(v)  # dict_values(['A', 'B', 'C', 'D'])
    for value in v:
        print(value)

    # items():
    d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    i = d.items()
    print(i)  # dict_items([(100, 'A'), (200, 'B'), (300, 'C'), (400, 'D')])
    for item in i:
        print(item)
    for k, v in d.items():
        print(k, '....', v)

    # WAP to get value from the dictionary for the given key
    # d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    # k = int(input('Enter a key to get value'))
    # if k in d:
    #     print(d[k])
    # else:
    #     print('The specified key is not available')

    # WAP to get keys from the dictionary for the given value
    # d = {100: 'A', 200: 'A', 300: 'A', 400: 'D'}
    # value = input('Enter a value to find key')
    # available = False
    # for k,v in d.items():
    #     if value == v:
    #         print('The corresponding key is:', k)
    #         available = True
    # if not available:
    #     print('The specified key is not found')

    # pop(key):
    d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    print(d.pop(300))  # C
    print(d)  # {100: 'A', 200: 'B', 400: 'D'}
    # print(d.pop(700)) # KeyError: 700

    # pop(key,default_value):
    d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    print(d.pop(400, 'Guest'))  # D
    print(d.pop(700, 'Guest'))  # Guest

    # popitem():
    d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    print(d.popitem())  # (400, 'D')
    print(d.popitem())  # (300, 'C')
    print(d.popitem())  # (200, 'B')
    print(d.popitem())  # (100, 'A')
    print(d)  # {}
    # print(d.popitem()) # KeyError: 'popitem(): dictionary is empty'

    # clear():
    d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    print(d)  # {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    d.clear()
    print(d)  # {}

    # setdefault(key,value):
    d = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    print(d.setdefault(500, 'E'))  # E
    print(d)  # {100: 'A', 200: 'B', 300: 'C', 400: 'D', 500: 'E'}
    print(d.setdefault(100, 'Durga'))  # A
    print(d)  # {100: 'A', 200: 'B', 300: 'C', 400: 'D', 500: 'E'}

    # copy(): Means Cloning
    d1 = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    d2 = d1.copy()
    del d1[100]
    print(d1)  # {200: 'B', 300: 'C', 400: 'D'}
    print(d2)  # {100: 'A', 200: 'B', 300: 'C', 400: 'D'}

    # Aliasing
    d1 = {100: 'A', 200: 'B', 300: 'C', 400: 'D'}
    d2 = d1
    del d1[200]
    print(d1)  # {100: 'A', 300: 'C', 400: 'D'}
    print(d2)  # {100: 'A', 300: 'C', 400: 'D'}

    # WAP to take dictionaries from the keyboard and print sum of values
    # d = eval(input('Enter a dictionary'))
    # sum_of_values = 0
    # for v in d.values():
    #     sum_of_values += v
    # print('The sum of values:', sum_of_values)
    # print('Using Built-in method:', sum(d.values()))

    # WAP to find the number of occurrences of each letter present in the given string
    # word = input('Enter a word')
    # d ={}
    # for ch in word:
    #     d[ch] = d.get(ch,0) + 1
    # print(d)

    # WAP to find the number of occurrences of each vowel present in the given string
    # word = input('Enter a word')
    # vowels = {'a', 'e', 'i', 'o', 'u'}
    # d = {}
    # for ch in word:
    #     if ch in vowels:
    #         d[ch] = d.get(ch, 0) + 1
    # print(d)

    # Dictionary Comprehension

    # eg-1
    d = {x: x * x for x in range(1, 6)}
    print(d)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # eg-2
    d = {x: 2 ** x for x in range(1, 6)}
    print(d)  # {1: 2, 2: 4, 3: 8, 4: 16, 5: 32}

    # set merging:
    s1 = {100, 200}
    s2 = {300, 400}
    # s3 = s1 + s2 # TypeError: unsupported operand type(s) for +: 'set' and 'set'
    s3 = {*d1, *d2}
    print(s3)  # {400, 100, 300}

    # dict merging
    d1 = {100: 'A', 200: 'B'}
    d2 = {300: 'C', 400: 'D'}
    d3 = {**d1, **d2}
    print(d3)  # {100: 'A', 200: 'B', 300: 'C', 400: 'D'}

    # list inside dictionary:
    # d = {[10,20]:'Arman'}
    # print(d) # TypeError: unhashable type: 'list'
    d = {'Arman': [10,20]}
    print(d) # {'Arman': [10, 20]}

    # tuple inside dictionary as ky is possible
    d = {(10,20):'Arman'}
    print(d) # {(10, 20): 'Arman'}

    # list and set are unhashable type
    # d = {{'A', 'B'} : 20}
    # print(d) # TypeError: unhashable type: 'set'
    d = {'A' : {10,20}}
    print(d) # {'A': {10, 20}}

    # tuple as key and value both is possible
    d = {(10,20):(30,40)}
    d = {(10,20): (30,40)}
    print(d) # {(10, 20): (30, 40)}




