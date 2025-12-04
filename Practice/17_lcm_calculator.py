# LCM Calculator
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = lcm(a, b)
print(f"LCM of {a} and {b} is {result}")
