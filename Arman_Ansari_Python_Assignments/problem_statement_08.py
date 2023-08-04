if __name__ == '__main__':
    sentence = "cisco infosys oracle cts cisco"
    for word in sentence.split(' '):
        if word.startswith('c'):
            print(word)

    # Recommended Way
    items = [word for word in sentence.split(' ') if word[0] == 'c']
    print(items)
