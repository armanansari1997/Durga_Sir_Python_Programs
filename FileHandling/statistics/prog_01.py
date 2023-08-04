import os

statistics = os.stat('abc.txt')
print(statistics)

for info in statistics:
    print(info)