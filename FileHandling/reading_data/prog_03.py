# reading data line by line

f = open('abc.txt', 'r')
line = f.readline()
while line != '':
    # print(line)  # It is printing in a new line
    print(line, end='')
    line = f.readline()
f.close()

# Output :
# Durga
# Software
# Solutions
# Hyderabad


# By using readlines() function
f = open('abc.txt', 'r')
l = f.readlines()
print(l)  # ['Durga\n', 'Software\n', 'Solutions\n', 'Hyderabad\n']
for line in l:
    # print(line)  # It is printing in a new line
    print(line, end='')
f.close()


# Output :
# Durga
# Software
# Solutions
# Hyderabad
