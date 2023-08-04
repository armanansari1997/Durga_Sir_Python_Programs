# If we use 'with' statement then we don't need to close the file explicitly

with open('abc.txt', 'r') as f1, open('xyz.txt', 'w') as f2:
    # Read the data from 'abc.txt' file
    data = f1.read()

    # Write the data to the 'xyz.txt' file
    f2.write(data)

    # Checking whether file is closed or not
    print(f1.closed)  # False
    print(f2.closed)  # False

# Checking whether file is closed or not
print(f1.closed)  # True
print(f2.closed)  # True
