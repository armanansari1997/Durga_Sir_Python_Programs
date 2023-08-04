if __name__ == '__main__':
    l = [10, 20, 30, 40, 5, 30, 40]
    inp = int(input('Enter a no to search'))
    i = 0
    for x in l:
        if inp == x:
            print('Element is :', x)
            print('Index of element is :', l.index(inp), end=' ')
            i += 1
            break
    if i == 0:
        print("list doesn't contain element :", inp)
