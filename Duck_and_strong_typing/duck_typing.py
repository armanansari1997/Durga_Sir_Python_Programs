class Duck:
    def walk(self):
        print('thapak thapak thapak thapak')


class Horse:
    def walk(self):
        print('tabdak tabdak tabdak tabdak')


class Cat:
    def talk(self):
        print('Meow Meow')


def my_function(obj):
    obj.walk()


d = Duck()
my_function(d)

h = Horse()
my_function(h)

c = Cat()
# my_function(c)  # AttributeError: 'Cat' object has no attribute 'walk'. Did you mean: 'talk'?
