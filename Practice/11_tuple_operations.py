# Program 11: Tuple Operations
colors = ("Red", "Green", "Blue")
print(f"Tuple: {colors}")
print(f"Length: {len(colors)}")
print(f"First element: {colors[0]}")
print(f"Last element: {colors[-1]}")

print(f"\nSlicing:")
print(f"First 2: {colors[:2]}")
print(f"Reversed: {colors[::-1]}")

point = (10, 20)
x, y = point
print(f"\nUnpacking - x: {x}, y: {y}")

numbers = (1, 2, 3, 2, 4, 2)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

print(f"\nTuple is immutable (cannot be changed)")
