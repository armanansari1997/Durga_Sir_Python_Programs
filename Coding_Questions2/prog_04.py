# if no % 3 Fizz
# if no % 5 Fuzz
# if no % 3 and no % 5 FizzFuzz
# else no

def fizz_fuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzFuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Fuzz'
    else:
        return n


for i in range(1, 21):
    print(fizz_fuzz(i))
