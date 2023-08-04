"""
*
* *
* * *
* * * *
* * * * *
"""

n = 5

# for i in range(1, n+1):
#     print('* ' * i)

# 2nd way
for i in range(1, n+1):  # 1,2,3,4,5
    for j in range(i):  # 0,i
        print('*', end=' ')
    print()



