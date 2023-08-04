# Input   : the sky is blue
# Output  : blue is sky the


inp = "the sky is blue"
inp = inp.split()
# print(type(inp))  # <class 'list'>
# l1 = inp[::-1]
# res = ' '.join(l1)
res = ' '.join(inp[::-1])
print(res)