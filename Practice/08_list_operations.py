# Program 8: List Operations
fruits = ["Apple", "Banana", "Cherry"]
print(f"List: {fruits}")
print(f"Length: {len(fruits)}")

fruits.append("Date")
print(f"After append: {fruits}")

fruits.remove("Banana")
print(f"After remove: {fruits}")

fruits.insert(1, "Blueberry")
print(f"After insert: {fruits}")

print(f"\nIteration:")
for fruit in fruits:
    print(f"  - {fruit}")

print(f"\nReverse: {fruits[::-1]}")
