# bank_account_system.py
import csv

class Account:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid or insufficient funds.")

class Customer:
    def __init__(self, name, acc_no):
        self.name = name
        self.account = Account(acc_no)

    def save_transaction(self, action, amount):
        with open("transactions.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.name, self.account.acc_no, action, amount, self.account.balance])

# Example usage
customer1 = Customer("Alice", "ACC001")
customer1.account.deposit(500)
customer1.save_transaction("Deposit", 500)
customer1.account.withdraw(150)
customer1.save_transaction("Withdraw", 150)
