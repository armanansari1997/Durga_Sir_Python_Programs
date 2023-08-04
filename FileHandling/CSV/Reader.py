import csv

with open('emp.csv', 'r') as f:
    r = csv.reader(f)

    print(type(r))  # <class '_csv.reader'>
    # converting 'csv.reader' type to 'list' data type
    data = list(r)
    # printing the data as list type
    print(data)

    # printing the data as rows and columns
    for row in data:
        for col in row:
            print(col, end=' ')
        print()
