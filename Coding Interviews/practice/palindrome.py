# way -01

# def palindrome(s):
#     temp = s[::-1]
#     if s == temp:
#         print("Yes!! It's a palindrome")
#     else:
#         print("No!! It's not a palindrome")

# s = 'liril'
# palindrome(s)


# way -02

def palindrome(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            return False
    return True


s = 'liril'
result = "Palindrome" if palindrome(s) else "Not a Palindrome"
print(result)





