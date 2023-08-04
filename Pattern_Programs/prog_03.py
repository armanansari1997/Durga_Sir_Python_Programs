"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

n = 5

for i in range(n):  # 0,1,2,3,4
    for j in range(i+1):  # (1,2,3,4,5) 0+1=1,1+1=2,2+1=3,3+1=4,4+1=5
        print('*', end=' ')
    print()

for i in range(n):  # 0,1,2,3,4
    for j in range(i+1, n):  # 1,2,3,4
        print('*', end=' ')
    print()
