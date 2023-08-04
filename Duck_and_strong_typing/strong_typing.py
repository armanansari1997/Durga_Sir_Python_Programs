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
    if hasattr(obj, 'walk'):  # checking whether this method exist or not in this object
        obj.walk()
    if hasattr(obj, 'talk'):  # checking whether this method exist or not in this object
        obj.talk()


d = Duck()
my_function(d)  # thapak thapak thapak thapak

h = Horse()
my_function(h)  # tabdak tabdak tabdak tabdak

c = Cat()
my_function(c)  # Meow Meow
