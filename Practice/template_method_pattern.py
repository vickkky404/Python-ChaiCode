"""Template Method Pattern - Define skeleton of algorithm, let subclasses override specific steps."""

from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Abstract template with algorithm skeleton."""
    
    def process(self, data):
        """Template method defining algorithm structure."""
        cleaned = self.validate_and_clean(data)
        processed = self.transform(cleaned)
        result = self.aggregate(processed)
        return self.format_output(result)
    
    @abstractmethod
    def validate_and_clean(self, data):
        pass
    
    @abstractmethod
    def transform(self, data):
        pass
    
    @abstractmethod
    def aggregate(self, data):
        pass
    
    @abstractmethod
    def format_output(self, data):
        pass


class CSVProcessor(DataProcessor):
    """Concrete implementation for CSV."""
    
    def validate_and_clean(self, data):
        return [d.strip() for d in data]
    
    def transform(self, data):
        return [d.upper() for d in data]
    
    def aggregate(self, data):
        return ', '.join(data)
    
    def format_output(self, data):
        return f'CSV Output: {data}'


class JSONProcessor(DataProcessor):
    """Concrete implementation for JSON."""
    
    def validate_and_clean(self, data):
        return [d.strip() for d in data]
    
    def transform(self, data):
        return [{'value': d} for d in data]
    
    def aggregate(self, data):
        return data
    
    def format_output(self, data):
        return f'JSON Output: {data}'


# Demonstration
if __name__ == "__main__":
    data = ['apple', ' banana ', 'cherry']
    
    csv_proc = CSVProcessor()
    print(csv_proc.process(data))
    
    json_proc = JSONProcessor()
    print(json_proc.process(data))
