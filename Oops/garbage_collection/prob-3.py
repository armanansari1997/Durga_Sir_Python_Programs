import time


class Test:
    def __init__(self):
        print('Constructor Execution...')

    def __del__(self):
        print('Fulfilling last wish and performing cleanup activities')


t1 = Test()
t2 = Test()
t1 = None
t2 = None
print('End of Application')

# output:
# Constructor Execution...
# Constructor Execution...
# Fulfilling last wish and performing cleanup activities
# Fulfilling last wish and performing cleanup activities
# End of Application
