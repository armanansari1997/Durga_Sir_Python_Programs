# input = 'A2B2C3D4'
# output = 'AABBCCCDDDD'

s = 'A2B2C3D4'
res = ''
for ch in s:
    if ch.isalpha():
        temp = ch
    else:
        res += temp + str(ch)
print(res)