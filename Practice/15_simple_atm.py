# Simple ATM

balance = 1000
pin = 1234

attempts = 3
while attempts > 0:
    entered_pin = int(input("Enter PIN: "))
    if entered_pin == pin:
        print("PIN correct!")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN. Attempts left: {attempts}")
else:
    print("Account locked!")
    exit()

while True:
    print("\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print(f"Balance: Rs.{balance}")
    elif choice == 2:
        amount = int(input("Withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawn: Rs.{amount}")
        else:
            print("Insufficient balance")
    elif choice == 3:
        amount = int(input("Deposit amount: "))
        balance += amount
        print(f"Deposited: Rs.{amount}")
    elif choice == 4:
        print("Thank you!")
        break
