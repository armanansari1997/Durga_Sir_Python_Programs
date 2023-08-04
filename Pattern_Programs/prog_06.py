"""
* * * * *
 * * * *
  * * *
   * *
    *

"""

n = 5

for i in range(n):  # 0,1,2,3,4
    for j in range(i):
        print(end=' ')
    for k in range(i, n):
        print('*', end=' ')
    print()
