# WAP to generate fake Employee Database Testing?

# 1) Employee Name
# 2) Employee Number
# 3) Employee Salary
# 4) Employee City
# 5)Employee Mobile Number
# 6) Designation

# 1) Employee Name Requirements:
"""
    1) The name should contain 3 to 10 characters
    2) First Character should be upper case and remaining characters should be in lower case
"""
# 2) Employee Number Requirements:


"""
    1) Employee Number Should starts with 'e-' followed by 4 digits
    eg:- e-1234
"""
# 3) Employee Salary Requirement
"""
    1) Employee Salary should be float value from 10000 to 50000
"""

# 4) Employee City should be from ['Hyderabad', 'Chennai', 'Bangalore', 'Kolkata',
# 'Pune', 'Delhi', 'Mumbai']

# 5) Mobile Number should contain exactly 10 digits where first number should be 6 to 9.
# No restrictions on remaining digits eg:- 9848098480

# 6) Employee Designation should be from : ['Software Engineer', 'Senior Software Engineer', 'Team Lead',
#  'Project Lead', 'Project Manager']


from random import *

alphabets = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
cities = ['Hyderabad', 'Chennai', 'Bangalore', 'Kolkata', 'Pune', 'Delhi', 'Mumbai']
designations = ['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead', 'Project Manager']


def get_employee_name():
    my_name = choice(alphabets).upper()
    for i in range(randint(2, 9)):
        my_name += choice(alphabets)
    return my_name


def get_employee_number():
    emp_number = 'e-'
    for i in range(4):
        emp_number += choice(digits)
    return emp_number


def get_employee_salary():
    my_salary = uniform(10001, 500001)
    return my_salary


def get_employee_city():
    my_city = choice(cities)
    return my_city


def get_mobile_number():
    my_number = str(choice('6789'))
    for i in range(9):
        my_number += choice(digits)
    return my_number


def get_employee_designation():
    my_designation = choice(designations)
    return my_designation


def get_employee_all_details():
    print('Employee Name : ', get_employee_name())
    print('Employee Number : ', get_employee_number())
    # print('Employee Salary : ', get_employee_salary()) # example- 231689.1719360058
    print('Employee Salary : %.2f' % get_employee_salary()) # example- 231689.17
    # print('Employee Salary : {:.2f}'.format(get_employee_salary())) # example- 231689.17
    print('Employee City : ', get_employee_city())
    print('Employee Mobile Number : ', get_mobile_number())
    print('Employee Designation : ', get_employee_designation())


# get_employee_all_details()
for i in range(10):
    get_employee_all_details()
    print('---------------------------------------------------')