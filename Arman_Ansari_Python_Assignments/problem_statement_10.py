if __name__ == '__main__':
    list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    items = [e for e in list_one if e % 3 == 0]
    print(len(items))