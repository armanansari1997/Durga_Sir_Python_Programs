class Test:
    def __init__(self):
        print('Constructor Execution....')

    def __del__(self):
        print('Destructor Execution....')


# t = Test()
# print('End of Application')

t = Test()
t = None
print('End of Application')