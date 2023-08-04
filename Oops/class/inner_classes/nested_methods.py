class Test:
    def m1(self):
        def calc(a, b):
            print('The Sum :', a + b)
            print('The Product :', a * b)
            print('The difference :', a - b)
            print('The average :', (a + b) / 2)

        calc(10, 20)
        print('---------------------')
        calc(100, 200)
        print('---------------------')
        calc(1000, 2000)


t = Test()
t.m1()
