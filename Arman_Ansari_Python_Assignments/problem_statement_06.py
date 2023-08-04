if __name__ == '__main__':
    count = 0
    sample_list = [1, 2, 3, 4, 4, 4, 5, 6, 6]
    for number in sample_list:
        if number == 4:
            count = count + 1
    print(count)

    # Recommended way
    # Here 4 is a value
    print(sample_list.count(4))
