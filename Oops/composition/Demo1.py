class Engine:
    def use_engine(self):
        print('Engine specific functionality')


class Car:
    def __init__(self):
        self.engine = Engine()

    def use_car(self):
        print('Car required engine functionality')
        self.engine.use_engine()


c = Car()
c.use_car()

# Output:
# Car required engine functionality
# Engine specific functionality
