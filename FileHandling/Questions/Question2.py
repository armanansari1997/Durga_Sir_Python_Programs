# WAP to print the number of lines, words and characters present in the given file
import os

fname = input('Enter the file :')
if os.path.isfile(fname):
    print('File Exists :', fname)
    f = open(fname, 'r')
    lcount = wcount = ccount = 0
    for line in f:
        lcount += 1
        ccount += len(line)
        words = line.split()
        wcount += len(words)
    print('The number of lines :', lcount)
    print('The number of words :', wcount)
    print('The number of characters :', ccount)

    # Closing the file
    f.close()
else:
    print("File doesn't Exists :", fname)


# 2nd way :

# import os, sys
# fname = input('Enter the file name : ')
# if os.path.isfile(fname):
#     print('File Exists :', fname)
#     f = open(fname, 'r')
# else:
#     print("File doesn't exists ", fname)
#     sys.exit(0)
#
# lcount = wcount = ccount = 0
# for line in f:
#     lcount += 1
#     ccount += len(line)
#     words = line.split()
#     wcount += len(words)
# f.seek(0)
# print(f.read())
# print('Lines count :', lcount)
# print('Words count :', wcount)
# print('Characters count :', ccount)
#
# # Closing the file
# f.close()
