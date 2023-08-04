def count_substring(string, sub_string):
    myindex = string.find(sub_string)
    count = 0
    if myindex != -1:
        for i in range(myindex, len(string)):
            count += 1
        return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)