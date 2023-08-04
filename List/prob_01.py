if __name__ == '__main__':
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = input('Enter a String')
    out = ''
    # for ch in s:
    #     if ch in vowels:
    #         if ch not in out:
    #             out += ch
    # print(out)
    # print(len(out))

    # for ch in vowels:
    #     if ch in s:
    #         out += ch
    # print(out)
    # print(len(out))

    out = [ch for ch in vowels if ch in s]
    print(out)
    print('The length of vowels is ',len(out))
