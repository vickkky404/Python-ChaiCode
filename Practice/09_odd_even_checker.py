# Odd or Even Number Checker
# Check if a number is odd or even

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Check if negative
if num < 0:
    print("(This is a negative number)")
elif num > 0:
    print("(This is a positive number)")
else:
    print("(This is zero)")
