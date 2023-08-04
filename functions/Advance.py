from functools import reduce

if __name__ == '__main__':
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # odd = filter(lambda n:n%2 != 0,l)
    # print(odd) #  <filter object at 0x000001D3A1CB6DD0>
    odd = list(filter(lambda n: n % 2 != 0, l))
    print(odd)  # [1, 3, 5, 7, 9]

    # even numbers
    even = list(filter(lambda n: n % 2 == 0, l))
    print(even)  # [0, 2, 4, 6, 8, 10]

    # divisible by 3 and odd
    div_by_3_and_odd = list(filter(lambda n: n % 3 == 0 and n % 2 != 0, l))
    print(div_by_3_and_odd)  # [3, 9]

    # biggest of 2 numbers
    bigger = lambda a, b: a if a > b else b
    print(bigger(10, 20))  # 20
    print(bigger(-10, -20))  # -10

    # biggest of 3 numbers
    bigger = lambda a, b, c: a if a > b and a > c else b if b > c else c
    print(bigger(10, 20, 30))  # 30
    print(bigger(6, 3, 4))  # 6
    print(bigger(10, 50, 40))  # 50

    heroines = ['KatrinaKaif', 'KareenaKapoor', 'Anushka', 'Deepika', 'SunnyLeone', 'Mallika']
    # print the name which starts with k
    starts_with_k = list(filter(lambda name: name[0] == 'K', heroines))  # ['KatrinaKaif', 'KareenaKapoor']
    print(starts_with_k)

    # print the names whose name length is divisible by 5
    length_div_by_5 = list(filter(lambda name: len(name) % 5 == 0, heroines))
    print(length_div_by_5)  # ['SunnyLeone']

    # print the names whose name length is odd
    length_is_odd = list(filter(lambda name: len(name) % 2 != 0, heroines))
    print(length_is_odd)  # ['KatrinaKaif', 'KareenaKapoor', 'Anushka', 'Deepika', 'Mallika']

    # map() function:
    l = [1, 2, 3, 4, 5]


    # Find square values without lambda function
    def squareit(num):
        return num * num


    l1 = list(map(squareit, l))
    print(l1)  # [1, 4, 9, 16, 25]

    # Find square values using lambda:
    l1 = map(lambda n: n * n, l)
    print(l1)  # <map object at 0x000001FA79873D30>
    l1 = list(map(lambda n: n * n, l))
    print(l1)  # [1, 4, 9, 16, 25]

    # eg-1
    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 10, 15, 20, 25]
    l3 = list(map(lambda x, y: x * y, l1, l2))
    print(l3)  # [5, 20, 45, 80, 125]

    # eg-2
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l2 = [5, 10, 15, 20, 25]
    l3 = list(map(lambda x, y: x * y, l1, l2))
    print(l3)  # [5, 20, 45, 80, 125]

    # eg-3
    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 10, 15, 20, 25, 30, 35, 40]
    l3 = list(map(lambda x, y: x * y, l1, l2))
    print(l3)  # [5, 20, 45, 80, 125]

    # eg-4
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l4 = list(map(lambda x, y, z: x + y + z, l1, l2, l3))
    print(l4)  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    # reduce() function:
    l = [10, 20, 30, 40, 50]
    result = reduce(lambda x, y: x + y, l)
    print(result)  # 150

    # Sum of first 100 number using reduce() function
    result = reduce(lambda x, y: x + y, range(1, 101))
    print(result)  # 5050

