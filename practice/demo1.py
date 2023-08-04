class A:
    def monkey(self):
        print('Monkey Defined')


def updated_monkey(self):
    print('Updated Monkey')


A.monkey = updated_monkey
obj = A()
obj.monkey()
