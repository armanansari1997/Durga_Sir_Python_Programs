# WAP for the following requirement :
# input : a3z2b4
# output : aaabbbbzz ( sorted )
if __name__ == '__main__':
    s = 'a3z2b4'
    output = ''
    for ch in s:
        if ch.isalpha():
            x = ch
        else:
            d = int(ch)
            output += x * d
    print(''.join(sorted(output))) # aaabbbbzz

