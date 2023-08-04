if __name__ == '__main__':
    n1 = int(input("Enter a number"))
    n2 = int(input("Enter a number"))
    if n1 > n2:
        print('Greater number is {}'.format(n1))
    elif n1 < n2:
        print('Greater number is {}'.format(n2))
    else:
        print('Numbers are equal : {}'.format(n1))
