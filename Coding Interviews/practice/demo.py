arr1 = [25, 28, 23, 12, 15]
for i in range(len(arr1)):
    for j in range(i+1, len(arr1)):
        if arr1[i] > arr1[j]:
            arr1[i], arr1[j] = arr1[j], arr1[i]

print(arr1)