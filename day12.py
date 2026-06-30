class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

class CurrentAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

a1 = SavingsAccount("1234569", 1000)
a1.display()

c1 = CurrentAccount("987654321", 2000)
c1.withdraw(500)
c1.display()

