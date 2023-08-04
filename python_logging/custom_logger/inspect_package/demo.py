import inspect


def get_info():
    print(inspect.stack())
    print(inspect.stack()[1])
    print('Caller module :', inspect.stack()[1][1])
    print('Caller function :', inspect.stack()[1][3])

