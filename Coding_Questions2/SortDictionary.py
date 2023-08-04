# 1st way
dict1 = {575: "Apple", 876: "Mango", 132: "Grapes", 782: "Banana"}
d = sorted(dict1.keys())
print(d)
dict2 = {}
for i in d:
    dict2[i] = dict1[i]

print(dict2)

# 2nd Way using (Dict Comprehension)
res = {key: value for key, value in sorted(dict1.items(), key=lambda x: x[1])}
print(res)
