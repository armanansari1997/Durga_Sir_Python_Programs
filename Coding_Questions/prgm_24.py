inp1 = "KXIP"
inp2 = "SDF"
inp3 = "WRG"
i, j, k = 0, 0, 0
while i < len(inp1) or j < len(inp2) or k < len(inp3):
    output = ''
    if i < len(inp1):
        output += inp1[i]
        i += 1
    if j < len(inp2):
        output += inp2[j]
        j += 1
    if k < len(inp3):
        output += inp3[k]
        k += 1
    print(output)
