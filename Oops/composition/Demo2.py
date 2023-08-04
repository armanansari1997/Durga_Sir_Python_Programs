class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def get_info(self):
        print(f'Car Name : {self.name}, Model : {self.model}, Color : {self.color}')


class Employee:
    def __init__(self, ename, eno, car):
        self.ename = ename
        self.eno = eno
        self.car = car

    def emp_info(self):
        print('Employee Name : ', self.ename)
        print('Employee Number : ', self.eno)
        print('Employee Car Info')
        self.car.get_info()


car = Car('Innova', '2.5v', 'Grey')
emp = Employee('Durga', 2890, car)
emp.emp_info()



