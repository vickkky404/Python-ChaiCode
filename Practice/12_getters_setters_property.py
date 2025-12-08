# OOPS Program 12: Getters, Setters and Property Decorator
# Demonstrates property decorator and encapsulation

class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder
        self._balance = balance
    
    @property
    def balance(self):
        """Getter for balance"""
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        """Setter for balance with validation"""
        if amount < 0:
            print("Error: Balance cannot be negative")
        else:
            self._balance = amount
    
    @property
    def account_holder(self):
        return self._account_holder
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Deposited: {amount}. New balance: {self._balance}')
        else:
            print('Deposit amount must be positive')
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f'Withdrawn: {amount}. Remaining balance: {self._balance}')
        else:
            print('Invalid withdrawal amount')

if __name__ == '__main__':
    acc = BankAccount('Raj Kumar', 5000)
    print(f'Account Holder: {acc.account_holder}')
    print(f'Balance: {acc.balance}')
    acc.deposit(2000)
    acc.withdraw(1500)
    acc.balance = 8000
    print(f'Updated Balance: {acc.balance}')
    acc.balance = -500
