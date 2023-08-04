if __name__ == '__main__':
    number_list = list([1, 2, 3, 4, 5])
    for number in number_list:
        if number == 3:
            print(True)
    # 2nd way
    print(3 in number_list)
