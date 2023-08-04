# Reverse a dictionary

dct = {
    "Animal": "Dog",
    "Fruit": "Pear",
    "Vegetable": "Cabbage",
    "Tree": "Maple",
    "Flower": "Daisey"
}

l = list(dct.items())
l = l[::-1]
d = dict(l)
print(d)  # {'Flower': 'Daisey', 'Tree': 'Maple', 'Vegetable': 'Cabbage', 'Fruit': 'Pear', 'Animal': 'Dog'}
