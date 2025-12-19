class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Amount")
            return None
account1 = BankAccount("123", "Ayon")
print(account1.balance)
account1.deposit(250)
print(account1.balance)
account1.withdraw(251)
print(account1.balance)
