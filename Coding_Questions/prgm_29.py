# WAP to extract digits from the given string
test_string = '1w3e4r5t6y7u7i8i'
res = ''
for x in test_string:
    if x.isdigit():
        res += x
print(res)

# using lambda function and filter function
res = ''.join(filter(lambda x: x.isdigit(), test_string))
print(res)
