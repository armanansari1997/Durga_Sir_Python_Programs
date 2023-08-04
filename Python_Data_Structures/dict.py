# dictionary data type:

d = {'durga': 100, 'ravi': 200}
print(d)  # {'durga': 100, 'ravi': 200}
print(d.items())  # dict_items([('durga', 100), ('ravi', 200)])
print(d.keys())  # dict_keys(['durga', 'ravi'])
print(d.values())  # dict_values([100, 200])

d2 = dict([('ArMan', 'Kolkata'), ('Rusia', 'Odisa'), ('Madhur', 'Indore')])
print(d2)  # {'ArMan': 'Kolkata', 'Rusia': 'Odisa', 'Madhur': 'Indore'}
print(d2.items())  # dict_items([('ArMan', 'Kolkata'), ('Rusia', 'Odisa'), ('Madhur', 'Indore')])
print(d2.keys())  # dict_keys(['ArMan', 'Rusia', 'Madhur'])
print(d2.values())  # dict_values(['Kolkata', 'Odisa', 'Indore'])

print(d2.get('Arman'))  # None  (dictionary doesn't have key called 'Arman')
print(d2.get('Arman', -100))  # -100  (dictionary doesn't have key called 'Arman' hence default)
print(d2.get('ArMan'))  # Kolkata   (key found in dictionary)

# print(d2.pop('Arman'))  # KeyError: 'Arman'
print(d2.pop('Arman', 'Custom Value'))  # Custom Value (because key doesn't exist)
print(d2.pop('ArMan'))  # Kolkata
print(d2)  # {'Rusia': 'Odisa', 'Madhur': 'Indore'}

print(d.popitem())  # ('ravi', 200)  (It removes last item)
print('After popitem :', d)  # After popitem : {'durga': 100}

d2_copy = d2.copy()
d2.clear()
print(d2)  # {}
print(d2_copy)  # {'Rusia': 'Odisa', 'Madhur': 'Indore'}

print(d2_copy.setdefault('ArMan', 'Kolkata'))  # Kolkata (key doesn't exist hence returns new value of key)
print(d2_copy.setdefault('ArMan', 'Bengaluru'))  # Kolkata (if key exist then it returns value of exist key)
print(d2_copy)  # {'Rusia': 'Odisa', 'Madhur': 'Indore', 'ArMan': 'Kolkata'}

d2_copy.update([('Farhan', 'Mumbai'), ('Kartik', 'Pune')])
dummy_dict = {'Company': 'InfoBeans', 'Company2': 'Infosys', 'Company3': 'KPMG'}
print(d2_copy)  # {'Rusia': 'Odisa', 'Madhur': 'Indore', 'ArMan': 'Kolkata', 'Farhan': 'Mumbai', 'Kartik': 'Pune'}
d2_copy.update((dummy_dict))
print(d2_copy)  # {'Rusia': 'Odisa', 'Madhur': 'Indore', 'ArMan': 'Kolkata', 'Farhan': 'Mumbai', 'Kartik': 'Pune',
# 'Company': 'InfoBeans', 'Company2': 'Infosys', 'Company3': 'KPMG'}


# 1) get(key)
# 2) get(key, defaultValue)
# 3) d.setdefault(key,value)
# 4) pop(key)
# 5) pop(key, defaultValue)
# 6) popitem(key)
# 7) clear()
# 8) copy()
# 9) keys()
# 10) values()
# 11) items()

# Concatenate 2 dictionary :-

dict1 = {'Arman': 'Kolkata', 'Rusia': 'Odisa'}
dict2 = {'Madhur': 'Indore', 'Londhe': 'Pune', 'Moin': 'Indore'}
# here
dict3 = {**dict1, **dict2}
print(id(dict1))  # 2573885295104
print(id(dict2))  # 2573885244608
print(id(dict3))  # 2573885300672
print(dict3)  # {'Arman': 'Kolkata', 'Rusia': 'Odisa', 'Madhur': 'Indore', 'Londhe': 'Pune', 'Moin': 'Indore'}
# here
dict1 = {**dict1, **dict2}
print(dict1)  # {'Arman': 'Kolkata', 'Rusia': 'Odisa', 'Madhur': 'Indore', 'Londhe': 'Pune', 'Moin': 'Indore'}
print(id(dict1))  # 2573885518912
