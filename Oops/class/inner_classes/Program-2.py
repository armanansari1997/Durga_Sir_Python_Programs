# Nesting Inner Class
class Outer:
    def __init__(self):
        print('Outer Object Creation')

    class Inner:
        def __init__(self):
            print('Inner object creation')

        class InnerInner:
            def __init__(self):
                print('InnerInner Object Creation')

            def m1(self):
                print('InnerInner class method')

            @staticmethod
            def m2():
                print('InnerInner Class classmethod')


# 1
o = Outer()
i = o.Inner()
ii = i.InnerInner()
ii.m1()  # InnerInner class method
ii.m2()  # InnerInner Class classmethod
i.InnerInner.m2()  # InnerInner Class classmethod (Recommended)
print('---------------------')

# 2
o = Outer()
o.Inner().InnerInner().m1()
print('------------------')
# 3
Outer().Inner().InnerInner().m1()
Outer().Inner().InnerInner.m2()
