import time


class Test:
    def __init__(self):
        print('Constructor Execution...')

    def __del__(self):
        print('Destructor Execution...')


t1 = Test()
t2 = t1
t3 = t2
del t1
time.sleep(5)
print('Object not destroyed after deleting t1')
del t2
print('Object not destroyed even after deleting t2')
time.sleep(5)
print('Deleting last reference...')
del t3
print('End of Application')

# output:
# Constructor Execution...
# Object not destroyed after deleting t1
# Object not destroyed even after deleting t2
# Deleting last reference...
# Destructor Execution...
# End of Application
