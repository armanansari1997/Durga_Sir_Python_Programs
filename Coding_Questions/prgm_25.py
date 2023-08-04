# Find the longest substring where character is not repeated
s1 = 'abcfggdghiqwerty'
length = 3
l1 = []
temp = ""
for i in range(len(s1)):
    if s1[i] not in temp:
        temp += s1[i]
    else:
        l1.append(temp)
        temp = s1[i]
l1.append(temp)
print(l1)  # ['abcfg', 'gd', 'ghiqwerty']
print(max(l1))  # ghiqwerty

