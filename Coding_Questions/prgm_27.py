s = 'I am having a very nice day'
s = s.split()
count = 0

# using for loop
for x in s:
    count += 1
print(count)

# Using while loop
count = 0
i = 0
while i < len(s):
    count += 1
    i += 1
print(count)