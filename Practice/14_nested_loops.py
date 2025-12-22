# Program 14: Nested Loops
print("Multiplication Table (1 to 3 by 1 to 3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

print("\nPyramid Pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nMatrix:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()
