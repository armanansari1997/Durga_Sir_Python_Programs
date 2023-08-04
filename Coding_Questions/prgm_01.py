# Find the min and max value without using any predefined functions
l = [10, 50, 30, 20, 60, 80, 40]
max_val = l[0]
min_val = l[0]
for i in l:
    if i > max_val:
        max_val = i
    elif i < min_val:
        min_val = i

print("Maximum value :", max_val)
print("Minimum Value :", min_val)
