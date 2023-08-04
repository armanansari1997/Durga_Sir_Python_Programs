import time


class Test:
    def __init__(self):
        print('Constructor Execution...')

    def __del__(self):
        print('Destructor Execution...')


l = [Test(), Test(), Test()]
del l
time.sleep(5)
print('End of Application')

# output:
# Constructor Execution...
# Constructor Execution...
# Constructor Execution...
# Destructor Execution...
# Destructor Execution...
# Destructor Execution...
# End of Application
