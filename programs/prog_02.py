import os

try:
    print('stmt-1')
    # os._exit(1000)
except:
    print('stmt-2')
finally:
    print('finally')

