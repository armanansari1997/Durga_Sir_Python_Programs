characters = ['Arman', 'Rusia', 'Shivam', 'Moin']

# enumerate() returns a sequence of (index, item) tuples
print(list(enumerate(characters)))  # [(0, 'Arman'), (1, 'Rusia'), (2, 'Shivam'), (3, 'Moin')]

# use enumerate() in a for loop to get an item and its index
for index, character in enumerate(characters):
    print(index, character)

# Output :
#0 Arman
# 1 Rusia
# 2 Shivam
# 3 Moin

