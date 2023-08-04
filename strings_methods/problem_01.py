# Find index of all occurrences and count the no. of occurrences
if __name__ == '__main__':
    s = 'ABCDEFABCDEFABCDEFAB'
    subs = 'ABC'
    i = s.find(subs)
    count = 0
    if i == -1:
        print('String does not contain substring : ' + subs)
    while i != -1:
        count += 1
        print('String contains {} at index : {}  '.format(subs, i))
        i = s.find(subs, i + len(subs), len(s))
    print('The number of occurrences : {}'.format(count))
