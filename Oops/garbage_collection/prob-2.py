import time


class Test:
    def __init__(self):
        print('Constructor Execution...')

    def __del__(self):
        print('Fulfilling last wish and performing cleanup activities')


t1 = Test()
t2 = Test()
print('End of Application')

# output:
# Constructor Execution...
# Constructor Execution...
# End of Application
# Fulfilling last wish and performing cleanup activities
# Fulfilling last wish and performing cleanup activities
