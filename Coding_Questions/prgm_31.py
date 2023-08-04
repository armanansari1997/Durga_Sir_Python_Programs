# Given a string as your input, delete any reoccurring character, and return the new string

def delete_reoccurring_characters(inp_str):
    res = ""
    for ch in s:
        if ch not in res:
            res += ch
    return res


s = 'mississippi'
print(delete_reoccurring_characters(s))
