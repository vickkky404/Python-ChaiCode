# Custom exception class definition

class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive!")
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount}, only {balance} available!")
    return balance - amount

try:
    balance = 5000
    withdraw(balance, -100)
except InvalidAmountError as e:
    print(f"Error: {e}")
except InsufficientFundsError as e:
    print(f"Error: {e}")
