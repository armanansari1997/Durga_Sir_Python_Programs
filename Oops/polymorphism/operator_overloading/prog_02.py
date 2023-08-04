class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        total_pages = self.pages + other.pages
        return total_pages


b1 = Book(100)
b2 = Book(200)
print(b1 + b2)  # 300


