# OOPS Program 29: Container Magic Methods
# Demonstrates __len__, __getitem__, __setitem__, __contains__

class CustomList:
    def __init__(self, items=None):
        self.items = items or []
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __contains__(self, item):
        return item in self.items
    
    def __repr__(self):
        return f'CustomList({self.items})'

class SimpleDict:
    def __init__(self):
        self.data = {}
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value

if __name__ == '__main__':
    lst = CustomList([1, 2, 3, 4, 5])
    print('Length:', len(lst))
    print('Item at 0:', lst[0])
    print('2 in lst:', 2 in lst)
    lst[0] = 10
    print('After update:', lst)
    
    d = SimpleDict()
    d['name'] = 'Raj'
    d['age'] = 25
    print('Dict length:', len(d))
    print('Name:', d['name'])
