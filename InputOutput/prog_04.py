# tell() and seek() function in Input Output Concept
# f = open('txt')
f = open('txt1', 'r')
print(f.tell())  # 0 (used to find the cursor in the file)
f.seek(4)  # moving cursor to the 4th character in the file
print(f.tell())  # 4
f.close()