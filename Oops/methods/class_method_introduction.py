class Bird:
    wings = 2

    @classmethod
    def fly(cls, name):
        print(f'{name} flying with {Bird.wings} wings')


Bird.fly('Parror')
Bird.fly('Eagle')


# eg-2


# Program to track no. of objects created for a class
class Test:
    count = 0

    def __init__(self):
        Test.count += 1

    @classmethod
    def get_no_of_objects(cls):
        print('The number of objects created :', cls.count)


t = Test()
t = Test()
t = Test()
t = Test()
Test.get_no_of_objects()
print(Test.count)  # 4
