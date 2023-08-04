# inp = ['hello', 'I', 'Am', 'TigerAnalytics', 'And', 'Amigoscode']

# user input
inp = eval(input('Enter the list of Strings'))
max_length = len(inp[0])
index = 0
for i, x in enumerate(inp):
    if len(x) > max_length:
        max_length = len(x)
        index = i

print('The maximum length of character is :', max_length)  # 14
print('The character is :', inp[index])  # TigerAnalytics

