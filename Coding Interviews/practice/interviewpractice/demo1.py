# oldlist = [10, [20, 30], 'Arman']
# print(id(oldlist))
# print(id(oldlist[0]))
# print(id(oldlist[1][0]))
# print(id(oldlist[1][1]))
# print(id(oldlist[2]))
# newlist = oldlist
# print("-------Newlist------")
# print(id(newlist))
# print(id(newlist[0]))
# print(id(newlist[1][0]))
# print(id(newlist[1][1]))
# print(id(newlist[2]))
# print('----changes-----')
# newlist[1][0] = 999
# newlist[2] = 'changed'
# print(oldlist)
# print(newlist)

# ----changes-----
# [10, [999, 30], 'changed']
# [10, [999, 30], 'changed']

# import copy
# oldlist = [10, [20, 30], 'Arman']
# print(id(oldlist))
# print(id(oldlist[0]))
# print(id(oldlist[1]))
# print(id(oldlist[1][0]))
# print(id(oldlist[1][1]))
# print(id(oldlist[2]))
# newlist = copy.copy(oldlist)
# print("-------Newlist------")
# print(id(newlist))
# print(id(newlist[0]))
# print(id(oldlist[1]))
# print(id(newlist[1][0]))
# print(id(newlist[1][1]))
# print(id(newlist[2]))
# print('----changes-----')
# newlist[1][0] = 999
# newlist[2] = 'changed'
# print(oldlist)
# print(newlist)

# ----changes-----
# [10, [999, 30], 'Arman']
# [10, [999, 30], 'changed']

import copy
oldlist = [10, [20, 30], 'Arman']
print(id(oldlist))
print(id(oldlist[0]))
print(id(oldlist[1]))
print(id(oldlist[1][0]))
print(id(oldlist[1][1]))
print(id(oldlist[2]))
newlist = copy.deepcopy(oldlist)
print("-------Newlist------")
print(id(newlist))
print(id(newlist[0]))
print(id(newlist[1]))
print(id(newlist[1][0]))
print(id(newlist[1][1]))
print(id(newlist[2]))
print('----changes-----')
newlist[1][0] = 999
newlist[2] = 'changed'
print(newlist)
print(oldlist)

# ----changes-----
# [10, [20, 30], 'Arman']
# [10, [999, 30], 'changed']
