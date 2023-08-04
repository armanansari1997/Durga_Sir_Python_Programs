class Test:

    @staticmethod
    def average(list1):
        result = sum(list1) / len(list1)  # here 'result' is a local variable
        return result

    @staticmethod
    def wish(name):
        for i in range(10):  # here 'i' is a local variable
            print('Good Evening', name)


t = Test()
list1 = [10, 20, 30, 40]
print(Test.average(list1))  # 25.0
# Test.wish('Arman')
t.wish('Arman')

