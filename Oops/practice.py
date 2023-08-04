class Student:
    """This class developed by Arman for Test"""

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def talk(self):
        print('Student Name :', self.name)
        print('Student Roll No :', self.roll_no)
        print('Student Marks :', self.marks)


s1 = Student('Arman', 101, 90)
s2 = Student('Farhan', 102, 91)
s1.talk()
print('---------------------')
s2.talk()
print('--------------------')
print(s1.name)  # Arman
print(s1.roll_no)  # 101
print(s1.marks)  # 90
print('----------------------')
# TO print docstring
print(s1.__doc__)  # This class developed by Arman for Test
print(Student.__doc__)  # This class developed by Arman for Test
