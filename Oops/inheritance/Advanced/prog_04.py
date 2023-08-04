class Parent:
    a = 888

    def __init__(self):
        self.b = 999


class Child(Parent):
    # Constructor Overriding
    def __init__(self):
        self.b = 20

    def m1(self):
        print(self.b)


c = Child()
c.m1()  # 20
