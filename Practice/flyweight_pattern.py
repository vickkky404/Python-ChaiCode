"""Flyweight Pattern - Use sharing to support large numbers of similar objects."""

class TreeFlyweight:
    def __init__(self, tree_type):
        self.tree_type = tree_type
    
    def display(self, x, y):
        print(f'{self.tree_type} at ({x}, {y})')

class TreeFactory:
    _trees = {}
    
    @classmethod
    def get_tree(cls, tree_type):
        if tree_type not in cls._trees:
            cls._trees[tree_type] = TreeFlyweight(tree_type)
        return cls._trees[tree_type]
    
    @classmethod
    def get_total(cls):
        return len(cls._trees)

if __name__ == '__main__':
    factory = TreeFactory()
    for _ in range(5):
        factory.get_tree('Oak')
    for _ in range(3):
        factory.get_tree('Pine')
    
    print(f'Total unique tree types: {factory.get_total()}')
    factory.get_tree('Oak').display(10, 20)
    factory.get_tree('Pine').display(30, 40)
