if __name__ == '__main__':
    s = 'ABCDEFGHIBJK'
    print(s.find('B')) # 1
    print(s.find('Z')) # -1

    print(s.rfind('B')) # 9
    print(s.rfind('Z')) # -1

    print(s.index('B')) # 1
    # print(s.index('Z')) # ValueError: substring not found

    print(s.rindex('B')) # 1
    # print(s.rindex('Z')) # ValueError: substring not found

    print('Count of B is : {} '.format(s.count('B')))
