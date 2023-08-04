f = open('abc.txt', 'r')
print(f.tell())  # 0
f.seek(3)
print(f.tell())  # 3
print(f.read(2))  # ga
f.seek(20)
print(f.read())
# Output:
# ga
# utions
# Hyderabad

f.seek(0)
print(f.read())
f.close()
# Output :
# Durga
# Software
# Solutions
# Hyderabad

