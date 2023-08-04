with open('txt1', 'r') as f1, open('txt2', 'w') as f2:
    lines = f1.readlines()
    for line in lines:
        f2.write(line)
    