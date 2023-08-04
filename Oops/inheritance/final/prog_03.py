# How to call parent class 'static' and 'class method' from child class static method???

class Parent:
    @classmethod
    def m1(cls):
        print('Parent class @classmethod')

    @staticmethod
    def m2():
        print('Parent class @staticmethod')


class Child(Parent):

    @staticmethod
    def m2():
        super(Child, Child).m1()
        super(Child, Child).m2()


# calling child class @staticmethod using child class name
Child.m2()
