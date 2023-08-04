# WAP to find duplicate in a string

s = "abcadfbe"
res = ""
for i in s:
    if s.count(i) > 1:
        if i not in res:
            res += i
print(res)