class Parent:
    def __init__(self):
        print('Parent Constructor')

    def m1(self):
        print('Parent class Instance Method')

    @classmethod
    def m2(cls):
        print('Parent class @classmethod')

    @staticmethod
    def m3():
        print('Parent class @staticmethod')


class Child(Parent):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    @classmethod
    def m2(cls):
        # super().__init__()  # Error
        # super().m1()  # Error
        super().m2()
        super().m3()

    @staticmethod
    def m3():
        # super().__init__()  # Error
        # super().m1()  # Error
        # super().m2()  # Error
        # super().m3()  # Error
        pass


c = Child()
c.m1()
c.m2()
c.m3()
