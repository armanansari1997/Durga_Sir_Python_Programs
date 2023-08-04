def duplicate_chars_and_theirs_index():
    l = [1, 1, 1, 4, 6, 3, 2, 3]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] == l[j] and i != j:
                print('Duplicate Character is :', l[j], 'and index is :', j)  # need to check


def find_max_and_min_without_sorting():
    l = [1, 5, 2, 7, 0, 4]
    max_n = l[0]
    min_n = l[0]
    for num in l:
        if num > max_n:
            max_n = num
        elif num < min_n:
            min_n = num
    print('Min number is :', min_n)
    print('Max number is :', max_n)


def sort_list_in_desc():
    # sort the list in descending order
    l = [1, 5, 2, 7, 0, 4]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]  # Swapping
    print(l)


def sort_list_in_asc():
    # sort the list in ascending order
    l = [1, 5, 2, 7, 0, 4]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]  # Swapping
    print(l)


sort_list_in_asc()
sort_list_in_desc()
find_max_and_min_without_sorting()
duplicate_chars_and_theirs_index()