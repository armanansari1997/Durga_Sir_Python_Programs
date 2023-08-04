# overloading 'string method'

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


s1 = Student('Durga', 101, 95)
s2 = Student('Ravi', 102, 98)

print(s1)  # <__main__.Student object at 0x0000016EFDF3BC10>
print(s2)  # <__main__.Student object at 0x0000016EFDF3BBB0>

# Solution :
# prog_08