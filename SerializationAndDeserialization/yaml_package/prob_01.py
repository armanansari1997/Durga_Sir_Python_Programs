from pyaml import yaml

emp_dict = {'name': 'Durga', 'age': 35, 'Salary': 2000.0, 'isMarried': True}

# Serializing to yaml string
yaml_string = yaml.dump(emp_dict)
print(yaml_string)

# Serializing to yaml file
with open('emp.yaml', 'w') as f:
    yaml.dump(emp_dict, f)

# Deserializing from yaml string
new_dict = yaml.safe_load(yaml_string)
print(type(new_dict))
for k, v in new_dict.items():
    print(k, ':', v)

# Deserializing from yaml file
with open('emp.yaml', 'r') as f:
    new_dict2 = yaml.safe_load(f)
print(new_dict2)
