# Demo program for Deserialization from "json String"

import json

json_string = '''{
             "name": "durga",
             "age": 35,
             "salary": 30000.0,
             "isMarried": true,
             "isHavingGF": null
}'''

employee = json.loads(json_string)
print(type(employee))

# print in 1 line
print(employee)

# print line by line
print()
print('Employee Name :', employee['name'])  # employee.get('name')
print('Employee Age :', employee['age'])  # employee.get('age')
print('Employee Salary :', employee['salary'])  # employee.get('salary')
print('Is Married :', employee['isMarried'])  # employee.get('isMarried')
print('Is Having GF:', employee.get('isHavingGF'))  # employee['isHavingGF']

# printing using another way
print()
for k, v in employee.items():
    print(k, ':', v)
