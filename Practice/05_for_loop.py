# Program 5: For Loop
print("Printing numbers 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

print("\nPrinting even numbers:")
for i in range(2, 11, 2):
    print(i, end=" ")

print("\n\nIteration over list:")
colors = ["Red", "Green", "Blue"]
for color in colors:
    print(f"Color: {color}")

print("\nPrinting multiplication table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
