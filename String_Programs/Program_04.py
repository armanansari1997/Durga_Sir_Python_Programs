# to print characters present at even index and odd index separately for the given string
if __name__ == '__main__':
    # s = 'durgasoft'
    # i = 0
    # print("Characters present at even index")
    # while i < len(s):
    #     print(s[i])
    #     i += 2
    # print("Characters present at odd index")
    # i = 1
    # while i < len(s):
    #     print(s[i])
    #     i += 2

    s = 'durgasoft'
    res = s[::2]
    print("Characters present at even index is : ",res)

    res2 = s[1::2]
    print("Characters present at odd index is : ", res2)
