import os
from datetime import *

statistics = os.stat('abc.txt')
print('File size in bytes :', statistics.st_size)

print('Last modified Time :')
print(datetime.fromtimestamp(statistics.st_mtime))
