# vowel count

s = "abcedifoazuyyetr"
vow_count = 0
for ch in s:
    if ch.isalpha():
        if (ch == 'a') | (ch == 'e') | (ch == 'i') | (ch == 'o') | (ch == 'u'):  # braces is mandatory
            vow_count += 1

print('The vowel count is :', vow_count)


# 2nd way :

# s = "abcedifoazuyyetr"
# vow_count = 0
# vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
# for ch in s:
#     if ch in vowel:
#         vow_count += 1
#
# print('The vowel count is :', vow_count)
