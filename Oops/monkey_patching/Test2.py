class Test:
    def __init__(self, x):
        self.x = x

    def get_data(self):
        print('Some code to fetch data from database')

    def f1(self):
        self.get_data()

    def f2(self):
        self.get_data()


t1 = Test(5)
t1.f1()  # Some code to fetch data from database
t1.f2()  # Some code to fetch data from database


def get_new_data(self):
    print('Some code to fetch data from test data')


# replacing address of "get_data" with "get_new_data"
Test.get_data = get_new_data
t1.f1()  # Some code to fetch data from test data
t1.f2()  # Some code to fetch data from test data
