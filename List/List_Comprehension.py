if __name__ == '__main__':
    # create a list of no's from 1 to 10
    l = [x for x in range(1, 11)]
    print(l)

    # create a list with square value from 1 to 10
    l = [x * x for x in range(1, 11)]
    print(l)

    # creation of list 2 power(1 to 5)
    l = [2 ** x for x in range(1,6)]
    print(l)

    # creation of list from 1 to 100 which are divisible by 10
    l = [x for x in range(1,101) if x % 10 == 0]
    print(l)

    # create a list with elements present in l1 but not in l2
    l1 = [10,20,30,40]
    l2 = [30,40,50,60]
    l = [x for x in l1 if x not in l2]
    print(l)

    # create a list elements present in both l1 and l2
    l = [x for x in l1 if x in l2]
    print(l)

    # Prgm - 1
    # input: ['Balaiah','Nag','Venki','Chiru']
    # Output: ['B','N','V','C']

    l = ['Balaiah','Nag','Venki','Chiru']
    out = [ch[0] for ch in l]
    print(out)

    # Prgm - 2
    s = 'the quick brown fox jumps over the lazy dog'
    words = s.split()
    l = [[word.upper(),len(word)] for word in words]
    print(l)






