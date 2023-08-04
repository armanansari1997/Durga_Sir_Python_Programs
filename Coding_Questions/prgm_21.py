# WAP check whether the 2 strings are Anagrams or not

s1 = 'SILENT'
s2 = 'LISTEN'
if sorted(s1) == sorted(s2):
    print('Anagram')
else:
    print('Not Anagram')

# using ternary operator
print('Anagram' if sorted(s1) == sorted(s2) else 'Not Anagram')