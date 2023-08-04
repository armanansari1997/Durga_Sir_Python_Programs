# tell() function :

# Opening the file
f = open('abc.txt')

print(f.tell())  # 0
print(f.read(2))  # Du
print(f.tell())  # 2
print(f.read(3))  # rga
print(f.tell())  # 5

# Closing the file
f.close()


# seek() function :

# Opening the file
f = open('abc.txt', 'r')

f.seek(3)  # seek from 0 to 2 (means 3 characters)
print(f.tell())  # 3
print(f.readline())  # ga
f.seek(17)  # seek from 0 to 16 (means 17 characters)
print(f.tell())  # 17
