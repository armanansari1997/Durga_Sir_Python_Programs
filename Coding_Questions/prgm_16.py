# WAP to print duplicate element present in list

l = ['hello', 10, 20, 40, 20, 60, 40, 30]
l1 = []
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j] and l[i] not in l1:
            l1.append(l[i])

print(l1)  # [20, 40]
