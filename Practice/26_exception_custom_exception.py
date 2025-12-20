# Exception Handling - Custom Exception Class
# Demonstrates creating and using custom exception classes

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance={balance}, requested={amount}")

class BankAccount:
    """Bank account class with exception handling"""
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        """Withdraw money with exception handling"""
        try:
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        except InsufficientFundsError as e:
            print(f"Error: {str(e)}")
        finally:
            print("Transaction completed.")

if __name__ == "__main__":
    account = BankAccount(1000)
    account.withdraw(500)
    account.withdraw(600)
