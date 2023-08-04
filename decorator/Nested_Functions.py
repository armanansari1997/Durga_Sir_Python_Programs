# Nested Functions

# eg- 01
def outer():
    print('Outer Function execution started')

    def inner():
        print('inner function execution')

    print('Outer Function execution completed')


outer()

# Output:
# Outer Function execution started
# Outer Function execution completed


# eg-2
def outer():
    print('Outer Function execution started')

    def inner():
        print('inner function execution')
    inner()
    inner()
    inner()
    inner()

    print('Outer Function execution completed')


outer()

# Output:
# Outer Function execution started
# inner function execution
# inner function execution
# inner function execution
# inner function execution
# Outer Function execution completed
