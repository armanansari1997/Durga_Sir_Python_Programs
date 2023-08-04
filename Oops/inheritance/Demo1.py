class P:
    def m1(self):
        print('Parent Method')


class C(P):
    def m2(self):
        print('Child Method')


c = C()
c.m1()  # Parent Method
c.m2()  # Child Method
