# convert number to word (88 to EIGHTY EIGHT) from 0-99
if __name__ == '__main__':
    l = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve',
         'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    l1 = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    n = int(input("Enter any number between 0 and 99"))
    output = ''
    if n == 0:
        output = 'ZERO'
        print(output)
    elif n < 20:
        output = l[n].upper()
        print(output)
    elif n >= 20:
        output = l1[n//10].upper() +' '+ l[n%10].upper()
        print(output)
    else:
        print('Please enter number between 0 and 99')