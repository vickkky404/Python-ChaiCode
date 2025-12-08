# OOPS Program 17: Context Managers
# Demonstrates __enter__ and __exit__ for context management

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f'File {self.filename} opened')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f'File {self.filename} closed')
        return False

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        self.connection = f'Connected to {self.db_name}'
        print(self.connection)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Disconnected from {self.db_name}')
        return False

if __name__ == '__main__':
    with FileManager('test.txt', 'w') as f:
        print('Writing to file')
    
    with DatabaseConnection('MySQL') as conn:
        print(f'Using connection: {conn}')
