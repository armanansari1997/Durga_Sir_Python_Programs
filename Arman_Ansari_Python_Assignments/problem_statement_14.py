from random import Random


class GuessANumber:
    def __init__(self):
        pass

    def mul(self, num):
        return num * 2


if __name__ == '__main__':
    obj1 = GuessANumber()
    num1 = eval(input("Enter a num : "))
    mulVal = obj1.mul(num1)
    ran = Random()
    ranValue = ran.randint(5, 50)
    if mulVal == ranValue:
        print("Congrats number matches!!!!!")
    else:
        print("Better Luck Next Time")
        print("Number was : ", ranValue)

