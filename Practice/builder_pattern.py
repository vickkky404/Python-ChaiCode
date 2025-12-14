"""Builder Pattern - Separate construction of complex object from its representation."""


class House:
    """Complex object to be built."""
    
    def __init__(self):
        self.foundation = None
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None
        self.interior = None
    
    def __str__(self):
        return f"House: {self.foundation}, {self.walls}, {self.roof}, {self.windows}, {self.doors}, {self.interior}"


class HouseBuilder:
    """Abstract builder interface."""
    
    def __init__(self):
        self.house = House()
    
    def build_foundation(self):
        raise NotImplementedError
    
    def build_walls(self):
        raise NotImplementedError
    
    def build_roof(self):
        raise NotImplementedError
    
    def build_windows(self):
        raise NotImplementedError
    
    def build_doors(self):
        raise NotImplementedError
    
    def build_interior(self):
        raise NotImplementedError
    
    def get_house(self):
        return self.house


class ConcreteHouseBuilder(HouseBuilder):
    """Concrete builder for building a standard house."""
    
    def build_foundation(self):
        self.house.foundation = "Concrete foundation"
    
    def build_walls(self):
        self.house.walls = "Brick walls"
    
    def build_roof(self):
        self.house.roof = "Tiled roof"
    
    def build_windows(self):
        self.house.windows = "Wooden windows"
    
    def build_doors(self):
        self.house.doors = "Wooden doors"
    
    def build_interior(self):
        self.house.interior = "Painted walls and wooden floors"


class ModernHouseBuilder(HouseBuilder):
    """Concrete builder for building a modern house."""
    
    def build_foundation(self):
        self.house.foundation = "Steel-reinforced concrete"
    
    def build_walls(self):
        self.house.walls = "Glass and steel walls"
    
    def build_roof(self):
        self.house.roof = "Solar panel roof"
    
    def build_windows(self):
        self.house.windows = "Double-glazed windows"
    
    def build_doors(self):
        self.house.doors = "Automated glass doors"
    
    def build_interior(self):
        self.house.interior = "Smart home systems and marble floors"


class HouseConstructor:
    """Director that constructs the house."""
    
    def __init__(self, builder: HouseBuilder):
        self.builder = builder
    
    def construct_house(self):
        self.builder.build_foundation()
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_windows()
        self.builder.build_doors()
        self.builder.build_interior()
        return self.builder.get_house()


# Demonstration
if __name__ == "__main__":
    # Building a standard house
    builder = ConcreteHouseBuilder()
    constructor = HouseConstructor(builder)
    house1 = constructor.construct_house()
    print("Standard House:")
    print(house1)
    
    # Building a modern house
    builder = ModernHouseBuilder()
    constructor = HouseConstructor(builder)
    house2 = constructor.construct_house()
    print("\nModern House:")
    print(house2)
