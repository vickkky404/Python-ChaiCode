# Armstrong Number Checker
# A number is armstrong if sum of cubes of digits equals the number

num = int(input("Enter a number: "))
temp = num
sum_cubes = 0

while temp > 0:
    digit = temp % 10
    sum_cubes += digit ** 3
    temp //= 10

if sum_cubes == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
