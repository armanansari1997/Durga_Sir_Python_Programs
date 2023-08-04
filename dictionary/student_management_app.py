if __name__ == '__main__':
    n = int(input('Enter the no. of student :'))
    d = {}
    for i in range(n):
        name = input('Enter student name: ')
        marks = int(input('Enter student marks: '))
        d[name] = marks
    print('Student insertion is completed')
    print('*' * 30)
    print('NAME', '\t\t', 'MARKS')
    print('*' * 30)
    for k, v in d.items():
        print(k, '\t\t', v)
    print('Searching is started')
    while True:
        name = input('Enter student name to search the marks: ')
        marks = d.get(name, -1)
        if marks == -1:
            print('Student not found')
        else:
            print('Marks of {} is {}'.format(name, marks))
        option = input('Do you want to check for any other student marks (yes/no): ')
        if option.lower() == 'no':
            break
    print('Thanks for using our application!!!')
