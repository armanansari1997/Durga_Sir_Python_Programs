# Serialization / Pickling
import pickle

from emp import Employee

f = open('receiver.abc', 'wb')
while True:
    eno = int(input('Enter Employee Number'))
    ename = input('Enter Employee Name')
    esal = float(input('Enter Employee Salary'))
    eaddr = input('Enter Employee Address')
    # Creating Object of Employee Class
    e = Employee(eno, ename, esal, eaddr)
    # Serializing / Pickling
    pickle.dump(e, f)
    option = input('Do you want to serialize another object [yes/no]')
    if option.lower() == 'no':
        break
