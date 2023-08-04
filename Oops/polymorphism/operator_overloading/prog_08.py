# overloading 'string method'

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        # return type must be string only
        return f'Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}'


s1 = Student('Durga', 101, 95)
s2 = Student('Ravi', 102, 98)

print(s1)  # Name: Durga, Roll No: 101, Marks: 95
print(s2)  # Name: Ravi, Roll No: 102, Marks: 98

