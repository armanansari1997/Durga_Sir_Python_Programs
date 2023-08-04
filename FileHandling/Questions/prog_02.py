f = open('xyz.txt', 'w')
# Writing to the 'xyz.txt' file
f.write('All Students are STUPIDS')

with open('xyz.txt', 'r+') as f:
    # Reading from 'xyz.txt' file
    text = f.read()
    print(text)
    print('Current cursor position :', f.tell())

    f.seek(17)
    f.write('GEMS!!!')
    f.seek(0)

    text = f.read()
    print('Data After Modification')
    print(text)

    f.seek(17)
    f.write('DATA')
    f.seek(0)

    text = f.read()
    print(text)
