if __name__ == '__main__':
    s = 'durga'

    # 1) Using Slice operator
    # print(s[::-1])

    # rev = reversed(s)
    # for i in rev:
    #     print(i)
    # We will get character's line by line

    # Using reversed and join object
    # rev = reversed(s)
    # print(''.join(rev))

    # Using while loop by +ve indexing
    # i = 0
    # rev = ''
    # while i < len(s):
    #     rev = s[i] + rev
    #     i += 1
    # print(rev)

    # USing while loop by -ve indexing
    i = len(s) - 1
    rev = ''
    while i >= 0:
        rev += s[i]
        i -= 1
    print(rev)



