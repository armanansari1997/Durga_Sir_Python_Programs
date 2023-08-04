# Assume i/p string contains only alphabets and digits.WAP to sort characters of the string
# first alphabet symbols followed by digits?
if __name__ == '__main__':
    s = 'B4A1D3'
    # o/p : ABD134

    alphabets = ''
    digits = ''
    for i in s:
        if i.isalpha():
            alphabets += i
        else:
            digits += i
    output = sorted(alphabets) + sorted(digits)
    print(''.join(output))
