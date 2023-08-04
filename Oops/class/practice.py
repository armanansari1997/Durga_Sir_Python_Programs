# Accessing members of one class inside another class

class Employee:
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print('Employee Number : ', self.eno)
        print('Employee Name : ', self.ename)
        print('Employee Salary : ', self.esal)


class Manager:

        def update_emp_sal(self):
            emp.esal += 10000
            emp.display()


emp = Employee(101, 'Durga', 45000)
Manager.update_emp_sal(emp)