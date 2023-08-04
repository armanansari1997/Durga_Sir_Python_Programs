# Check whether String is palindrome or not

mystring = "liril"

# way -01

# new_string = mystring[::-1]
# print(mystring == new_string)


# way -02
new_string = ""
for i in range(len(mystring)):
    new_string = mystring[i] + new_string
result = "Palindrome" if new_string == mystring else "Not a Palindrome"
print(result)
