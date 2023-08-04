def decor(func):
    def inner():
        print('Send the person to Beauty parlour')
        print('Showing a person with full of decoration')

    return inner


@decor
def display():
    print('Showing a person as it is')


display()
# Output:
# Send the person to Beauty parlour
# Showing a person with full of decoration

