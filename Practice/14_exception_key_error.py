# Exception Handling - Key Error
# Demonstrates how to handle KeyError when accessing dictionary keys

def access_dict_key():
    """Function to access dictionary keys with exception handling"""
    try:
        person = {'name': 'John', 'age': 25, 'email': 'john@example.com'}
        key = input("Enter the key to access: ")
        print(f"{key}: {person[key]}")
    except KeyError:
        print(f"Error: Key not found in dictionary!")
    except Exception as e:
        print(f"Error: {type(e).__name__} - {str(e)}")
    finally:
        print("Dictionary access operation completed.")

if __name__ == "__main__":
    access_dict_key()
