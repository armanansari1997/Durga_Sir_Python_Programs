import pickle


class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print(f'Employee No : {self.eno}, Employee Name : {self.ename}, Employee Salary : {self.esal}, '
              f'Employee Address : {self.eaddr}')


e = Employee(100, 'Arman', 1000, 'Kolkata')
# Pickling an object
with open('serial.arm', 'wb') as f:
    pickle.dump(e, f)
print('Pickling is Completed !!!')

# Unpickling an object
with open('serial.arm', 'rb') as f:
    new_obj = pickle.load(f)
print('Unpickling an Object')
new_obj.display()
print('Unpickling an object is completed !!!')

