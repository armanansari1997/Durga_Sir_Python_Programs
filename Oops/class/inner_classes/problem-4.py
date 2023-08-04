# important
class Person:
    def __init__(self, name, dd, mm, yyyy):
        print('Person Object Creation')
        self.name = name
        self.dob = self.DOB(dd, mm, yyyy)

    def info(self):
        print('Name :', self.name)
        self.dob.display()

    class DOB:
        def __init__(self, dd, mm, yyyy):
            print('DOB Object Creation')
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

        def display(self):
            print(f'DOB={self.dd}/{self.mm}/{self.yyyy}')


p = Person('Arman', '01', '05', '1997')
p.info()
