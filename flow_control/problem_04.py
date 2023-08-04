if __name__ == '__main__':
    n1 = int(input("Enter a number"))
    n2 = int(input("Enter a number"))
    n3 = int(input("Enter a number"))
    if n1 > n2 and n1 > n3:
        print('Greater number is {}'.format(n1))
    elif n2 > n3:
        print('Greater number is {}'.format(n2))
    else:
        print('Greater number is {}'.format(n3))