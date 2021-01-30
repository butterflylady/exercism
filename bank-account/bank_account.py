"""
Exercism solution for "bank-account"
"""


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.state = "unopened"

    def error_if_not_opened(self):
        if self.state == "unopened":
            raise ValueError("Account is not opened!")
        elif self.state == "closed":
            raise ValueError("Account is closed!")

    def get_balance(self):
        self.error_if_not_opened()
        return self.balance

    def open(self):
        if self.state == "opened":
            raise ValueError("Account is already opened!")
        self.state = "opened"
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount!")
        self.error_if_not_opened()
        self.balance += amount

    def withdraw(self, amount):
        self.error_if_not_opened()
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount!")
        self.balance -= amount
        if self.balance < 0:
            raise ValueError("Insufficient balance")

    def close(self):
        self.error_if_not_opened()
        self.state = "closed"
