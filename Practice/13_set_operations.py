# Program 13: Set Operations
fruits = {"Apple", "Banana", "Cherry", "Apple"}
print(f"Set: {fruits}")
print(f"Length: {len(fruits)}")

fruits.add("Date")
print(f"After add: {fruits}")

fruits.remove("Banana")
print(f"After remove: {fruits}")

print(f"\nSet Operations:")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")
