# Remove Duplicates from the given list
# print duplicates present in the list

mylist = ["hello", 10, 20, 40, 20, 20, 60, 10, 40, 30, 10]

# way -01

uniq_ele_list = []
dupl_ele_lst = []
for ele in mylist:
    if ele not in uniq_ele_list:
        uniq_ele_list.append(ele)
    elif ele not in dupl_ele_lst:
        dupl_ele_lst.append(ele)
print("Unique Elements List :", uniq_ele_list)
print("Duplicate Elements List :", dupl_ele_lst)

# way -02

# dupl_ele_lst = []
# for ele in mylist:
#     if mylist.count(ele) > 1 and ele not in dupl_ele_lst:
#         dupl_ele_lst.append(ele)
# print("Duplicate Elements List :", dupl_ele_lst)

# way -03

dupl_ele_lst = []
for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
        if mylist[i] == mylist[j] and mylist[i] not in dupl_ele_lst:
            dupl_ele_lst.append(mylist[i])
print("Duplicate Elements List :", dupl_ele_lst)
