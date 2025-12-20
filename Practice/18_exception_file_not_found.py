# Exception Handling - File Not Found Error
# Demonstrates FileNotFoundError when file doesn't exist

def read_file():
    """Function to read file with exception handling"""
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print("Error: The specified file does not exist!")
    except IOError:
        print("Error: Unable to read the file!")
    finally:
        print("File operation completed.")

if __name__ == "__main__":
    read_file()
