"""

10 9 8 7
6 5 4
3 2
1


"""

n = 4
count = (n+1) * 2
for i in range(n):
    for j in range(i+1, n+1):
        print(count, end=' ')
        count -= 1
    print()