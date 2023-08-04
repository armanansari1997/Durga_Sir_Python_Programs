if __name__ == '__main__':
    l = []
    print(type(l))
    l.append(10)
    l.append(20)
    l.append(30)
    l.append('Arman')
    l.append(True)
    l.append(10)
    print(l)

    # List is Mutable
    l[0] = 7777
    print(l)

    # l = eval(input('Enter a list of numbers'))
    # print(l)

    l2 = [10, 20, 30, 40]
    print(l2)  # [10,20,30,40]

    l3 = list('durga')
    print(l3)  # ['d', 'u', 'r', 'g', 'a']

    l4 = list(range(0, 10, 2))
    print(l4)

    l4 = list(('durga', 'soft'))
    print(l4)  # ['durga', 'soft']

    l = 'Learning Python is very easy'
    l = l.split()
    print(l)

    # Accessing Elements of List
    l = [10, 20, 30, 40]
    print(l[0])
    print(l[-1])
    # print(l[100]) # IndexError: list index out of range

    # Using Slicing
    l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(l[2:7])
    print(l[2:7:2])
    print(l[8:2:-2])  # [90, 70, 50]
    print(l[4:100])  # [50,60,70,80,90,100]
    print(l[4:0:2])  # []

    # Traversing Elements of list
    i = 0
    while i < len(l):
        print(l[i])
        i += 1
    # Using For Loop
    print('Using For Loop')
    for x in l:
        print(x)
    # Only Even no's
    print('Only Even')
    for x in range(2, len(l), 2):
        print(x)

    # Print elements of List index wise
    l = [10, 20, 30, 40, 50, 60]
    i = 0
    while i < len(l):
        print('The element present at +ve index :{} and -ve index :{} is : {}'.format(i, i - len(l), l[i]))
        i += 1

    # Mathematical Operators for list
    l1 = [10, 20, 30]
    l2 = [40, 50, 60]
    l3 = l1 + l2
    print(l3)

    # l2 = l1 + 100 # TypeError: can only concatenate list (not "int") to list
    l2 = l1 + [100]
    print(l2)

    # Repetition Operator
    l1 = [10,20]
    l2 = l1 * 2
    print(l2)
    l3 = 2 * l1
    print(l3)

    l1 = [10,20]
    l2 = [30,40]
    l3 = l1 + l2
    l4 = l3 * 3
    print(l4)

    # Equality Operator
    l1 = ['Dog','Cat','Rat']
    l2 = ['Dog','Cat','Rat']
    l3 = ['DOG','CAT','RAT']
    l4 = ['Cat','Rat','Dog']
    print(l1 == l2)
    print(l1 == l3)
    print(l1 == l4)
    print(l1 != l4)

    # Relational Operator
    print('Relational Operator :')
    l1 = [10,20,30,40]
    l2 = [50,60]
    print(l1 < l2)
    print(l1 <= l2)
    print(l1 > l2)
    print(l1 >= l2)

    # Membership Operator
    print('Membership Operator')
    l1 = [10,20,30,40]
    print(20 in l1)
    print(40 in l1)
    print(50 in l1)
    print(50 not in l1)
