import json

employee = {
    'name': 'Durga',
    'age': '35',
    'salary': 30000,
    'isMarried': True,
    'isHavingGF': None
}

# serialize from python dict object to a "json string"

# json_string = json.dumps(employee)  #  without any indentation
# json_string = json.dumps(employee, indent=4)  # maintain indentation
json_string = json.dumps(employee, indent=4, sort_keys=True)  # with indentation and sorting using keys
print('Sorting using keys')
print(json_string)

# serialize from python dict object to "json file"
with open('emp.json', 'w') as f:
    # json.dump(employee, f)
    json.dump(employee, f, indent=4)


