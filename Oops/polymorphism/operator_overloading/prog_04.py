# overloading of > and <= Operators for Student class object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __le__(self, other):
        return self.marks <= other.marks


s1 = Student('Durga', 100)
s2 = Student('Ravi', 200)
s3 = Student('Shiva', 300)


res1 = s1 > s2
res2 = s1 <= s2
res3 = s2 < s3
print(res1)  # False
print(res2)  # True
print(res3)  # True


# Note:
# If we overload the '__lt__()' then it will overload the '__gt__()' too
