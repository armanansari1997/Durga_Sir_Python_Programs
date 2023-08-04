# Reverse internal content of each word
if __name__ == '__main__':
    s = input("Enter the words")
    l = s.split()
    l1 = []
    for word in l:
        l1.append(word[::-1])
    output = ' '.join(l1)
    print(output)

