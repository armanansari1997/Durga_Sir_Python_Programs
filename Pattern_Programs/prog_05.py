"""
        *
      * *
    * * *
  * * * *
* * * * *

"""

n = 5
for i in range(n):  # 0,1,2,3,4
    for j in range(i+1, n):  # 1,2,3,4
        print(end='  ')
    for k in range(i+1):
        print('*', end=' ')
    print()


