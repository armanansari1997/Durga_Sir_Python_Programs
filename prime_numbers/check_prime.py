if __name__ == '__main__':
    n = int(input('Enter any number'))
    if n <= -1:
        print('Number is not a prime : ',n)
    else:
        is_prime = True
        for i in range(2,n//2+1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime == True:
            print('Number is prime : ', n)
        else:
            print('Number is not prime : ', n)