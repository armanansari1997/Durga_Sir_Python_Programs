f = open('abc.txt', 'r')
print(f.read(3))
print(f.readline())
print(f.readline())
print(f.read(4))
print('Remaining data : ')
print(f.read())

f.close()
