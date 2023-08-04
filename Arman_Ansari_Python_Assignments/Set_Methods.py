if __name__ == '__main__':
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)  # show that duplicates have been removed {'orange', 'pear', 'banana', 'apple'}

    print('orange' in basket)  # True
    print('crabgrass' in basket)  # False

    # Demonstrate set operations on unique letters from two words
    a = set('abracadabra')
    b = set('alacazam')
    print(a)  # unique letters in a {'a', 'r', 'b', 'c', 'd'}
    print(b)  # letters in a but not in b {'r', 'd', 'b'}
