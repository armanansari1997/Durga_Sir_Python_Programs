# From class method of Child class, how to call parent class 'constructor' and
# 'instance methods' indirectly???

class Parent:
    def __init__(self):
        print('Parent Constructor')

    def m1(self):
        print('Parent class Instance Method')


class Child(Parent):

    @classmethod
    def m2(cls):
        super(Child, cls).__init__(cls)
        super(Child, cls).m1(cls)


# calling a @classmethod using class name
Child.m2()
