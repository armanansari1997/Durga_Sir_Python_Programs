# various places to declare the static variables

class Test:
    a = 10  # static variable

    def __init__(self):
        Test.b = 20  # static variable

    def m1(self):
        Test.c = 30  # static variable

    @classmethod
    def m2(cls):
        Test.d = 40  # static variable
        cls.e = 50  # static variable

    @staticmethod
    def m3():
        Test.f = 60  # static variable


t = Test()
t.m1()
Test.m2()
Test.m3()
Test.g = 70  # static variable
print(Test.__dict__)


# Q) How to access static variables
# 1) inside constructor by using 'self' or 'classname'
# 2) inside instance method by using 'self' or 'classname'
# 3) inside class method by using 'cls' or 'classname'
# 4) inside static method by using 'classname'
# 5) outside class by using 'object reference' / 'classname'

class Test:
    a = 10

    def __init__(self):
        print('Inside Constructor', self.a)
        print('Inside Constructor', Test.a)

    def m1(self):
        print('Inside instance method :', self.a)
        print('Inside instance method :', Test.a)

    @classmethod
    def m2(cls):
        print('Inside Class method :', cls.a)
        print('Inside Class method :', Test.a)

    @staticmethod
    def m3():
        print('Inside Static method :', Test.a)


t = Test()
t.m1()
Test.m2()
Test.m3()
print('Outside Class using object reference :', t.a)
print('Outside class using class name :', Test.a)


# Q) Where we can modify the value of static variable


class Test:
    a = 10

    def __init__(self):
        Test.a = 20


print(Test.a)  # 10
t = Test()
print(Test.a)  # 20


# eg-2
class Test:
    a = 10

    def __init__(self):
        Test.a = 20

    def m1(self):
        Test.a = 30

    @classmethod
    def m2(cls):
        cls.a = 40
        Test.a = 50

    @staticmethod
    def m3():
        Test.a = 60


t = Test()
t.m1()
t.m2()
t.m3()
print(t.a)  # 60
Test.a = 70
print(t.a)  # 70


# Program  set-1 about static and instance variables

# eg-1
class Test:
    a = 10

    def m1(self):
        self.a = 888  # instance variable


t = Test()
t.m1()
print(t.a)  # 888 (instance variable)
print(Test.a)  # 10 (static variable)


# eg-2
class Test:
    a = 10

    def m1(self):
        Test.a = 888  # static variable


t = Test()
print(t.a)  # 10
t.m1()
print(t.a)  # 888


# eg-3
class Test:
    a = 10

    def __init__(self):
        self.b = 20


t1 = Test()
t2 = Test()
print('t1 :', t1.a, t1.b)  # t1 : 10 20
print('t2 :', t2.a, t2.b)  # t2 : 10 20
t1.a = 888
t1.b = 999
print('t1 :', t1.a, t1.b)  # t1 : 888 999
print('t2 :', t2.a, t2.b)  # t2 : 10 20


# eg-4

class Test:
    a = 10

    def __init__(self):
        self.b = 20


t1 = Test()
t2 = Test()
print('t1 :', t1.a, t1.b)  # t1 : 10 20
print('t2 :', t2.a, t2.b)  # t2 : 10 20
Test.a = 888
Test.b = 999
print('t1 :', t1.a, t1.b)  # t1 : 888 20
print('t2 :', t2.a, t2.b)  # t2 : 888 20
print('Test :', Test.a, Test.b) # Test : 888 999

# Set-2
# eg-5


class Test:
    a = 10

    def __init__(self):
        self.b = 20


t1 = Test()
t2 = Test()
Test.a = 888
t1.b = 999
print('t1 :', t1.a, t1.b)  # t1 : 888 999
print('t2 :', t2.a, t2.b)  # t2 : 888 20


# eg-6

class Test:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        self.a = 888
        self.b = 999


t1 = Test()
t2 = Test()
t1.m1()
print('t1 :', t1.a, t1.b)  # t1 : 888 999
print('t2 :', t2.a, t2.b)  # t2 : 10 20

# eg-7


class Test:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        self.a = 888
        self.b = 999


t1 = Test()
t2 = Test()
t1.m1()
t2.m1()
print('t1 :', t1.a, t1.b)  # t1 : 888 999
print('t2 :', t2.a, t2.b)  # t2 : 888 999

# eg-8


class Test:
    a = 10

    def __init__(self):
        self.b = 20

    @classmethod
    def m1(cls):
        cls.a = 888
        cls.b = 999


t1 = Test()
t2 = Test()
t1.m1()
print('t1 :', t1.a, t1.b)  # t1 : 888 20
print('t2 :', t2.a, t2.b)  # t2 : 888 20
print('Test : ', Test.a, Test.b)  # Test : 888 999

# Q) How to delete static variables


class Test:
    a = 10

    @classmethod
    def m1(cls):
        # del Test.a
        del cls.a


t = Test()
t.m1()
# print(t.a)  # AttributeError: 'Test' object has no attribute 'a'
# print(Test.a)  # AttributeError: type object 'Test' has no attribute 'a'
print(Test.__dict__) # 'a' is not present in this dictionary

# eg-2


class Test:
    a = 10

    def __init__(self):
        Test.b = 20
        del Test.a

    def m1(self):
        Test.c = 30
        del Test.b

    @classmethod
    def m2(cls):
        Test.d = 40
        del Test.c

    @staticmethod
    def m3():
        Test.e = 50
        del Test.d


print(Test.__dict__)  # {'a': 10,etc}
t = Test()
print(Test.__dict__)  # {'b': 20,etc}
t.m1()
print(Test.__dict__)  # {'c':30,etc}
Test.m2()
print(Test.__dict__)  # {'d': 40,etc}
Test.m3()
print(Test.__dict__)  # {'e': 50,etc}


# eg-2


class Test:
    a = 10


t = Test()
print(t.a)  # 10
print(Test.a)  # 10
# del t.a  # AttributeError: a
del Test.a
print(Test.a)  # AttributeError: type object 'Test' has no attribute 'a'
