# Right angle triangle
if __name__ == '__main__':
    n = int(input("Enter the size"))
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()