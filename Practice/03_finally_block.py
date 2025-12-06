# Finally block demonstration
# Finally block always executes

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Division result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid integers!")
finally:
    print("Thank you for using the calculator!")
