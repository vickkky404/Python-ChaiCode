"""Strategy Pattern - Define a family of algorithms, encapsulate each one, and make them interchangeable."""

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """Abstract strategy for payment methods."""
    
    @abstractmethod
    def pay(self, amount: float) -> str:
        """Process payment with specific strategy."""
        pass


class CreditCardPayment(PaymentStrategy):
    """Concrete strategy for credit card payment."""
    
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using Credit Card {self.card_number[-4:]}"


class PayPalPayment(PaymentStrategy):
    """Concrete strategy for PayPal payment."""
    
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using PayPal account {self.email}"


class CryptoCurrencyPayment(PaymentStrategy):
    """Concrete strategy for cryptocurrency payment."""
    
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using Crypto Wallet {self.wallet_address[:8]}..."


class ShoppingCart:
    """Context class that uses a payment strategy."""
    
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item: str, price: float):
        """Add item to cart."""
        self.items.append((item, price))
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        """Set the payment strategy."""
        self.payment_strategy = strategy
    
    def checkout(self) -> str:
        """Process checkout with the selected strategy."""
        if not self.payment_strategy:
            return "No payment strategy selected!"
        
        total = sum(price for _, price in self.items)
        return self.payment_strategy.pay(total)


# Demonstration
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 1200)
    cart.add_item("Mouse", 50)
    cart.add_item("Keyboard", 100)
    
    # Using Credit Card
    cart.set_payment_strategy(CreditCardPayment("4532-1234-5678-9010", "123"))
    print(cart.checkout())
    
    # Switch to PayPal
    cart.set_payment_strategy(PayPalPayment("user@example.com"))
    print(cart.checkout())
    
    # Switch to Cryptocurrency
    cart.set_payment_strategy(CryptoCurrencyPayment("1A2B3C4D5E6F7G8H"))
    print(cart.checkout())
