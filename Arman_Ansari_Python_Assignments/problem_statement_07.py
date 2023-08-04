if __name__ == '__main__':
    number_list = [1, 2, 3, 4, 5, [4, 6], 7]
    required_number = eval(input("Enter number"))
    for number in number_list:
        if isinstance(number, list):
            print(required_number in number)

