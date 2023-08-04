if __name__ == '__main__':
    s = 'durga sir is a very good trainer'
    s = s.split()

    # Using slice operator
    # print(s[::-1])

    # Using reversed and join object
    # rev = []
    # for i in reversed(s):
    #     rev.append(''.join(i))
    # output = ' '.join(rev)
    # print(output)

    # Using while loop
    i = len(s)-1
    rev = []
    while i >= 0:
        rev.append(s[i])
        i -= 1
    output = ' '.join(rev)
    print(output)
