if __name__ == '__main__':
    print('{}, {}, {}'.format('a','b','c')) # a, b, c
    print('{}:{}:{}'.format('a','b','c')) # a:b:c
    print('{0}, {1}, {2}'.format('a','b','c')) # a, b, c

    print('{2}, {1}, {0}'.format('a','b','c')) # 'c, b, a'

    # Using Keyword Arguments
    name = 'Arman'
    salary = 40000
    designation = 'Software Engineer'
    print('Hello {n}, Your designation is {d}, And your salary is {s}'.format
          (n=name,s=salary,d=designation))

    # unpacking argument sequence
    print('{2}, {1}, {0}'.format(*'abc')) # 'c, b, a'

    # Using the comma as a th  ousands separator:
    print('{:,}'.format(1234567890)) # '1,234,567,890'
