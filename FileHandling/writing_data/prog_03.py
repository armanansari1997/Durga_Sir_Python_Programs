f = open('def.txt', 'w')

# # d = {'Durga': 100, 'Ravi': 200}
d = {'Durga\n': 100, 'Ravi\n': 200}  # Keys should be string types only
f.writelines(d)
print('Data written to the file successfully')

f.close()

# d = {100: 'Arman\n', 200: 'Madhur\n'}
# # f.writelines(d)  # TypeError: write() argument must be str, not int
# f.writelines(d.values())  # NoError
# print('Data written to the file successfully')
# f.close()
