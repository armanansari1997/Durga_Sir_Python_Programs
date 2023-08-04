# list of missing numbers

# 1st way:
def missing_num(lst):
    res = [x for x in range(lst[0], lst[-1] + 1) if x not in lst]
    return res


lst = [1, 3, 4, 2, 8, 9]
res = missing_num(lst)
print(res)  # [5, 6, 7]

# 2nd way:


def missing_num2(lst, n):
    b = [0] * (lst[-1])
    for i in range(n):
        if i not in lst[i]:
            b[i] = 1
    return b


lst = [1, 3, 4, 2, 8, 9]
n = len(lst)
res = missing_num2(lst, n)
print(res)
