class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print(f'Employee No : {self.eno}, Employee Name : {self.ename}, Employee Salary : {self.esal}, '
              f'Employee Address : {self.eaddr}')