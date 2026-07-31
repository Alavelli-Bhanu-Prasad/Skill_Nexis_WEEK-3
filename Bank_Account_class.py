class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt

    def withdraw(self, amt):
        if 0 < amt <= self.balance:
            self.balance -= amt

    def display_balance(self):
        return self.balance


# Example usage
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.display_balance())