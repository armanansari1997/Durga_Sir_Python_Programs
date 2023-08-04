class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('Hi', self.name)
        print('Your marks are :', self.marks)

    def grade(self):
        if self.marks >= 60:
            print('you got First grade')
        elif self.marks >= 50:
            print('you got second grade')
        elif self.marks >= 35:
            print('you got third grade')
        else:
            print('you are failed')


n = int(input('Enter no. of student : '))
for i in range(n):
    name = input('Enter student name : ')
    marks = int(input('Enter marks : '))
    s = Student(name, marks)
    s.display()
    s.grade()
    print('--------------------------')