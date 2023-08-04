import pickle
from emp import Employee

print('Pickling an Object')
f = open('serial2.abc', 'wb')
while True:
    eno = int(input('Enter ENO : '))
    ename = input('Enter ENAME : ')
    esal = float(input('Enter ESAL : '))
    eaddr  = input('Enter EADDR : ')
    e = Employee(eno, ename, esal, eaddr)
    pickle.dump(e, f)   # to pickle we used dump(object, file) function
    option = input('Do you want to serialize another object [yes/no]')
    if option.lower() == 'no':
        f.close()
        break

print('Serialization/Pickling of multiple objects are completed')
