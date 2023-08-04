# input  : [1,2,-4,-1,40,-30]
# output : [1,2,40,-4,-1,-30]

num_list = [1, 2, -4, -1, 40, -30]
pos_list = []
neg_list = []
for num in num_list:
    if num >= 0:
        pos_list.append(num)
    else:
        neg_list.append(num)
print(pos_list)
print(neg_list)
# res = [pos_list, neg_list]
# print(res)  # [[1, 2, 40], [-4, -1, -30]]

# pos_list.append(neg_list)
# print(pos_list)  # [1, 2, 40, [-4, -1, -30]]

pos_list.extend(neg_list)
res = pos_list
print(res)  # [1, 2, 40, -4, -1, -30]
