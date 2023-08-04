# input : {'orange':'fruit', 'potato': 'vegetable', 'banana': 'fruit'}
# output : {'fruit': ['orange', 'banana'], 'vegetable': ['potato']}

inp = {'orange': 'fruit', 'potato': 'vegetable', 'banana': 'fruit'}
mydict = {}

# for ele in inp:
#     if inp[ele] not in mydict:
#         mydict[inp[ele]] = [ele]
#     else:
#         mydict[inp[ele]].append(ele)
#
# print(mydict)



for k, v in inp.items():
    if v not in mydict:
        mydict[v] = inp[k]
print(mydict)

