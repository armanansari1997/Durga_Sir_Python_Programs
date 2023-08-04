import csv

with open('emp.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ENO', 'ENAME', 'ESAL', 'EADDR'])
    while True:
        eno = int(input('Enter the Employee Number : '))
        ename = input('Enter the Employee Name : ')
        esal = float(input('Enter the Employee Salary : '))
        eaddr = input('Enter the Employee Address')

        w.writerow([eno, ename, esal, eaddr])

        option = input('Do you want to insert one more record [yes/no]')
        if option.lower() == 'no':
            break

print('Writing data to the file completed successfully')
