# For this challenge, create a bank account class that has two attributes:
# owner
# balance

# and two methods:
# deposit
# withdraw

class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        print(f"Added {deposit_amount} to the balance")

    def withdraw(self,withdraw_amount):
        if withdraw_amount >= self.balance:
            print("Sorry not enough!")
        else:
            self.balance -= withdraw_amount
            print("Withdrawal Accepted")

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"

account = Account('Sam',500)
print(account)
print(account.owner)
print(account.balance)
account.deposit(75)
account.withdraw(500)
print(account)