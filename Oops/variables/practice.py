class Student:
    school_name = 'DURGASOFT'  # static variable

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def info(self):
        x = 10
        for i in range(x):
            print(i)


s = Student('Arman', 101)
s.info()
print(s.school_name)  # DURGASOFT
print(Student.school_name)  # DURGASOFT
print(Student.__dict__)  # {'school_name': 'DURGASOFT', '__init__': <function Student.__init__ at 0x00000229B34AA290>,etc}
print(s.__dict__)  # {'name': 'Arman', 'roll_no': 101}
