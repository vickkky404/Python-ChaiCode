# Singleton Pattern

class Singleton:
    _instance = None
    _counter = 0
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._counter += 1
        return cls._instance
    
    def __init__(self):
        self.value = None
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    @classmethod
    def get_instance_count(cls):
        return cls._counter

class Database(Singleton):
    def __init__(self):
        super().__init__()
        self.connection = "Connected to DB"
    
    def query(self, sql):
        return f"Executing: {sql}"

# Testing
db1 = Database()
db2 = Database()
db3 = Database()

print(f"db1 is db2: {db1 is db2}")
print(f"db2 is db3: {db2 is db3}")
print(f"Instance count: {Database.get_instance_count()}")
print(f"db1.connection: {db1.connection}")
print(f"Query result: {db2.query('SELECT * FROM users')}")
