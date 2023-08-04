f = open('abc.txt', 'r')
data = f.read(10)  # read only 10 characters
print(data)

f.close()
