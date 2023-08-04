import time


class Test:
    def __init__(self):
        print('Constructor Execution...')

    def __del__(self):
        print('Fulfilling last wish and performing cleanup activities')


t = Test()
t = None
print('End of Application')

# output:
# Constructor Execution...
# Fulfilling last wish and performing cleanup activities
# End of Application
