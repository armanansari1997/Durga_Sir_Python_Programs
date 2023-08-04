# remove duplicate elements without using set function

s = "aaabbbcccdddfa"
res = ""

for ch in s:
    if ch not in res:
        res += ch

print(res)  # abcdf

# 2nd way
s = "aabbccs"
target = []
for ch in s:
    if ch not in target:
        target.append(ch)

output = ''.join(target)
print(output)

