# Factorial Calculator - Iterative Method
# Calculate factorial of a number using loops

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial not defined for negative numbers")
elif num == 0:
    print(f"Factorial of {num} is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
