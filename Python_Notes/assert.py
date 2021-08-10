#assert condition, 'String'
#If condition is true, ignore the string
#If condition is false, print the string
class Banks():
    title = 'Bank'
    def __init__(self, uname, money):
        self.name = uname;
        self.balance = money
    def save_money(self, money):
        assert money > 0, 'You need to have more than $0. '
        self.balance += money
        print('$', money, ' finished saving. ')
    def withdraw_money(self, money):
        assert money > 0, 'You need to have more than $0. '
        assert money <= self.balance, 'Saving not enough!'
        self.balance -= money
        print('$', money, ' withdrawn. ')
    def get_balance(self):
        print(self.name.title(), '$', self.balance, ' left in the account. ')

hungbank = Banks('hung', 100)
hungbank.get_balance()
hungbank.save_money(300)
hungbank.get_balance()
hungbank.save_money(-300)
hungbank.get_balance()
