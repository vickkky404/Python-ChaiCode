# Exception with list operations
try:
    lst = [1, 2, 3]
    lst.remove(10)
except ValueError:
    print("Item not in list")
