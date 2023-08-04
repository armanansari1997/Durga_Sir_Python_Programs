class Parent:
    a = 10

    def __init__(self):
        print('Parent Constructor')

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('parent class @classmethod')

    @staticmethod
    def m3():
        print('Parent class @staticmethod')


class Child(Parent):
    def __init__(self):
        print('Child Constructor')

    def method1(self):
        print(super().a)
        self.m1()
        self.m2()
        self.m3()
        super().__init__()


c = Child()
c.method1()