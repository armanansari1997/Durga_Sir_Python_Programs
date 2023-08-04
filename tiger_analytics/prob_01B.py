# user input
# inp = eval(input('Enter the list of Strings'))

inp = "Hello I am TigerAnalytics And AmigosCode"
char_list = [x for x in inp.split()]  # ['hello', 'I', 'Am', 'TigerAnalytics', 'And', 'Amigoscode']
max_length = len(char_list[0])
index = 0
for i, x in enumerate(char_list):
    if len(x) > max_length:
        max_length = len(x)
        index = i

print('The maximum length of character is :', max_length)  # 14
print('The character is :', char_list[index])  # TigerAnalytics
