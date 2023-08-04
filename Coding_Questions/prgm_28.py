# write a python function to search a given element X without using built-in method
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return 'No Such element found'


l = [1, 2, 3, 4, 4, 5, 5, 6, 1]
print(search(l, 6))  # 7
print(search(l, 10))  # No Such element found
