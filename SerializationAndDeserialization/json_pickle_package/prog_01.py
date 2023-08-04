import jsonpickle


class Employee:
    def __init__(self, eno, ename, esal, eaddr, isMarried):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
        self.isMarried = isMarried

    def display(self):
        print('Employee Number : {}, Employee Name: {}, Employee Salary : {}, Employee Address : {}'
              'Is Married : {}'.format(self.eno, self.ename, self.esal, self.eaddr, self.isMarried))


# Creating Object of Employee class
e = Employee(100, 'Durga', 1000.0, 'Hyderabad', True)

# Serialization to json_string
json_string = jsonpickle.encode(e)
print(json_string)

# Serializing to the json file
with open('emp.json', 'w') as f:
    f.write(json_string)

# Deserializing from json_string
e2 = jsonpickle.decode(json_string)

# Calling Employee class 'display' function using new object reference
e2.display()
print(type(e2))  # <class '__main__.Employee'>

# Deserializing from json file
with open('emp.json', 'r') as f:
    # reading line and storing data into the json_string
    json_string = f.readline()

e3 = jsonpickle.decode(json_string)
e3.display()
