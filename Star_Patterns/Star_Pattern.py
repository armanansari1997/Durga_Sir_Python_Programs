if __name__ == '__main__':
    size = int(input("Enter the size"))
    for i in range(size):
        # print('* ' * (size-i))
        # print('*',end=' ') * * *
        # print('* ' * size)
        print((chr(65+i)+' ') * size)
        # for j in range(i+1):
        #     print('*', end=' ')
        # print()

