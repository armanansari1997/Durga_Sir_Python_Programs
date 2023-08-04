if __name__ == '__main__':
    word = input("Enter")
    d = {"DIGITS": 0, "LETTERS": 0}
    for c in word:
        if c.isdigit():
            d["DIGITS"] += 1
        elif c.isalpha():
            d["LETTERS"] += 1
        else:
            pass
    print("DIGITS", d["DIGITS"])
    print("LETTERS", d["LETTERS"])

