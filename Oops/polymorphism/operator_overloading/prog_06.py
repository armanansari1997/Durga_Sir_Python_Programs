# Program to overload multiplication operator to work on Employee objects

class Employee:
    def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

    def __mul__(self, other):
        res = self.salary_per_day * other.workingDays
        return res


class TimeSheet:
    def __init__(self, name, working_days):
        self.name = name
        self.workingDays = working_days

    def __mul__(self, other):
        res = self.workingDays * other.salary_per_day
        return res


e = Employee('Ravi', 500)
t = TimeSheet('Durga', 25)

print('The month salary :', e*t)  # The month salary : 12500
print('The month salary :', t*e)  # The month salary : 12500

