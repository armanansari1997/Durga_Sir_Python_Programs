# WAP to check whether the given file exists or not. If it is available then print its content .

import os

fname = input('Enter the file name : ')
if os.path.isfile(fname):
    print('File exists :', fname)
    print('The content of the file is : ')
    f = open(fname, 'r')
    text = f.read()
    print(text)
    f.close()
else:
    print("File doesn't exists", fname)

# 2nd way :
# import os, sys
#
# fname = input('Enter file name : ')
# if os.path.isfile(fname):
#     print('File Exists :', fname)
#     f = open(fname, 'r')
# else:
#     print("File doesn't exists :", fname)
#     sys.exit(0)
#
# text = f.read()
# print('The content of the file is :')
# print(text)
# f.close()
