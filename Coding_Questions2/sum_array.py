mylist = [4, 5, 6, 7, 2, 8, 3, 1, 9]
num = 10
for i in range(len(mylist)-1):
    for j in range(i+1, len(mylist)):
        if mylist[i] + mylist[j] == num:
            print(mylist[i], mylist[j])
