class Outer:
    def __init__(self):
        print('Outer Object Creation')

    class Inner:
        def __init__(self):
            print('Inner Object Creation')

        def m1(self):
            print('Inner Class Method')

        @classmethod
        def m2(cls):
            print('Inner Class Classmethod')

#1
# o = Outer()
# i = o.Inner()
# i.m1()
#2
# o.Inner().m1()
# o.Inner.m2()
#3
Outer().Inner().m1()
Outer().Inner.m2()
