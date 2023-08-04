if __name__ == '__main__':
    l = [10,20,30,10,20,40,30]
    print(len(l))
    print(l.count(10))
    print(l.count(50))

    l1 = [1,2,1,2,3,4]
    print(l1.index(1))
    print(l1.index(2))
    # print(l1.index(5)) # ValueError: 5 is not in list

    l = []
    for i in range(1,101):
        if i % 10 == 0:
            l.append(i)
    print(l)
    # out = [i for i in range(1,101) if i % 10 == 0]
    # print(out)

    #l.insert()
    l = [10,20,30,40]
    l.insert(1,7777)
    print(l)

    l.insert(100,7777)
    l.insert(-100,9999)
    print(l)

    # extend():-
    order1 = ['Chicken','Mutton','Fish']
    order2 = ['KF','KO','RC']
    order1.extend(order2)
    print(order1)

    # Using append add multiple elements
    l1 = [10,20,30]
    l2 = [40,50]
    l1.append(l2)
    print(l1)
    print(len(l1))

    # Using extend multiple elements
    l1 = [10, 20, 30]
    l2 = [40, 50]
    l1.extend(l2)
    print(l1)
    print(len(l1))

    l1 = [10,20,30]
    l2 = 'ABC'
    l1.extend(l2)
    print(l1)
    print(len(l1))

    l1 = [10, 20, 30]
    l2 = 'ABC'
    l1.append(l2)
    print(l1)
    print(len(l1))

    # remove() :-
    l = [10,20,10,20,40]
    l.remove(40)
    print(l)
    l.remove(10) # only the 1st element will be deleted
    print(l)
    # l.remove(50) #ValueError: list.remove(x): x not in list

    # l = [1,2,3,4,5,6]
    # print('Before Removal',l)
    # x = int(input('Enter an element to  remove'))
    # if x in l:
    #     l.remove(x)
    #     print('After Removal',l)
    # else:
    #     print(x,'not present in list')

    # Remove all occurrences
    # l = [1,1,1,1,2,2,2,3,3]
    # x = int(input('Enter element to remove'))
    # while True:
    #     if x in l:
    #         l.remove(x)
    #     else:
    #         break
    # print('After Removal ', l)

     # pop():
    l = [10,20,30]
    print(l.pop())
    print(l)
    print(l.pop())
    print(l.pop())
    print(l)

    # pop(index):
    l = [10,20,30,40]
    print(l.pop(1))
    print(l)
    # print(l.pop(100)) # IndexError: pop index out of range

    # clear():
    l = [10,20,30,40]
    print(l)
    l.clear()
    print(l)

    # reverse():
    l = [10,20,30,40]
    l.reverse()
    print(l)

    # reversed() of python inbuilt function
    l = [10,20,30,40,50]
    r = reversed(l)
    l1 = list(r)
    print(l)
    print(r)
    print(l1)

    # Sorting elements of List
    # sort()
    l = [10,50,5,20,30]
    l.sort()
    print('Sorted List : ',l)

    l = ['Banana','Cat','Apple']
    l.sort()
    print(l)

    # descending Order using sort(reverse=True)
    l = [20,5,15,0,10]
    l.sort(reverse=True)
    print(l)

    l = ['Banana', 'Cat', 'Apple']
    l.sort(reverse=True)
    print(l)

    l = [40,30,10,'A','B']
    # l.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

    # sorted() of python inbuilt function
    l = [10,80,5,15,30,25]
    l1 = sorted(l)
    print(l)
    print(l1)

    # Aliasing of List Object
    l1 = [10,20,30]
    l2 = l1
    l1[1] = 7777
    print(l1) # [10, 7777, 30]
    print(l2) # [10, 7777, 30]

    # Cloning
    # using slice Operator
    l = [10,20,30]
    l1 = l[::]
    l1[1] = 7777
    print(l) # [10, 20, 30]
    print(l1) # [10, 7777, 30]

    # using copy() method
    l = [10,20,40]
    l1 = l.copy()
    l[1] = 8888
    print(l) # [10, 8888, 40]
    print(l1) # [10, 20, 40]

    # Nested List
    l = [10,20,[30,40]]
    print(l[0]) # 10
    print(l[1]) # 20
    print(l[2]) # [30, 40]
    print(l[-1]) # [30, 40]
    print(l[2][0]) # 30
    print(l[2][1]) # 40

    # Program to print Matrix:
    l1 = [[10,20,30],[40,50,60],[70,80,90]]
    print(l1)
    print('Elements row wise : ')
    for l in l1:
        print(l)

    print('Elements in matrix style : ')
    for i in l1:
        for j in i:
            print(j, end=' ')
        print()







