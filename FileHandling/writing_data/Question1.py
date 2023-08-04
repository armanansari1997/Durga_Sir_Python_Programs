# WAP to specify file name and data dynamically from the keyboard (for write operation)

file = input('Enter file name')
f = open(file, 'w')
while True:
    data = input('Enter data to write')
    f.write(data+'\n')
    option = input('Do you want to add some more data [yes/no]')
    if option.lower() == 'no':
        f.close()
        break

print('Your provided data witten to the file successfully')
