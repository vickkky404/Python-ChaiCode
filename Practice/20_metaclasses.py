# OOPS Program 20: Metaclasses
# Demonstrates metaclass creation and usage

class SingletonMeta(type):
    instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
    
    def connect(self):
        print(f'Connecting to {self.host} as {self.user}')
    
    def get_connection(self):
        return f'Connection: {self.host}'

class LoggingMeta(type):
    def __new__(mcs, name, bases, dct):
        print(f'Creating class {name}')
        return super().__new__(mcs, name, bases, dct)

class Logger(metaclass=LoggingMeta):
    def log(self, msg):
        print(f'LOG: {msg}')

if __name__ == '__main__':
    db1 = Database('localhost', 'admin', 'pass')
    db2 = Database('localhost', 'admin', 'pass')
    
    print('db1 is db2:', db1 is db2)
    db1.connect()
    print(db2.get_connection())
    
    logger = Logger()
    logger.log('Test message')
