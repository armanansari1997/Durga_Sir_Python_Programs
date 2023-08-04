# Opening the files
f1 = open('abc.txt', 'r')
f2 = open('xyz.txt', 'w')

# Reading data from 'abc.txt' file
data = f1.read()
# print(type(data))  # <class 'str'>

# Writing data to the 'xyz.txt' file
# f2.writelines(data)
f2.write(data)

# Closing the files
f1.close()
f2.close()
