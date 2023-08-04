class Parent:
    def __init__(self, name, age, height, weigth):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weigth

    def display(self):
        print('Name :', self.name)
        print('Age :', self.age)
        print('Height :', self.height)
        print('Weight :', self.weight)


class Child(Parent):
    def __init__(self, name, age, height, weigth, roll_no, marks):
        # self.name = name
        # self.age = age
        # self.height = height
        # self.weight = weigth
        super().__init__(name, age, height, weigth)
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        # print('Name :', self.name)
        # print('Age :', self.age)
        # print('Height :', self.height)
        # print('Weight :', self.weight)
        super().display()
        print('Roll No :', self.roll_no)
        print('Marks :', self.marks)


c = Child('Ravi', 24, 5.6, 70, 101, 95)
c.display()


