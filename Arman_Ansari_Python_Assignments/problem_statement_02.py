if __name__ == '__main__':
    num1 = int(input("Enter num1"))
    num2 = int(input("Enter num2"))
    num3 = int(input("Enter num3"))
    output = num1 if num1 > num2 else num2
    output2 = output if output > num3 else num3
    print(output2)

    # Recommended Way
    result = num1 if (num1 > num2 and num1 > num3) else num2 if (num2 > num1 and num2 > num3) else num3
    print(result)
