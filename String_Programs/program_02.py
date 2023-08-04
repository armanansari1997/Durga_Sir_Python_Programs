# Reverse internal content of every 2nd word present in the given string
if __name__ == '__main__':
    s = input("Enter the words")
    l = s.split()
    l1 = []
    for i in range(len(l)):
        if i%2 == 0:
            l1.append(l[i])
        else:
            l1.append(l[i][::-1])
    output = ' '.join(l1)
    print(output)
    print('{2} {0} {1}'.format("hhsjjssj","hhshsj",22))