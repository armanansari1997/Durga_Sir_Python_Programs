# static method introduction and demo program
# eg-1
class Test:

    @staticmethod
    def m1():
        pass


Test.m1()


# eg-2


class Test:
    @staticmethod
    def add(a, b):
        print('The sum :', (a + b))

    @staticmethod
    def product(a, b):
        print('The Product :', (a * b))

    @staticmethod
    def average(a, b):
        print('The average :', (a + b) / 2)


Test.add(10, 20)  # The sum : 30
Test.product(10, 20)  # The Product : 200
Test.average(10, 20)  # The average : 15.0


# Q) If we are not using any decorator for method?
# If we are calling by using object reference , then it is treated as instance method
# If we are calling by using class name , then it is treated as static method
# eg-1
class Test:
    # def m1(): # TypeError: Test.m1() takes 0 positional arguments but 1 was given
    #    print('Some Method')
    pass


t = Test()


# t.m1()

# eg-2


class Test:
    def m1(x):
        print('some method')


t = Test()
t.m1()  # some method


# t.m1(10)  # TypeError: Test.m1() takes 1 positional argument but 2 were given


# eg-3


# class Test:
#     def m1():
#         print('Some method')
#
#
# Test.m1()


# eg-4


class Test:
    def m1(x):
        print('Some method')


Test.m1(10)  # Some method
# Test.m1()  # TypeError: Test.m1() missing 1 required positional argument: 'x'

t = Test()
t.m1()  # Some method
