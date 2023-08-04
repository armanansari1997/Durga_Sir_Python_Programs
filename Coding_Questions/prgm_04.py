# maximum repeated character in a string
# Time complexity should be lesser than O(n2)

s = 'itininiytnnhhn'
ch = {}
for i in s:
    ch[i] = ch.get(i, 0) + 1   # recommended to use
    # if i not in ch:
    #     ch[i] = 1
    # else:
    #     ch[i] += 1

print(ch)  # {'i': 4, 't': 2, 'n': 5, 'y': 1, 'h': 2}
max_ch = max(ch, key=ch.get)
print(max_ch)  # n
