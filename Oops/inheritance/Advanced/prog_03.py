# How to call method of a particular superclass

class Parent:
    # static variable
    a = 888

    def __init__(self):
        # instance variable
        self.b = 999


class Child(Parent):
    # instance method
    def m1(self):
        print(self.a)
        print(self.b)
        print(super().a)
        # print(super().b)  # AttributeError: 'super' object has no attribute 'b'
#       Note: 1) we cannot use super() to access parent class instance variable from child class
#             2) we should use 'self' keyword only


c = Child()
c.m1()
