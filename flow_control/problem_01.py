# convert number to word (4 to FOUR) from 0-9
if __name__ == '__main__':
    l = ['zero','one','two','three','four','five','six','seven','eight','nine']
    n = int(input("Enter any number between 0 and 9"))
    print(l[n].upper())