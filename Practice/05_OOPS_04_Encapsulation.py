# OOPS Program 4: Encapsulation
# Demonstrate data hiding and encapsulation using private attributes

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid amount or insufficient balance")
    
    def get_balance(self):
        return self.__balance

# Create account and perform operations
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current Balance: {account.get_balance()}")
