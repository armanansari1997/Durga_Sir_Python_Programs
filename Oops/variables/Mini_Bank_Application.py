class Customer:
    """Customer class developed by Arman for bank Operations"""

    bank_name = 'DURGABANK'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print('Balance After Deposit :', self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Balance ... cannot perform this operation')
        else:
            self.balance -= amount
            print('Balance After Withdrawal :', self.balance)


print('Welcome to', Customer.bank_name)
name = input('Enter your name : ')
c = Customer(name)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option = input('Choose your option : ')
    if option.lower() == 'd':
        amount = float(input('Enter amount to deposit : '))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter amount to withdraw : '))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('Thanks for Banking...')
        break
    else:
        print('Invalid option, Please choose valid option')
