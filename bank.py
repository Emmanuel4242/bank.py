# Bank account system
# class: BankAccount
# Attributes: owner_name,balance,account_number
# Methods: deposit(),withdraw,check_balance()

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
      self.balance += amount
      print(f"{self.owner} deposited ${amount}.New balance :${self.balance}")
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdraw ${amount}.New balance:${self.balance}")
        else:
            print("insufficient!")

# creating an account
account1 = BankAccount("Johnson ", 4000)
account1.deposit(1500)
account1.withdraw(800)

