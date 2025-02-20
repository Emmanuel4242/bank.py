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

# Library Management System
# Class: Book
# Attributes: title, author, ISBN, available
# Methods: borrowbook(), returnbook()

class Book:  
    def __init__(self, title, author, ISBN):  
        self.title = title  
        self.author = author  
        self.ISBN = ISBN  
        self.available = True  

    def borrowbook(self):  
        if self.available:  
            self.available = False  
            print(f"Book '{self.title}' borrowed successfully.")  
        else:  
            print("Book is already borrowed.")  

    def returnbook(self):  
        self.available = True  
        print(f"Book '{self.title}' returned.")  

# Create an object  
book1 = Book("A tale of two cities", "Charles Dickens", "0823107794")  
book1.borrowbook()   
book1.borrowbook()  
book1.returnbook()

# Online Shopping Cart
# Class: CartItem
# Attributes: item_name, price, quantity
# Methods: additem(), removeitem(), calculate_total()

class CartItem:  
    def __init__(self, item_name, price, quantity):  
        self.item_name = item_name  
        self.price = price  
        self.quantity = quantity  

    def additem(self):  
        self.quantity += 1  
        print(f"Added 1 {self.item_name}. Total quantity: {self.quantity}")  

    def removeitem(self):  
        if self.quantity > 0:  
            self.quantity -= 1  
            print(f"Removed 1 {self.item_name}. Remaining quantity: {self.quantity}")  
        else:  
            print("No items left to remove.")  

    def calculate_total(self):  
        return self.price * self.quantity  

# Create an object  
item1 = CartItem("New laptop", 200, 5)  
item1.additem()
item1.removeitem() 
print(f"Total cost: ${item1.calculate_total()}") 
