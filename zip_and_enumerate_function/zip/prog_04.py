# How to unzip
names = ['Manjeet', 'Nikhil', 'Simba', 'Astha']
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(names, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# Printing resultant values
print('The zipped result is :', mapped)

# unzipping values
namz, roll_noz, markz = zip(*mapped)
print('The unzipped result :\n', end='')

# printing initial lists
print('The name list is :',namz)
print('The roll no list is :',roll_noz)
print('The marks list is :',markz)