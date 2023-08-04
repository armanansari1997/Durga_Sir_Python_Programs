def isMultipleOf3(num):
    return num % 3 == 0


def isMultipleOf5(num):
    return num % 5 == 0


# def isMultipleOf3And5(num):
#     return num % 3 == 0 and num % 5 == 0

def isMultipleOf3And5(num):
    return isMultipleOf3(num) and isMultipleOf5(num)


if __name__ == '__main__':
    num = int(input("Enter the number"))

    # #if num % 3 == 0 and num % 5 == 0:
    #  #   print("FizFuzz")
    # #elif num % 3 == 0:
    # #    print("Fiz")
    # elif num % 5 == 0:
    #     print("Fuzz")
    # else:
    #     print(num)

    if isMultipleOf3And5(num):
        print("FizFuzz")
    elif isMultipleOf3(num):
        print("Fiz")
    elif isMultipleOf5(num):
        print("Fuzz")
    else:
        print(num)

