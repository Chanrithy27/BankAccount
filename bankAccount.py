class BankAccount:

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited {amount}!")
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print(
                f"Insufficient funds. You can't withdraw more than {self.balance}")
            return self
        else:
            self.balance -= amount
        print(f"You withdrew {amount}")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self


user1 = BankAccount(.05, 0)
user1.deposit(100).deposit(100).deposit(25).withdraw(
    100).yield_interest().display_account_info()
user2 = BankAccount(.02, 40)
user2.deposit(100).deposit(52).withdraw(100).withdraw(10).withdraw(
    5).withdraw(200).yield_interest().display_account_info()
