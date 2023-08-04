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