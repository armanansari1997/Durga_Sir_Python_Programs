if __name__ == '__main__':
    print('{},{},{}'.format('a', 'b', 'c'))
    print('{}:{}:{}'.format('a', 'b', 'c'))
    print('{0}:{1}:{2}'.format('a', 'b', 'c'))
    print('{2}:{1}:{0}'.format('a', 'b', 'c'))
    print('{1}:{2}:{0}'.format('a', 'b', 'c'))
    name = 'Alex Peter'
    designation = 'Software Engineer'
    salary = 50000
    print('Hello {n}, your designation is {d}, And your salary is RS {s}'.format(n=name, d=designation, s=salary))
