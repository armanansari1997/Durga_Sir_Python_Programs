# Remove Punctuation except space

s = '/*apples are & found% only @red & green'
res = ""
for i in s:
    if (i >= 'A' and i <= 'Z') | (i >= 'a' and i <= 'z') | (i == ' '):
        res += i

print(res)
