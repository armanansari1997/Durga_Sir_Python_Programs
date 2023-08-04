class Student:
    school_name = 'DURGASOFT'

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # instance method
    def get_student_info(self):
        print(self.name)
        print(self.roll_no)

    @classmethod
    def get_school_info(cls):
        print(Student.school_name)
        print(cls.school_name)

    @staticmethod
    def get_sum(a, b):
        sum = a+b
        return sum


