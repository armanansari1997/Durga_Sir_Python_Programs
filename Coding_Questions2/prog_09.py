# Question 1)

str1 = "Sky is Blue"
str2 = ' '.join(str1.split()[::-1])
print(str2)  # Blue is Sky

# 1) (or)
str1 = "Sky is Blue"
list1 = list(reversed(str1.split()))
result = ' '.join(list1)
print(result)  # Blue is Sky


# Question 2)
list1 = [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6]
list2 = []
for x in list1:
    if list1.count(x) == 1:
        list2.append(x)
print(list2)  # [1, 4]

# 2) (or)
result = [x for x in list1 if list1.count(x) == 1]
print(result)  # [1, 4]

# Question 3)
str1 = "a,a,a,b,b,c,c,c"
list1 = str1.split(',')
dict1 = {}

for x in list1:
    if x not in dict1:
        dict1[x] = 1
    else:
        dict1[x] += 1

print(dict1)  # {'a': 3, 'b': 2, 'c': 3}


# 3) (or)
str1 = "aaabbccc"
for x in str1:
    dict1.setdefault(x, 0) + 1

print(dict1)  # {'a': 3, 'b': 2, 'c': 3}

# Question 4)
str1 = "A3X4Z3"
str2 = ""
for ch in str1:
    if ch.isalpha():
        str2 += ch
        temp = ch
    else:
        if (ord(temp) + int(ch)) > 90:
            str2 += chr(64 + (int(ch) - (90-ord(temp))))
        else:
            str2 += chr(ord(temp) + int(ch))

print(str2)

