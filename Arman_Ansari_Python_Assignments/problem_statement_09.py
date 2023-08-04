if __name__ == '__main__':
    number_list = [1, [2, 3], [4, 5], [6, 7], 8, 9, 10]
    count = 0
    for number in number_list:
        if isinstance(number, list):
            count = count + 1
    print(count)

    items = [e for e in number_list if isinstance(e, list)]
    print(len(items))