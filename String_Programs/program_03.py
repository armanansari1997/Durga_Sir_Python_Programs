# Merge Character of 2 string into a single string by taking characters alternatively
if __name__ == '__main__':
    s1 = "abcd"
    s2 = "efghijk"
    s3 = ''
    i,j = 0,0
    while i < len(s1) or j < len(s2):
        if i < len(s1):
            s3 += s1[i]
            i += 1
        if j < len(s2):
            s3 += s2[j]
            j += 1
    print(s3)
