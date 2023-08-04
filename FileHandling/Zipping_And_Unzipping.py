from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED

# Zipping file
f = ZipFile('files24072022.zip', 'w', ZIP_DEFLATED)

f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')

print('files24072022.zip file is created successfully')

# Unzipping file
# f = ZipFile('files24072022.zip', 'r', compression=ZIP_STORED)
names = f.namelist()
print(names)
