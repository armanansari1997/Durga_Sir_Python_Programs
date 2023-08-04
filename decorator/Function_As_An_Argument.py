#  we can pass a function as an argument to another function

# eg-1
def f1(func):
    func()


def f2():
    print('f2 function')


# function calling
f1(f2)  # f2 function'


# eg-2
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list(filter(is_even, list1))
print(list2)  # [2, 4, 6, 8, 10]
