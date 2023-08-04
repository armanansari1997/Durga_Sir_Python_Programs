# Sort a String without using any built-in method

s = 'arman'
res = ""
for i in range(len(s)):
    for j in range(i+1, len(s)-1):
        if ord(s[i]) < ord(s[j]):
            res += s[i]

print(res)
# Not Completed