# Find Duplictae Elements
mylist = [10, 20, 30, 40, 10, 30, 50, 60, 40, 10, 80, 50]

# Using List Comprehension
# newlist = list(set([num for num in mylist if mylist.count(num) > 1]))
# print(newlist)


# Using enumerate() function
# newlist = list(set([num for i, num in enumerate(mylist) if mylist.count(num) > 1]))
# print(newlist)


# Using a count() function
# newlist = []
# for num in mylist:
#     if mylist.count(num) > 1 and num not in newlist:
#         newlist.append(num)
# print('Duplicate elements are: ', newlist)

#  Using in, not in operators and count() method
# x = []
# y = []
# for num in mylist:
#     if num not in x:
#         x.append(num)
# for num in x:
#     if mylist.count(num) > 1:
#         y.append(num)
# print(y)


# Using Dictionary
mydict, newlist = {}, []
for num in mylist:
    mydict[num] = mydict.get(num, 0) + 1
print(mydict)
for k, v in mydict.items():
    if v > 1:
        newlist.append(k)
print(newlist)

