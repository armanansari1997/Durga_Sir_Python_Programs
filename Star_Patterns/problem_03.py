# Alphabet pattern
if __name__ == '__main__':
    n = int(input("Enter the size"))
    for i in range(n):
        print((chr(65+i) + ' ') * n)