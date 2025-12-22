# Program 6: While Loop
print("Counting from 1 to 5:")
i = 1
while i <= 5:
    print(i)
    i += 1

print("\nSum of numbers 1 to 10:")
sum_val = 0
num = 1
while num <= 10:
    sum_val += num
    num += 1
print(f"Sum: {sum_val}")

print("\nTable of 3:")
mult = 1
while mult <= 10:
    print(f"3 x {mult} = {3*mult}")
    mult += 1
