if __name__ == '__main__':
    s = 'aaaabbcaccz'
    # O/P : 5a2b3c1z
    s = sorted(s)
    print(s)
    out = ''
    i = 0
    j = 0
    while i < len(s):
        j = s.count(s[i])
        out += str(j) + s[i]
        i += j
    print(out)