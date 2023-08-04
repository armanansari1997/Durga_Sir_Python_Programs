class Test:
    def __init__(self):
        print('Constructor Called')


t1 = Test()  # Constructor Called
t2 = Test()  # Constructor Called
t3 = Test()  # Constructor Called


#  eg-2
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


s1 = Student('Arman', 101, 99)
print(s1.name, s1.roll_no, s1.marks)  # Arman 101 99
s2 = Student('Farhan', 102, 100)
print(s2.name, s2.roll_no, s2.marks)  # Farhan 102 100


# eg-3
class Test:
    def m1(self):
        print('method Calling')


t = Test()
t.m1()  # method Calling


# eg-4
class Test:
    def __init__(self):
        print('Constructor Called')


print('Eg-4')  # Constructor Called
t = Test()
print(t.__init__())
print(t.__init__())
print(t.__init__())


# Constructor Called
# None
# Constructor Called
# None
# Constructor Called
# None


# eg-5
class Test5:

    def __init__(self):
        print('First Constructor Called')

    def __init__(self, x):
        print('Second Constructor Called')


print('Eg-5')
t = Test5()
