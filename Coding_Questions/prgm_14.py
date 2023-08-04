# input  : aaabbbbcc
# output : a3b4c2

s = 'aaabbbbcc'
d = {}
res = ''
for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
for k, v in d.items():
    res += k + str(v)
print("Dictionary :", d)  # Dictionary : {'a': 3, 'b': 4, 'c': 2}
print("String :", res)  # String : a3b4c2
print("Most repeated character :", max(d, key=d.get))  # b
print("Least repeated character :", min(d, key=d.get))  # c

