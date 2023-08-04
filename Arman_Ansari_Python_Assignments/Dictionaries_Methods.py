import math

if __name__ == '__main__':
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    print(tel)
    print(tel['jack'])  # 4098
    tel['']='null'
    tel['']='null'
    print(tel)

    print(tel.items()) # dict_items([('jack', 4098), ('sape', 4139), ('guido', 4127), ('', 'null')])

    print(tel.keys()) # dict_values([4098, 4139, 4127, 'null'])

    print(tel.values()) # dict_keys(['jack', 'sape', 'guido', ''])

    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k,v in knights.items():
        print(k,v)
    # o/p : gallahad the pure
    #       robin the brave

    print(knights.get('gallahad')) # the pure
    print(knights.get('arman'))  # None

    #-----------------------------------------------------#

    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i,v)
    # o/p : 0 tic
    #       1 tac
    #       2 toe

    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q,a in zip(questions, answers):
        print('What is your {0}? It is {1}'.format(q,a))
        # print(f'what is your {q}? It is {a}.')

    # O/p : What is your name?  It is lancelot.
    #       What is your quest?  It is the holy grail.
    #       What is your favorite color?  It is blue.

    for i in reversed(range(1,10,2)):
        print(i)

    # O/p : 9
    #       7
    #       5
    #       3
    #       1

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for i in sorted(basket):
        print(i)

    # O/p : apple
    #       apple
    #       banana
    #       orange
    #       orange
    #       pear

    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for i in sorted(set(basket)):
        print(i)

    # A set of elements we will get but order we don't know
    # apple
    # banana
    # orange
    # pear

    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)

    print(filtered_data) # [56.2, 51.7, 55.3, 52.5, 47.8]
