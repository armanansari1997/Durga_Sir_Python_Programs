if __name__ == '__main__':
    n = int(input("Enter the size"))
    for i in range(n):
        print(' ' * (n-i-1) + '* ' * (i+1))