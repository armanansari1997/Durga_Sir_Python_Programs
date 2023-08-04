if __name__ == '__main__':
    # a = eval(input("Enter num1"))
    # b = eval(input("Enter num2"))
    # c = eval(input("Enter num3"))
    a, b, c = [int(x) for x in input("Enter 3 numbers").split(' ')]
    print(a + b + c)
