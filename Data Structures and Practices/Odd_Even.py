def check_odd_even(num):
    if num % 2 == 0:
        print(f"{num} is Even..")
    else:
        print(f"{num} is Odd")

n = int(input("Enter a number: "))
check_odd_even(n)