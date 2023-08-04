# Q) Where we can declare instance variables
# inside constructor by using self
# inside instance method by using self
# outside the class by using object reference

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30


t = Test()
print(t.__dict__) #  {'a': 10, 'b': 20}
t.m1()
print(t.__dict__) #  {'a': 10, 'b': 20, 'c': 30}
t.d = 40
print(t.__dict__) #  {'a': 10, 'b': 20, 'c': 30, 'd': 40}


# eg-2
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30


t1 = Test()
t1.m1()
t1.d = 40
t2 = Test()
print(t1.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(t2.__dict__)  # {'a': 10, 'b': 20}


# Q) How to access instance variables?
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def display(self):
        print(self.a, self.b)


t = Test()
t.display()  # 10 20
print(t.a)  # 10
print(t.b)  # 20


# Q) How to delete instance variables
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.c


t1 = Test()
t1.m1()
print(t1.__dict__)  # {'a': 10, 'b': 20, 'd': 40}
t2 = Test()
del t2.b, t2.d # delete operation
print(t2.__dict__) # {'a': 10, 'c': 30}


# Q) How to update instance variables
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20


t1 = Test()
t1.a = 888
t1.b = 999
t2 = Test()
print('t1 :', t1.a, t1.b)  # t1 : 888 999
print('t2 :', t2.a, t2.b)  # t2 : 10 20



