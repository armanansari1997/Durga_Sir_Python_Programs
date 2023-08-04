if __name__ == '__main__':
    # Keys must be a single element
    # Value can be any type such as list, tuple, integer, etc.
    # d = {}
    # d['Arman'] = 20
    # # Key must be a single element
    # # d[{'a',10,20}] = 40 # Error
    # d['A'] = {'arman',20,30}
    # print(d)

    # Dict = {"Name":'Arman', 'Age':24}

    employee = {'Name': 'Arman', 'Age': 24, 'Salary': 30000, 'Company': 'GOOGLE'}
    print(type(employee))
    print('Printing Employee data')
    print(employee)

    # Accessing Values
    print('Name: %s' % employee['Name'])
    print('Age: %d' % employee['Age'])
    print('Salary: %d' % employee['Salary'])
    print('Company: %s' % employee['Company'])

    # Python provides the built-in function dict() method which is also used to create dictionary.
    # The empty curly braces {} is used to create empty dictionary.

    # Creating an empty Dictionary
    Dict = {}
    print("Empty Dictionary: ")
    print(Dict)

    # Creating a Dictionary
    # with dict() method
    d = dict({1: 'JAVA', 2: 'T', 3: 'POINT'})
    print("\nCreate Dictionary by using  dict(): ")
    print(d)

    # Creating a Dictionary
    # with each item as a Pair
    d = dict([(1, 'Arman'), (2, 'Ansari')])
    print('\nDictionary with each item as a pair: ')
    print(d)

    # Adding dictionary values
    # Creating an empty Dictionary
    Dict = {}
    print("Empty Dictionary: ")
    print(Dict)


    Dict[0] = 'Peter'
    Dict[2] = 'Joseph'
    Dict[3] = 'Rocky'
    print('\nDictionary after adding 3 elements:')
    print(Dict)

    # Adding set of values
    # with a single Key
    # The Emp_ages doesn't exist to dictionary
    Dict['Emp_ages'] = 20, 33, 24
    print('\nDictionary adding after 3 elements: ')
    print(Dict)

    # Updating existing Key's Value
    Dict[3] = 'JavaTpoint'
    print("\nUpdated key value: ")
    print(Dict)

    # Example - 2:
    # Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
    # print(type(Employee))
    # print("printing Employee data .... ")
    # print(Employee)
    # Employee['Name'] = input('Name: ')
    # Employee['Age'] = int(input('Age: '))
    # Employee['salary'] = int(input('salary: '))
    # Employee['Company'] = input('Company: ')
    # print('\nPrinting the new Data:')
    # print(Employee)

    # Deleting elements using del keyword
    Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
    print("Deleting some of the employee data")
    del Employee["Name"]
    del Employee['Company']
    print("printing the modified information ")
    print(Employee)
    print("Deleting the dictionary: Employee");
    del Employee
    # print("Let's try to print it again")
    # print(Employee) # NameError: name 'Employee' is not defined

    # Using pop() method (pop w.r.t keys)
    # Creating a Dictionary
    Dict = {1: 'JavaTpoint', 2: 'Peter', 3: 'Thomas'}
    # Deleting a key
    # using pop() method
    pop_ele = Dict.pop(3)
    print(pop_ele)  # Thomas

    # A dictionary can be iterated using for loop as given below.
    Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
    for x in Employee:
        print(x)

    # Output: Thomas
    #         Name
    #         Age
    #         salary
    #         Company

    # for loop to print all the values of the dictionary
    for x in Employee:
        print(Employee[x])

    # Output:
    # ohn
    # 29
    # 25000
    # GOOGLE

    # for loop to print the values of the dictionary by using values() method.
    for v in Employee.values():
        print(v)

    # Output:
    # ohn
    # 29
    # 25000
    # GOOGLE

    # for loop to print the items of the dictionary by using items() method.
    for x in Employee.items():
        print(x)

    # Output:
    # ('Name', 'John')
    # ('Age', 29)
    # ('salary', 25000)
    # ('Company', 'GOOGLE')

    #     Properties of Dictionary keys
    for k, v in Employee.items():
        print(k, v)

    # Output:
    # Name John
    # Age 29
    # salary 25000
    # Company GOOGLE

    # In python, the key cannot be any mutable object. We can use numbers, strings, or tuples as the key,
    # but we cannot use any mutable object like the list as the key in the dictionary.
    # Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE",
    # [100, 201, 301]: "Department ID"}
    # for x,y in Employee.items():
    #     print(x,y)
    # TypeError: unhashable type: 'list'

    print(len(d))
