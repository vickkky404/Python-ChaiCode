# OOPS Program 22: Weak References
# Demonstrates weak references and garbage collection

import weakref
import gc

class Resource:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print(f'Resource {self.name} deleted')
    
    def display(self):
        return f'Resource: {self.name}'

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = weakref.ref(parent) if parent else None
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def get_parent(self):
        if self.parent:
            return self.parent()
        return None

if __name__ == '__main__':
    res = Resource('Database')
    print(res.display())
    
    weak_res = weakref.ref(res)
    print('Weak ref:', weak_res())
    
    del res
    gc.collect()
    print('After deletion:', weak_res())
    
    root = Node('root')
    child1 = Node('child1', root)
    root.add_child(child1)
    print('Parent of child1:', child1.get_parent().value)
