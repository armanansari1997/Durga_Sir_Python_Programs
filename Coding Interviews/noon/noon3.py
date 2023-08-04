mylist = [9, 8, -1, 2, -3, -5, 7]
new_list = []
new_list2 = []
for ele in mylist:
    if ele > 0:
        new_list.append(ele)
    else:
        new_list2.append(ele)

result = new_list + new_list2
print(result)
# Output : [9, 8, 2, 7, -1, -3, -5]
