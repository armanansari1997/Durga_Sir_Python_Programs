#  eg-1
class Test:
    def __init__(self):
        print(id(self))  # 1872209538272


t = Test()
print(id(t))  # 1872209538272


#  eg-2
class Test:
    def __init__(self):
        print('Constructor Called')

    def m1(self, x):
        print('x value is %d' % x)


t = Test()  # Constructor Called
t.m1(10)  # x value is 10
