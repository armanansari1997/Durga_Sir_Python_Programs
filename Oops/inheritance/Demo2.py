class Parent:
    a = 10

    def __init__(self):
        print('Parent Constructor')
        self.b = 20

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')


class Child(Parent):
    pass


c = Child()  # Parent Constructor
print(c.a)  # 10
print(c.b)  # 20
c.m1()  # Parent instance method
c.m2()  # parent class method (Child.m2())
c.m3()  # parent static method (Child.m3())
# Child.m2()
# Child.m3()
