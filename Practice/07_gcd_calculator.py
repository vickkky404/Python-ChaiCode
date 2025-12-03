# GCD (Greatest Common Divisor) Calculator
# Find GCD of two numbers using Euclidean algorithm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {result}")
