# input  : a3b4c2
# output : aaabbbbcc

s = 'a3b4c2'
size = len(s)
res = ""
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        res += x * d

print(res)

# Using while loop

# i = 0
# while i < size:
#     if s[i].isalpha():
#         x = s[i]
#     else:
#         d = int(s[i])
#         res = res + (x * d)
#     i += 1
# print(res)
