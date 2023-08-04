class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_and_drink(self):
        print('Eat Biryani and Drink Water')


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def work(self):
        print('Coding Python Programs')

    def emp_info(self):
        print('Employee Name : ', self.name)
        print('Employee Age : ', self.age)
        print('Employee Number : ', self.eno)
        print('Employee Salary : ', self.esal)


emp = Employee('Durga', 50, 872425, 50000)
emp.eat_and_drink()
emp.work()
emp.emp_info()
