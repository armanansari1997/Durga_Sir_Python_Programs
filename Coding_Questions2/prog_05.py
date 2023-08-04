# Check whether a given number is palindrome or not

# user input
no = int(input('Enter a no'))
# no = 45654
num = no
rev = rem = 0
while no > 0:
    rem = no % 10
    rev = rev * 10 + rem
    no = no // 10

res = 'palindrome' if num == rev else 'Not a palindrome'
print(res)
