f = open('xyz.txt', 'w')

# l = ['Sunny', 'Bunny', 'Chinny', 'Vinny']
l = ['Sunny\n', 'Bunny\n', 'Chinny\n', 'Vinny\n']
f.writelines(l)
print('Data written to the file successfully')

f.close()
