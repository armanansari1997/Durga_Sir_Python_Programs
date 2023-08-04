# Input: [2, 45, 32, 616]
# Output: [2, 9, 5, 13]

# Using nested for loop
l1 = [2, 45, 32, 616]
output = []
for num in l1:
    sum1 = 0
    for digit in str(num):
        sum1 += int(digit)
    output.append(sum1)
print(l1)
print(output)


# Without using nested for loop
l1 = [2, 45, 32, 616]
output = []
for num in l1:
    output.append(sum(map(int, list(str(num)))))
print(l1)
print(output)

