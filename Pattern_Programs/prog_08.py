"""

01
02 03
04 05 06
07 08 09 10
11 12 13 14 15

"""

n = 5
count = 1
for i in range(n):
    for j in range(i+1):
        if count < 10:
            print('0%d' % count, end=' ')
        else:
            print(count, end=' ')
        count += 1
    print()
