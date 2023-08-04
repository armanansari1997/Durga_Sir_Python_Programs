import pickle


class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('{} {} {} {}'.format(self.eno, self.ename, self.esal, self.eaddr))


e = Employee(100, 'Durga', 50000.0, 'Hyderabad')

# Serializing / pickling
with open('practice.abc', 'wb') as f:
    pickle.dump(e, f)
print('Pickling of Employee Object is completed')

# Deserialization / Unpickling
with open('practice.abc', 'rb') as f:
    emp = pickle.load(f)
print('Unpickling of Employee Object is completed')
print('Printing Employee Information')
emp.display()
