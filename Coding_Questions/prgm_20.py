# 1) Reverse a string using slicing
# 2) Reverse a string without using slicing
# 3) Check whether given string is Palindrome or not

# 1)
s = "arman"
s = s[::-1]
print("Reverse String :", s)  # Reverse String : namra

# 2)
s = "arman"
rev = ""
for i in s:
    rev = i + rev
print('Reverse String :', rev)  # Reverse String : namra

# 3)
s = 'abcba'
s1 = s[::-1]
if s == s1:
    print('Yes')
else:
    print('No')

# Output : Yes
