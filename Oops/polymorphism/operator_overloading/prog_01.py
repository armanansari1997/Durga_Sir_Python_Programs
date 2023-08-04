class Book:
    def __init__(self, pages):
        self.pages = pages


b1 = Book(100)
b2 = Book(100)
print(b1 + b2)  # TypeError: unsupported operand type(s) for +: 'Book' and 'Book'


# Solution:
# prog_02
