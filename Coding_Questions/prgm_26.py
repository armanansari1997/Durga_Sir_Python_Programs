l = [1, 2, 3, 4, 4, 5, 5, 6, 1]
l1 = []
l2 = []
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        l2.append(i)
print(l1)  # Remove duplicates  # [1, 2, 3, 4, 5, 6]
print(l2)  # Duplicates elements # [4, 5, 1]
print(set(l1))  # {1, 2, 3, 4, 5, 6}
print(set(l2))  # {1, 4, 5}

# Recommended way
output = {x for x in l if l.count(x) > 1}
print(output)  # {1, 4, 5}
print(type(output))  # <class 'set'>
