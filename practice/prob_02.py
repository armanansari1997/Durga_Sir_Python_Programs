if __name__ == '__main__':
    n = int(input('Enter a number between 0 and 99'))
    l = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
         'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    l1 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    out = ''
    if n == 0:
        out = 'ZERO'
    elif n < 20:
        out = l[n].upper()
    elif n < 100:
        out = (l1[n // 10] + ' ' + l[n % 10]).upper()
    print(out)

    # elif n < 1000:
    #     out = (l[n//100] + ' Hundred ' + l[n%10]).upper()
    #     out = (l[n//100] + ' Hundred ' +l1[n//100]+' '+ l[n%10]).upper()
