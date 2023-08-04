# find max height of person that will see all its people without sorting, and they will be placed in order
# Input     : 2,17,6,8,1
# Output    : 1,8,17

inp = [2, 17, 6, 8, 1]
inp = list(reversed(inp))  # [1, 8, 6, 17, 2]
max_height = inp[0]
li = []
for i in inp:
    if i >= max_height:
        max_height = i
        li.append(i)
print(li)

