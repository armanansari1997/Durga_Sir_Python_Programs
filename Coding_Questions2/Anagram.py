# Check whether 2 given strings are Anagram or not

# User input
inp1 = input('Enter the input1')
inp2 = input('Enter the input2')
# inp1 = 'hello'
# inp2 = 'olhle'

res = 'Anagram' if sorted(inp1) == sorted(inp2) else 'Not an Anagram'
print(res)
