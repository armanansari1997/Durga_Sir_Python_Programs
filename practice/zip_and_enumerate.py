if __name__ == '__main__':
    # zip() returns a tuple
    # 1
    for item in list(zip(range(1, 4), ['Arman', 'Rusia', 'Moin', 'Shivam'])):
        print(item)
    # Output:
    # (1, 'Arman')
    # (2, 'Rusia')
    # (3, 'Moin')

    # 2
    l = []
    for item in list(zip(range(1, 4), ['Arman', 'Rusia', 'Moin', 'Shivam'])):
        l.append(item)
    print(l)  # [(1, 'Arman'), (2, 'Rusia'), (3, 'Moin')]

    # 3
    for item in enumerate(range(3)):
        print(item)
    # Output:-
    # (0, 0)
    # (1, 1)
    # (2, 2)
