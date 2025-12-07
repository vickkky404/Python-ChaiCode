# OOPS - Encapsulation
# Demonstrates data hiding and encapsulation using private attributes

class BankAccount:
    """Class demonstrating encapsulation with private attributes"""
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance(self):
        """Public method to get balance"""
        return self.__balance

# Usage
account = BankAccount("Raj", 5000)
account.deposit(2000)
account.withdraw(1000)
print(f"Balance: {account.get_balance()}")
# account.__balance = -5000  # Cannot access private attribute directly
