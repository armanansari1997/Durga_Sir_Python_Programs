# To know the contents of directory including subdirectories contents
import os

g = os.walk('material')
print(type(g))  # <class 'generator'>
print(g)  # <generator object _walk at 0x0000012F15D84200>
print()

# Every element returned by generator is a tuple which contains 3 elements
for directorypath, dirnames, filenames in g:
    print('Directory path :', directorypath)
    print('Directory names :', dirnames)
    print('File names :', filenames)
    print('---------------------------')

