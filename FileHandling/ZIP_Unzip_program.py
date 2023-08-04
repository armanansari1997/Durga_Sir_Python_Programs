from zipfile import *

f = ZipFile('files24072022.zip', 'r', ZIP_STORED)
names = f.namelist()
print(names)  # ['file1.txt', 'file2.txt', 'file3.txt']

# Read the content of file
for name in names:
    f1 = open(name, 'r')
    text = f1.read()
    print('File name :', name)
    print('The content of the file is :')
    print(text)
    print()
    f1.close()
