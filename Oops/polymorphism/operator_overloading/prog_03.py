# overloading of > and <= Operators for Student class object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student('Durga', 100)
s2 = Student('Ravi', 200)
s3 = Student('Shiva', 300)


res = s1 < s2
print(res)

# Output :
# res = s1 < s2
# TypeError: '<' not supported between instances of 'Student' and 'Student'

# Solution:
# prog_04