class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


n = int(input('Enter no. of students : '))
students = []
for i in range(n):
    s = Student()
    name = input('Enter student name : ')
    marks = int(input('Enter student marks : '))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)

for student in students:
    print('Hello', student.getName())
    print('your marks are : ',student.getMarks())
    print('-----------------------')