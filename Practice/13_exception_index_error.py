# Exception Handling - Index Error
# Demonstrates how to handle IndexError when accessing list elements

def access_list_element():
    """Function to access list elements with exception handling"""
    try:
        numbers = [10, 20, 30, 40, 50]
        index = int(input("Enter the index to access: "))
        print(f"Element at index {index}: {numbers[index]}")
    except IndexError:
        print("Error: Index out of range!")
    except ValueError:
        print("Error: Please enter a valid integer!")
    finally:
        print("List access operation completed.")

if __name__ == "__main__":
    access_list_element()
