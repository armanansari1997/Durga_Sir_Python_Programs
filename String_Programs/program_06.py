# WAP for the following requirement :
# input : a4b3c2
# output : aaaabbbcc
if __name__ == '__main__':
    s = 'a4b3c2'
    output = ''
    for ch in s:
        if ch.isalpha():
            x = ch
        else:
            d = int(ch)
            output += x * d
    print(output) # aaaabbbcc

