# Find the missing number
l = [1, 2, 3, 4, 5, 7, 8, 9, 10]
n = len(l) + 1
total_sum = 0
for i in range(1, n + 1):
    total_sum += i

sum = 0
for i in l:
    sum += i
print('The missing number is :', total_sum - sum)


