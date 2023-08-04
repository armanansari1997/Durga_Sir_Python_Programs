# We declare a method with same name in both parent and child classes but with different implementations

class Parent:
    def marry(self):
        print('Subbalaxmi/Appalamma')


class Child(Parent):
    def marry(self):
        print('Katrina Kaif')


c = Child()
c.marry()
