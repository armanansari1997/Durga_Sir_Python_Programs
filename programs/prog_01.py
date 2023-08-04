s = "India is a great country"
s = s.split()
for ch in s:
    print(ch[0].upper()+ch[1:].lower())

# Output:
# India
# Is
# A
# Great
# Country
