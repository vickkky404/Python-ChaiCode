#Else clause with try-except
try:
    x = 5
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Cannot divide!")
else:
    print(f"Result: {result}")
