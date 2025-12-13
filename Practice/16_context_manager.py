# Context Manager Protocol

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        if exc_type:
            print(f"Exception occurred: {exc_type}")
        return False

class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        print("Timer started")
        return self
    
    def __exit__(self, *args):
        import time
        end = time.time()
        print(f"Elapsed time: {end - self.start:.4f} seconds")

# Testing
print("Using Context Manager:")
with Timer():
    total = sum(range(1000000))
    print(f"Sum calculated: {total}")
