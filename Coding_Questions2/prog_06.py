# Check whether a given string is palindrome or not

inp = "liril"
out = ""
for x in reversed(inp):
    out += x

res = 'Palindrome' if ''.join(out) == inp else 'Not a Plaindrome'
print(res)
