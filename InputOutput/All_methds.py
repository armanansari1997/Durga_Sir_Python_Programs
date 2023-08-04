# 'a'       open for writing, appending to the end of the file if it exists
with open('txt1', 'r') as f1, open('txt2', 'a') as f2, open('txt1', 'a') as f3:
    print(f1.read(1))  # read 1st character of the file
    print(f1.readline())  # read all characters (or) remaining character
    print(f1.readlines())  # read line by line as list (treat a line as an element of list)

    f3.write('I love python\n')
    f2.write('I love python\n')

    f2.writelines('I am learning selenium with python\n')
    # print(f1.tell())
    # f1.seek(4)
    # f2.close()
    print(f1.fileno())

    print(f1.readable())  # true
    print(f2.readable())  # False
    print(f3.readable())  # False
