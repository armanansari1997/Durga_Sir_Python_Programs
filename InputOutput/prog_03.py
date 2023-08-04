with open('txt3', 'r') as f:
    lines = f.readlines()
    rev_list = ''.join(reversed(''.join(lines)))
    print(rev_list)
