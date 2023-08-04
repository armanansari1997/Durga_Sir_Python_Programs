# eg-1
class Human:
    class Head:
        def talk(self):
            print('Talking...')

        class Brain:
            def think(self):
                print('Thinking...')


human = Human()
head = human.Head()
head.talk()  # Talking...
b = head.Brain()
b.think()  # Thinking...

# eg-2 (Recommended)


class Human:
    def __init__(self, name):
        print('Human Constructor')
        self.name = name
        self.head = self.Head() # Inner Object Creation
        self.brain = self.Head().Brain() # InnerInner Object Creation

    def info(self):
        print('Hello, myself', self.name)
        self.head.talk()
        self.head.brain.think()
        self.brain.think()

    class Head:
        def __init__(self):
            print('Head Constructor')
            self.brain = self.Brain()

        def talk(self):
            print('Talking...')

        class Brain:
            def __init__(self):
                print('Brain Constructor')

            def think(self):
                print('Thinking...')


human = Human('Arman')
#   Human Constructor
#   Head Constructor
#   Brain Constructor
human.info()
# Hello, myself Arman
# Talking...
# Thinking...

