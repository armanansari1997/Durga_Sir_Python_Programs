# All possible substring
s = 'aaaabbaa'
for i in range(0, len(s)-2):
    for j in range(i+2, len(s)):
        res = s[i:j]

    print(res)

# longest substring
import sys
s = 'aaaabbaa'
for i in range(0, len(s)-2):
    for j in range(i+2, len(s)):
        res = s[i:j]

    print(res)
    sys.exit(0)
