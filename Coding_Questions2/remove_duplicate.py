# Remove duplicate elements from the given list


num_list = [8, 4, 1, 3, 1, 7, 6, 9, 5, 2, 7]

# way -01
# new_list = list(set(num_list))
# print(new_list)

# way -02
new_list = []
for ele in num_list:
    if ele not in new_list:
        new_list.append(ele)
print(new_list)

# way -03  Wrong output
# new_list = []
# result = [new_list.append(ele) for ele in num_list if ele not in new_list]
# print(result)

# way -04
# new_list = []
# for idx, ele in enumerate(num_list):
#     if ele not in num_list[0:idx]:
#         new_list.append(ele)
# print(new_list)

# way -05
# result = [ele for idx, ele in enumerate(num_list) if ele not in num_list[0:idx]]
# print(result)

# way -06
# new_dict = dict.fromkeys(num_list)
# new_list = list(new_dict.keys())
# print(new_list)

