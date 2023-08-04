# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists

f = open('txt2', 'r')
# print(f.write('I Love Programming'))
print(f.tell())
print(f.readlines())
f.seek(4)
print(f.tell())
print(f.readlines())
f.close()

